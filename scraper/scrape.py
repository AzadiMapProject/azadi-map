#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video scraper for Iran International and Manoto YouTube channels.
Extracts video metadata and attempts to identify locations from titles.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from locations import find_location, estimate_crowd_size, get_crowd_estimate, detect_event_type, is_protest_video

# Channel URLs - targeting shorts for location-specific content
CHANNELS = {
    "Iran International": "https://www.youtube.com/@IRANINTL/shorts",
}

# Output paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
OUTPUT_FILE = DATA_DIR / "videos.json"


def get_channel_videos(channel_url, channel_name, max_videos=10):
    """
    Use yt-dlp to get recent videos from a channel.
    Returns list of video dicts.
    """
    print(f"Fetching videos from {channel_name}...")

    try:
        # Use yt-dlp to get video info as JSON
        cmd = [
            "yt-dlp",
            "--flat-playlist",
            "--playlist-end", str(max_videos),
            "-j",
            channel_url  # URL already includes /shorts
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode != 0:
            print(f"Error fetching {channel_name}: {result.stderr}")
            return []

        videos = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            try:
                data = json.loads(line)
                video_id = data.get("id", "")
                title = data.get("title", "")

                if not video_id or not title:
                    continue

                # Filter: only protest-related videos
                if not is_protest_video(title):
                    print(f"  [SKIP] {title[:40]}... (not protest)")
                    continue

                # Try to find location in title
                location = find_location(title)

                # Estimate crowd size from title
                crowd_size = estimate_crowd_size(title)
                event_types = detect_event_type(title)

                video = {
                    "id": video_id,
                    "title": title,
                    "title_english": "",  # Could add translation later
                    "location": location,
                    "crowd_size": crowd_size,
                    "event_types": event_types,
                    "thumbnail": f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg",
                    "url": f"https://www.youtube.com/watch?v={video_id}",
                    "uploaded": data.get("upload_date", ""),
                    "source": channel_name
                }

                # Convert upload_date format if present (YYYYMMDD -> ISO)
                if video["uploaded"] and len(video["uploaded"]) == 8:
                    try:
                        d = datetime.strptime(video["uploaded"], "%Y%m%d")
                        video["uploaded"] = d.strftime("%Y-%m-%dT00:00:00Z")
                    except ValueError:
                        pass

                videos.append(video)
                loc_status = f"-> {location['name_en']}" if location else "(no location)"
                size_icon = {"very_large": "[XXL]", "large": "[XL]", "medium": "[M]", "small": "[S]"}.get(crowd_size, "")
                print(f"  {size_icon} {title[:45]}... {loc_status}")

            except json.JSONDecodeError:
                continue

        print(f"  Total: {len(videos)} videos from {channel_name}")
        return videos

    except subprocess.TimeoutExpired:
        print(f"Timeout fetching {channel_name}")
        return []
    except FileNotFoundError:
        print("ERROR: yt-dlp not found. Install with: pip install yt-dlp")
        return []


def load_existing_videos():
    """Load existing videos from JSON file if it exists."""
    if OUTPUT_FILE.exists():
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {v["id"]: v for v in data.get("videos", [])}
        except (json.JSONDecodeError, KeyError):
            pass
    return {}


def save_videos(videos):
    """Save videos to JSON file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    output = {
        "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "videos": videos
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(videos)} videos to {OUTPUT_FILE}")


def main():
    """Main scraper function."""
    print("=" * 60)
    print("Iran Video Map - Scraper")
    print("=" * 60)

    # Get max videos from command line or default to 10
    max_videos = 10
    if len(sys.argv) > 1:
        try:
            max_videos = int(sys.argv[1])
        except ValueError:
            print(f"Invalid number: {sys.argv[1]}, using default 10")

    # Load existing videos to merge
    existing = load_existing_videos()
    print(f"Loaded {len(existing)} existing videos")

    # Fetch from all channels
    all_videos = []
    for channel_name, channel_url in CHANNELS.items():
        videos = get_channel_videos(channel_url, channel_name, max_videos)
        all_videos.extend(videos)

    # Merge with existing (new videos override old)
    for video in all_videos:
        existing[video["id"]] = video

    # Convert back to list and sort by upload date (newest first)
    videos_list = list(existing.values())
    videos_list.sort(key=lambda x: x.get("uploaded", ""), reverse=True)

    # Save
    save_videos(videos_list)

    # Stats
    with_location = sum(1 for v in videos_list if v.get("location"))
    print(f"\nStats:")
    print(f"  Total videos: {len(videos_list)}")
    print(f"  With location: {with_location}")
    print(f"  Without location: {len(videos_list) - with_location}")


if __name__ == "__main__":
    main()
