/**
 * Iran Video Map - Frontend Application
 */

// Global state
let map;
let markers;
let allVideos = [];
let filteredVideos = [];
let currentZoom = 5;
let selectedDay = 'all';  // Current day filter
const ZOOM_THRESHOLD = 7;  // Below this = simple dots, above = colored bubbles
const PROTEST_START = '2025-12-28';  // First day of protests

// Iran center coordinates
const IRAN_CENTER = [32.4279, 53.6880];
const IRAN_ZOOM = 5;

/**
 * Initialize the Leaflet map
 */
function initMap() {
    map = L.map('map').setView(IRAN_CENTER, IRAN_ZOOM);

    // OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    // Simple layer group (no clustering - we group manually by city/location)
    markers = L.layerGroup();
    map.addLayer(markers);

    // Listen for zoom changes to update marker styles
    map.on('zoomend', function() {
        const newZoom = map.getZoom();
        if ((currentZoom < ZOOM_THRESHOLD && newZoom >= ZOOM_THRESHOLD) ||
            (currentZoom >= ZOOM_THRESHOLD && newZoom < ZOOM_THRESHOLD)) {
            currentZoom = newZoom;
            addMarkers(filteredVideos);
        }
        currentZoom = newZoom;
    });
}

/**
 * Load videos from JSON file
 */
async function loadVideos() {
    try {
        // Try to load from data folder (production)
        let response = await fetch('../data/videos.json');

        if (!response.ok) {
            // Try alternate path
            response = await fetch('./data/videos.json');
        }

        if (!response.ok) {
            console.warn('No videos.json found, using sample data');
            return getSampleData();
        }

        const data = await response.json();
        return data.videos || [];

    } catch (error) {
        console.warn('Error loading videos:', error);
        return getSampleData();
    }
}

/**
 * Sample data for testing when no videos.json exists
 */
function getSampleData() {
    return [
        {
            id: "sample1",
            title: "تظاهرات در میدان انقلاب تهران",
            location: {
                name_fa: "انقلاب",
                name_en: "Enghelab Square",
                city: "Tehran",
                lat: 35.7012,
                lng: 51.3890
            },
            thumbnail: "https://img.youtube.com/vi/dQw4w9WgXcQ/mqdefault.jpg",
            url: "https://youtube.com/watch?v=dQw4w9WgXcQ",
            uploaded: "2024-01-08T15:30:00Z",
            source: "Iran International"
        },
        {
            id: "sample2",
            title: "اعتراضات مردمی در اصفهان",
            location: {
                name_fa: "اصفهان",
                name_en: "Isfahan",
                city: "Isfahan",
                lat: 32.6539,
                lng: 51.6660
            },
            thumbnail: "https://img.youtube.com/vi/dQw4w9WgXcQ/mqdefault.jpg",
            url: "https://youtube.com/watch?v=dQw4w9WgXcQ",
            uploaded: "2024-01-07T12:00:00Z",
            source: "Manoto"
        },
        {
            id: "sample3",
            title: "گزارش از شیراز",
            location: {
                name_fa: "شیراز",
                name_en: "Shiraz",
                city: "Shiraz",
                lat: 29.5918,
                lng: 52.5837
            },
            thumbnail: "https://img.youtube.com/vi/dQw4w9WgXcQ/mqdefault.jpg",
            url: "https://youtube.com/watch?v=dQw4w9WgXcQ",
            uploaded: "2024-01-06T09:00:00Z",
            source: "Iran International"
        },
        {
            id: "sample4",
            title: "تجمع در تبریز",
            location: {
                name_fa: "تبریز",
                name_en: "Tabriz",
                city: "Tabriz",
                lat: 38.0800,
                lng: 46.2919
            },
            thumbnail: "https://img.youtube.com/vi/dQw4w9WgXcQ/mqdefault.jpg",
            url: "https://youtube.com/watch?v=dQw4w9WgXcQ",
            uploaded: "2024-01-05T18:00:00Z",
            source: "Manoto"
        }
    ];
}

/**
 * City center coordinates for grouping
 */
const CITY_CENTERS = {
    "Tehran": { lat: 35.6892, lng: 51.3890 },
    "Mashhad": { lat: 36.2605, lng: 59.6168 },
    "Isfahan": { lat: 32.6539, lng: 51.6660 },
    "Shiraz": { lat: 29.5918, lng: 52.5837 },
    "Tabriz": { lat: 38.0800, lng: 46.2919 },
    "Karaj": { lat: 35.8400, lng: 50.9391 },
    "Kermanshah": { lat: 34.3142, lng: 47.0650 },
    "Ahvaz": { lat: 31.3183, lng: 48.6706 },
    "Rasht": { lat: 37.2808, lng: 49.5832 },
    "Kerman": { lat: 30.2839, lng: 57.0834 },
    "Zanjan": { lat: 36.6736, lng: 48.4787 },
    "Sanandaj": { lat: 35.3219, lng: 46.9862 },
    "Urmia": { lat: 37.5527, lng: 45.0761 },
    "Zahedan": { lat: 29.4963, lng: 60.8629 },
    "Arak": { lat: 34.0917, lng: 49.6892 },
    "Gorgan": { lat: 36.8427, lng: 54.4353 },
    "Sari": { lat: 36.5633, lng: 53.0601 },
    "Ilam": { lat: 33.6374, lng: 46.4227 },
    "Yazd": { lat: 31.8974, lng: 54.3569 },
    "Qom": { lat: 34.6416, lng: 50.8746 },
    "Hamadan": { lat: 34.7990, lng: 48.5150 },
    "Ardabil": { lat: 38.2498, lng: 48.2933 },
    "Iran": { lat: 32.4279, lng: 53.6880 },
};

