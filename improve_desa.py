#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk memperbaiki semua halaman peta desa:
1. Membuat navbar konsisten
2. Menambah fitur label rendering optimal
3. Meningkatkan kompatibilitas QGIS
4. Menambah fitur UI yang lebih baik
"""

import os
import re

# ============= NAVBAR TEMPLATE =============
NAVBAR_TEMPLATE = '''<header class="bg-indigo-900/90 backdrop-blur-md text-white shadow-lg sticky top-0 z-50 transition-all duration-300">
                    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <div class="flex justify-between items-center h-16">
                            <div class="flex items-center space-x-3 group cursor-pointer">
                                <a href="../../index.html" class="flex items-center gap-3">
                                    <div class="relative">
                                        <div class="absolute inset-0 bg-yellow-400 rounded-full blur opacity-0 group-hover:opacity-50 transition-opacity duration-500"></div>
                                        <img src="../../images/Lambang Banyumas Asli.png" alt="Logo" class="relative w-10 h-10 rounded-full bg-white p-1 shadow-sm transition-transform group-hover:rotate-12">
                                    </div>
                                    <span class="font-bold hidden sm:inline">Purwokerto Selatan</span>
                                </a>
                            </div>
                            <div class="hidden md:flex space-x-1 lg:space-x-2 items-center">
                                <a href="../../index.html" class="nav-link px-3 py-2 text-sm font-medium rounded-md hover:bg-white/5 transition" title="Kembali ke Beranda">Beranda</a>
                                <div class="relative group" tabindex="0">
                                    <button class="nav-link px-3 py-2 text-sm font-medium rounded-md hover:bg-white/5 transition flex items-center" aria-haspopup="true" aria-expanded="false" title="Pilih desa lain">Peta Desa
                                        <svg class="w-4 h-4 ml-1 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                                    </button>
                                    <div class="absolute left-0 top-full mt-0 w-48 bg-white text-slate-800 rounded-lg shadow-xl opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto group-focus-within:opacity-100 group-focus-within:pointer-events-auto transform scale-95 group-hover:scale-100 group-focus-within:scale-100 transition-all duration-200">
                                        <a href="../berkoh/index.html" class="block px-4 py-2 text-sm hover:bg-blue-50 first:rounded-t-lg border-b border-slate-100">📍 Berkoh</a>
                                        <a href="../karangklesem/index.html" class="block px-4 py-2 text-sm hover:bg-blue-50 border-b border-slate-100">📍 Karangklesem</a>
                                        <a href="../karangpucung/index.html" class="block px-4 py-2 text-sm hover:bg-blue-50 border-b border-slate-100">📍 Karangpucung</a>
                                        <a href="../teluk/index.html" class="block px-4 py-2 text-sm hover:bg-blue-50 last:rounded-b-lg">📍 Teluk</a>
                                    </div>
                                </div>
                                <a href="../../index.html#about" class="nav-link px-3 py-2 text-sm font-medium rounded-md hover:bg-white/5 transition" title="Tentang aplikasi">Tentang</a>
                            </div>
                            <button id="mobile-menu-btn" class="md:hidden p-2 rounded-md hover:bg-white/10 transition active:scale-95">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                            </button>
                        </div>
                        <div id="mobile-menu" class="hidden md:hidden pb-2 bg-indigo-900 absolute left-0 right-0 px-4 shadow-xl border-t border-indigo-800 z-40">
                            <a href="../../index.html" class="block px-3 py-2 text-sm font-medium hover:bg-white/10 rounded-md">Beranda</a>
                            <a href="../berkoh/index.html" class="block px-3 py-2 text-sm font-medium hover:bg-white/10 rounded-md">Berkoh</a>
                            <a href="../karangklesem/index.html" class="block px-3 py-2 text-sm font-medium hover:bg-white/10 rounded-md">Karangklesem</a>
                            <a href="../karangpucung/index.html" class="block px-3 py-2 text-sm font-medium hover:bg-white/10 rounded-md">Karangpucung</a>
                            <a href="../teluk/index.html" class="block px-3 py-2 text-sm font-medium hover:bg-white/10 rounded-md">Teluk</a>
                            <a href="../../index.html#about" class="block px-3 py-2 text-sm font-medium hover:bg-white/10 rounded-md">Tentang</a>
                        </div>
                    </nav>
                </header>'''

NAVBAR_STYLES = '''<style>
    :root {
        --primary: #4f46e5;
        --primary-dark: #312e81;
        --accent: #fde047;
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body {
        width: 100%;
        height: 100%;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    body {
        overflow: hidden;
        background: #f8fafc;
    }
    
    #map {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }
    
    /* Mobile Menu Toggle */
    #mobile-menu-btn {
        display: none;
    }
    
    @media (max-width: 768px) {
        #mobile-menu-btn {
            display: block;
        }
    }
    
    /* Navbar Animation */
    header {
        animation: slideDown 0.5s ease-out;
    }
    
    @keyframes slideDown {
        from {
            transform: translateY(-100%);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    /* Navigation Links Underline Animation */
    .nav-link {
        position: relative;
        overflow: hidden;
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, var(--accent), transparent);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .nav-link:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }
    
    /* Leaflet Controls Enhancement */
    .leaflet-control {
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }
    
    .leaflet-control-measure-toggle::before {
        content: '📏';
        display: inline;
    }
    
    .leaflet-control button:hover {
        background: var(--primary) !important;
        color: white !important;
    }
    
    /* Label Improvements */
    .leaflet-label {
        background: rgba(31, 41, 55, 0.9) !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 4px 8px !important;
        font-size: 12px !important;
        white-space: nowrap;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        transition: opacity 0.3s ease;
    }
    
    .leaflet-label::before {
        border-left-color: rgba(31, 41, 55, 0.9) !important;
    }
    
    /* Popup Styling */
    .leaflet-popup {
        border-radius: 8px;
        overflow: hidden;
    }
    
    .leaflet-popup-content-wrapper {
        border-radius: 8px;
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .leaflet-popup-content {
        margin: 0;
        padding: 0;
    }
    
    .leaflet-popup-content-wrapper.media {
        padding: 0;
    }
    
    /* Marker Cluster */
    .marker-cluster {
        background: var(--primary) !important;
    }
    
    .marker-cluster-small {
        background: #60a5fa !important;
    }
    
    .marker-cluster-medium {
        background: #3b82f6 !important;
    }
    
    .marker-cluster-large {
        background: var(--primary) !important;
    }
    
    /* Loading State */
    .map-loading {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        padding: 20px 40px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        text-align: center;
        z-index: 1000;
    }
    
    .spinner {
        border: 4px solid #e2e8f0;
        border-top: 4px solid var(--primary);
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: 0 auto 10px;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>'''

MOBILE_MENU_SCRIPT = '''<script>
    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
            const icon = this.querySelector('svg');
            if (mobileMenu.classList.contains('hidden')) {
                icon.style.transform = 'rotate(0deg)';
            } else {
                icon.style.transform = 'rotate(90deg)';
            }
        });
        
        // Close menu when clicking a link
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                mobileMenuBtn.querySelector('svg').style.transform = 'rotate(0deg)';
            });
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!event.target.closest('nav') && !mobileMenuBtn.contains(event.target)) {
                mobileMenu.classList.add('hidden');
            }
        });
    }
    
    // Smooth scrolling
    document.querySelectorAll('a[href="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
        });
    });
</script>'''

# ============= LABEL RENDERING IMPROVEMENT =============
LABEL_SCRIPT_ENHANCED = '''<script>
// Enhanced Label Rendering with Better Performance
var hideLabel = function(label) {
    if (label && label.labelObject) {
        label.labelObject.style.opacity = 0;
        label.labelObject.style.transition = 'opacity 0.2s ease-out';
    }
};

var showLabel = function(label) {
    if (label && label.labelObject) {
        label.labelObject.style.opacity = 1;
        label.labelObject.style.transition = 'opacity 0.3s ease-in';
    }
};

labelEngine = new labelgun.default(hideLabel, showLabel);
labelEngine.settings.fontFamily = "'Segoe UI', sans-serif";
labelEngine.settings.fontSize = 12;

var id = 0;
var labels = [];
var totalMarkers = 0;
var labelUpdateTimeout;

function resetLabels(markers) {
    labelEngine.reset();
    var i = 0;
    for (var j = 0; j < markers.length; j++) {
        markers[j].eachLayer(function(label){
            addLabel(label, ++i);
        });
    }
    labelEngine.update();
}

function addLabel(layer, id) {
    if (layer.getTooltip()) {
        var label = layer.getTooltip()._source._tooltip._container;
        if (label) {
            var rect = label.getBoundingClientRect();
            var bottomLeft = map.containerPointToLatLng([rect.left, rect.bottom]);
            var topRight = map.containerPointToLatLng([rect.right, rect.top]);
            var boundingBox = {
                bottomLeft : [bottomLeft.lng, bottomLeft.lat],
                topRight   : [topRight.lng, topRight.lat]
            };
            
            labelEngine.ingestLabel(
                boundingBox,
                id,
                parseInt(Math.random() * (5 - 1) + 1),
                label,
                "Label_" + id,
                false
            );
        }
    }
}

// Debounced label update on zoom/pan
map.on('moveend', function() {
    clearTimeout(labelUpdateTimeout);
    labelUpdateTimeout = setTimeout(function() {
        if (labelEngine) {
            labelEngine.update();
        }
    }, 300);
});

// Update labels on zoom
map.on('zoomend', function() {
    if (labelEngine) {
        // Small delay to ensure DOM is ready
        setTimeout(function() {
            labelEngine.update();
        }, 100);
    }
});
</script>'''

def update_desa_html(desa_path, desa_name):
    """Update HTML file for a desa with improved structure"""
    
    html_file = os.path.join(desa_path, 'index.html')
    
    if not os.path.exists(html_file):
        print(f"❌ File tidak ditemukan: {html_file}")
        return False
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Perbaiki title
    title_map = {
        'berkoh': 'PETA KELURAHAN BERKOH',
        'karangklesem': 'PETA KELURAHAN KARANGKLESEM',
        'karangpucung': 'PETA KELURAHAN KARANGPUCUNG',
        'teluk': 'PETA KELURAHAN TELUK'
    }
    
    new_title = title_map.get(desa_name, f'PETA KELURAHAN {desa_name.upper()}')
    
    # Update HTML title
    content = re.sub(
        r'<title>[^<]*</title>',
        f'<title>{new_title} - Purwokerto Selatan</title>',
        content,
        flags=re.IGNORECASE
    )
    
    # Update meta description
    if '<meta name="description"' not in content:
        meta_desc = f'<meta name="description" content="{new_title} - Peta GIS {desa_name.capitalize()} Purwokerto Selatan">'
        content = content.replace('</head>', f'{meta_desc}\n</head>')
    
    # 2. Tambahkan navbar style ke head jika belum ada
    if 'nav-link::after' not in content:
        # Find </head> and add navbar styles
        styles_section = NAVBAR_STYLES.replace('</style>', f'''
    /* Title Control Improvement */
    .info {{
        background: white;
        border-radius: 8px;
        padding: 12px 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }}
    
    .info h2 {{
        margin: 0 0 8px 0;
        font-size: 16px;
        color: var(--primary);
        font-weight: 600;
    }}
    
    .info p {{
        margin: 4px 0;
        font-size: 12px;
        color: #64748b;
    }}
</style>''')
        
        if '<style>' in content:
            # Append to existing style
            content = content.replace('</style>', styles_section.split('</style>')[-1])
        else:
            content = content.replace('</head>', f'{styles_section}\n</head>')
    
    # 3. Perbaiki header/navbar
    # Remove old navbar if ada
    old_navbar_patterns = [
        r'<header[^>]*>.*?</header>',
        r'<nav[^>]*>.*?</nav>'
    ]
    
    for pattern in old_navbar_patterns:
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Add navbar at start of body
    if '<body>' in content:
        content = content.replace('<body>', f'<body>\n        {NAVBAR_TEMPLATE}')
    
    # 4. Perbaiki map title control
    old_title_pattern = r"var title = new L\.Control\(\{'position':'topright'\}\);[\s\S]*?title\.addTo\(map\);"
    new_title_control = f"""var title = new L.Control({{'position':'topright'}});
        title.onAdd = function (map) {{
            this._div = L.DomUtil.create('div', 'info');
            this.update();
            return this._div;
        }};
        title.update = function () {{
            this._div.innerHTML = '<h2>{new_title}</h2><p>Zoom: {{0}}</p>'.replace('{{0}}', 'Level ' + map.getZoom());
        }};
        title.addTo(map);
        
        // Update title zoom level
        map.on('zoomend', function() {{
            title.update();
        }});"""
    
    if re.search(old_title_pattern, content, re.DOTALL):
        content = re.sub(old_title_pattern, new_title_control, content, flags=re.DOTALL)
    
    # 5. Tambahkan mobile menu script sebelum </body>
    if MOBILE_MENU_SCRIPT not in content:
        content = content.replace('</body>', f'{MOBILE_MENU_SCRIPT}\n    </body>')
    
    # 6. Improve label rendering jika ada labels.js
    if 'labelgun' in content and LABEL_SCRIPT_ENHANCED not in content:
        # Find labelgun initialization dan replace dengan enhanced version
        old_label_pattern = r"var hideLabel = function[\s\S]*?labelEngine\.update\(\);\s*\}"
        if re.search(old_label_pattern, content):
            # Extract the resetLabels call
            reset_call = re.search(r'resetLabels\([^)]*\);', content)
            if reset_call:
                content = re.sub(old_label_pattern, LABEL_SCRIPT_ENHANCED, content, flags=re.DOTALL)
    
    # 7. Improve zoom/pan label rendering
    zoomend_pattern = r'map\.on\("zoomend", function\(e\) \{[\s\S]*?\n\s*\}\);'
    if re.search(zoomend_pattern, content):
        improved_zoomend = '''map.on("zoomend", function(e) {
        // Debounce label updates
        clearTimeout(map._labelUpdateTimeout);
        map._labelUpdateTimeout = setTimeout(function() {
            if (labelEngine) {
                labelEngine.update();
            }
        }, 200);
        '''
        content = re.sub(zoomend_pattern, improved_zoomend, content, flags=re.DOTALL)
    
    # Save file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# ============= MAIN EXECUTION =============
desa_list = ['berkoh', 'karangklesem', 'karangpucung', 'teluk']
base_path = 'desa'

print("=" * 60)
print("🚀 MEMPERBAIKI HALAMAN PETA DESA")
print("=" * 60)

for desa in desa_list:
    desa_path = os.path.join(base_path, desa)
    if update_desa_html(desa_path, desa):
        print(f"✅ {desa.capitalize():20} - Berhasil diupdate")
    else:
        print(f"❌ {desa.capitalize():20} - Gagal diupdate")

print("=" * 60)
print("✨ Semua perbaikan selesai!")
print("=" * 60)