/**
 * Check if video group contains violence
 */
function hasViolence(videos) {
    return videos.some(v => (v.event_types || []).includes('repression'));
}

/**
 * Group videos by exact location
 */
function groupByLocation(videos) {
    const groups = {};

    videos.forEach(video => {
        if (!video.location || !video.location.lat) return;

        const key = `${video.location.lat},${video.location.lng}`;
        if (!groups[key]) {
            groups[key] = {
                location: video.location,
                videos: []
            };
        }
        groups[key].videos.push(video);
    });

    return groups;
}

/**
 * Group videos by city
 */
function groupByCity(videos) {
    const groups = {};

    videos.forEach(video => {
        if (!video.location || !video.location.city) return;

        const city = video.location.city;
        if (!groups[city]) {
            const center = CITY_CENTERS[city] || { lat: video.location.lat, lng: video.location.lng };
            groups[city] = {
                location: {
                    name_en: city,
                    city: city,
                    lat: center.lat,
                    lng: center.lng
                },
                videos: []
            };
        }
        groups[city].videos.push(video);
    });

    return groups;
}

/**
 * Add markers to the map
 * Simple markers: blue = footage, red = violence
 */
function addMarkers(videos) {
    markers.clearLayers();

    const isZoomedIn = map.getZoom() >= ZOOM_THRESHOLD;
    const violenceOnly = document.getElementById('filter-violence').checked;

    // Group by city (zoomed out) or location (zoomed in)
    const viewMode = isZoomedIn ? 'location' : 'city';
    const groups = viewMode === 'city' ? groupByCity(videos) : groupByLocation(videos);

    Object.values(groups).forEach(group => {
        const { location, videos } = group;

        // Determine color: red if violence, blue otherwise
        const isViolent = hasViolence(videos);
        const markerColor = isViolent ? '#dc2626' : '#2563eb';

        // Radius based on video count (subtle scaling)
        const baseRadius = viewMode === 'city' ? 16 : 12;
        const radius = Math.min(baseRadius + Math.log2(videos.length + 1) * 4, 30);

        const marker = L.circleMarker([location.lat, location.lng], {
            radius: radius,
            fillColor: markerColor,
            color: '#fff',
            weight: 2,
            opacity: 1,
            fillOpacity: 0.85
        });
        marker.videoCount = videos.length;

        // Simple popup
        const popupContent = `
            <div class="popup-location">${location.name_en}</div>
            <div class="popup-count"><strong>${videos.length}</strong> video${videos.length > 1 ? 's' : ''}</div>
        `;
        marker.bindPopup(popupContent);

        // Click handler to show sidebar
        marker.on('click', () => {
            showSidebar(location, videos);
        });

        markers.addLayer(marker);
    });

    updateStats(videos);
}

/**
 * Show sidebar with videos from a location
 */
function showSidebar(location, videos) {
    const sidebar = document.getElementById('sidebar');
    const title = document.getElementById('sidebar-title');
    const list = document.getElementById('video-list');

    title.textContent = `${location.name_en} (${videos.length})`;

    list.innerHTML = videos.map(video => `
        <div class="video-card" onclick="window.open('${video.url}', '_blank')">
            <img src="${video.thumbnail}" alt="${video.title}" loading="lazy"
                 onerror="this.src='https://via.placeholder.com/120x68?text=No+Image'">
            <div class="video-info">
                <div class="video-title">${video.title}</div>
                <div class="video-meta">${formatDate(video.uploaded)}</div>
                <span class="video-source ${getSourceClass(video.source)}">${video.source}</span>
            </div>
        </div>
    `).join('');

    sidebar.classList.remove('hidden');
}

/**
 * Hide sidebar
 */
function hideSidebar() {
    document.getElementById('sidebar').classList.add('hidden');
}

/**
 * Format date for display
 */
function formatDate(dateStr) {
    if (!dateStr) return '';
    try {
        const date = new Date(dateStr);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    } catch {
        return dateStr;
    }
}

/**
 * Get CSS class for source
 */
function getSourceClass(source) {
    if (source === 'Iran International') return 'iran-international';
    if (source === 'Manoto') return 'manoto';
    return '';
}

/**
 * Format large numbers with K/M suffix
 */
function formatNumber(num) {
    if (num >= 1000000) {
        return (num / 1000000).toFixed(1) + 'M';
    }
    if (num >= 1000) {
        return (num / 1000).toFixed(0) + 'K';
    }
    return num.toString();
}

/**
 * Calculate total participant estimate
 */
function calculateTotalEstimate(videos) {
    let total = 0;
    const seenLocations = new Set();

    videos.forEach(v => {
        if (!v.location || !v.location.lat) return;

        // Use location key to avoid counting same location multiple times
        const locKey = `${v.location.lat},${v.location.lng}`;

        // Only count the largest estimate per location
        if (!seenLocations.has(locKey)) {
            seenLocations.add(locKey);
            const estimate = v.crowd_estimate?.avg || 50;
            total += estimate;
        }
    });

    return total;
}

/**
 * Count videos per city
 */
function countByCity(videos) {
    const cities = {};
    videos.forEach(v => {
        if (!v.location?.city) return;
        const city = v.location.city;
        cities[city] = (cities[city] || 0) + 1;
    });
    return cities;
}

/**
 * Update stats display
 */
function updateStats(videos) {
    const total = videos.length;
    const located = videos.filter(v => v.location && v.location.lat).length;
    const locations = new Set(videos.filter(v => v.location?.lat).map(v => `${v.location.lat},${v.location.lng}`)).size;

    // Count cities
    const cityCounts = countByCity(videos);
    const tehranCount = cityCounts['Tehran'] || 0;

    document.getElementById('stats-total').textContent = `${total} videos`;
    document.getElementById('stats-located').textContent = `${located} on map (Tehran: ${tehranCount})`;
    document.getElementById('total-videos').textContent = total;
    document.getElementById('total-locations').textContent = locations;

    // Log city breakdown to console
    console.log('Videos per city:', cityCounts);
}

/**
 * Apply filters to videos
 */
function applyFilters() {
    const violenceOnly = document.getElementById('filter-violence').checked;

    filteredVideos = allVideos.filter(video => {
        // Day filter
        if (selectedDay !== 'all') {
            const videoDate = getVideoDate(video);
            if (videoDate !== selectedDay) {
                return false;
            }
        }

        // Violence filter - show only videos with regime violence
        if (violenceOnly) {
            const eventTypes = video.event_types || [];
            if (!eventTypes.includes('repression')) {
                return false;
            }
        }

        return true;
    });

    addMarkers(filteredVideos);
    hideSidebar();
}

/**
 * Get date string (YYYY-MM-DD) from video
 */
function getVideoDate(video) {
    if (!video.uploaded) return null;
    try {
        // Handle ISO format: 2025-12-28T00:00:00Z
        return video.uploaded.substring(0, 10);
    } catch {
        return null;
    }
}

/**
 * Build day filter buttons based on available dates in videos
 * Only counts videos that have a location (will appear on map)
 */
function buildDayFilter(videos) {
    const container = document.getElementById('day-buttons');
    if (!container) return;

    // Count videos per day - ONLY those with location
    const dayCounts = {};
    videos.forEach(video => {
        const date = getVideoDate(video);
        const hasLocation = video.location && video.location.lat;
        if (date && hasLocation) {
            dayCounts[date] = (dayCounts[date] || 0) + 1;
        }
    });

    // Sort dates
    const dates = Object.keys(dayCounts).sort();

    if (dates.length === 0) {
        container.innerHTML = '<span style="color: #999; font-size: 0.75rem;">No dates available</span>';
        return;
    }

    // Create buttons for each day
    container.innerHTML = dates.map(date => {
        const count = dayCounts[date];
        const label = formatDayLabel(date);
        return `<button class="day-btn" data-day="${date}">${label} <span class="day-count">(${count})</span></button>`;
    }).join('');

    // Add click handlers
    document.querySelectorAll('.day-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.day-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedDay = btn.dataset.day;
            applyFilters();
        });
    });
}

/**
 * Format date as short label: "Dec 28", "Jan 1", etc.
 */
function formatDayLabel(dateStr) {
    try {
        const date = new Date(dateStr + 'T12:00:00Z');
        return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    } catch {
        return dateStr;
    }
}

/**
 * Initialize the application
 */
async function init() {
    initMap();

    // Load videos
    allVideos = await loadVideos();
    filteredVideos = allVideos;

    // Build day filter buttons
    buildDayFilter(allVideos);

    // Add markers
    addMarkers(allVideos);

    // Set up event listeners
    document.getElementById('sidebar-close').addEventListener('click', hideSidebar);
    document.getElementById('filter-violence').addEventListener('change', applyFilters);

    // FlightRadar toggle
    const frToggle = document.getElementById('flightradar-toggle');
    const frPanel = document.getElementById('flightradar-panel');
    const frIframe = document.getElementById('flightradar-iframe');

    if (frToggle && frPanel) {
        frToggle.addEventListener('click', () => {
            frPanel.classList.toggle('collapsed');
            // Lazy load iframe on first open
            if (!frPanel.classList.contains('collapsed') && frIframe && frIframe.src === 'about:blank') {
                frIframe.src = frIframe.dataset.src;
            }
        });
    }

    // Close sidebar when clicking on map
    map.on('click', hideSidebar);

    console.log(`Loaded ${allVideos.length} videos`);
}

// Start the app
init();
