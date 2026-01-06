#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

old_header = '''                <header class="bg-indigo-900/90 text-white sticky top-0">
                    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <div class="flex justify-between items-center h-16">
                            <div class="flex items-center space-x-3">
                                <a href="../../index.html" class="flex items-center gap-3">
                                    <img src="../../images/Lambang Banyumas Asli.png" alt="Logo" class="w-10 h-10 rounded-full bg-white p-1">
                                    <span class="font-bold">Purwokerto Selatan</span>
                                </a>
                            </div>
                            <div class="hidden md:flex space-x-2 items-center">
                                <a href="../../index.html" class="px-3 py-2 text-sm rounded-md hover:bg-white/5">Beranda</a>
                                <div class="relative">
                                    <button id="desa-dropdown-btn" class="px-3 py-2 text-sm rounded-md hover:bg-white/5" aria-expanded="false">Peta Desa</button>
                                    <div id="desa-dropdown-menu" class="absolute left-0 top-full mt-1 w-44 dropdown-menu bg-white text-slate-800 rounded-lg shadow-lg">
                                        <a href="../berkoh/index.html" class="block px-4 py-2 text-sm hover:bg-slate-100">Berkoh</a>
                                        <a href="../karangklesem/index.html" class="block px-4 py-2 text-sm hover:bg-slate-100">Karangklesem</a>
                                        <a href="../karangpucung/index.html" class="block px-4 py-2 text-sm hover:bg-slate-100">Karangpucung</a>
                                        <a href="../teluk/index.html" class="block px-4 py-2 text-sm hover:bg-slate-100">Teluk</a>
                                    </div>
                                </div>
                                <a href="../../index.html#about" class="px-3 py-2 text-sm rounded-md hover:bg-white/5">Tentang</a>
                            </div>
                            <button id="mobile-menu-btn" class="md:hidden p-2 rounded-md">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                            </button>
                        </div>
                        <div id="mobile-menu" class="hidden md:hidden pb-4 bg-indigo-900 px-4">
                            <a href="../../index.html" class="block px-3 py-3">Beranda</a>
                            <a href="../berkoh/index.html" class="block px-3 py-3">Berkoh</a>
                            <a href="../karangklesem/index.html" class="block px-3 py-3">Karangklesem</a>
                            <a href="../karangpucung/index.html" class="block px-3 py-3">Karangpucung</a>
                            <a href="../teluk/index.html" class="block px-3 py-3">Teluk</a>
                            <a href="../../index.html#about" class="block px-3 py-3">Tentang</a>
                        </div>
                    </nav>
                </header>'''

new_header = '''                <header class="bg-indigo-900/90 backdrop-blur-md text-white shadow-lg sticky top-0 z-50 transition-all duration-300">
                    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <div class="flex justify-between items-center h-16">
                            <div class="flex items-center space-x-3 group cursor-pointer">
                                <a href="../../index.html" class="flex items-center gap-3">
                                    <div class="relative">
                                        <div class="absolute inset-0 bg-yellow-400 rounded-full blur opacity-0 group-hover:opacity-50 transition-opacity duration-500"></div>
                                        <img src="../../images/Lambang Banyumas Asli.png" alt="Logo" class="relative w-10 h-10 rounded-full bg-white p-1 shadow-sm transition-transform group-hover:rotate-12">
                                    </div>
                                    <span class="font-bold">Purwokerto Selatan</span>
                                </a>
                            </div>
                            <div class="hidden md:flex space-x-1 lg:space-x-2 items-center">
                                <a href="../../index.html" class="nav-link px-4 py-2 text-sm font-medium rounded-md hover:bg-white/5 transition">Beranda</a>
                                <a href="../../purwokerto selatan/index.html" class="nav-link px-4 py-2 text-sm font-medium rounded-md hover:bg-white/5 transition">Peta Kecamatan</a>
                                <div class="relative group" tabindex="0">
                                    <button id="desa-dropdown-btn" class="nav-link px-4 py-2 text-sm font-medium rounded-md hover:bg-white/5 transition flex items-center" aria-expanded="false">Peta Desa
                                        <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                                    </button>
                                    <div id="desa-dropdown-menu" class="absolute left-0 top-full mt-0 w-44 dropdown-menu bg-white text-slate-800 rounded-lg shadow-lg opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto group-focus-within:opacity-100 group-focus-within:pointer-events-auto transform scale-95 group-hover:scale-100 group-focus-within:scale-100 transition-all">
                                        <a href="../berkoh/index.html" class="block px-4 py-2 text-sm hover:bg-slate-100">Berkoh</a>
                                        <a href="../karangklesem/index.html" class="block px-4 py-2 text-sm hover:bg-slate-100">Karangklesem</a>
                                        <a href="../karangpucung/index.html" class="block px-4 py-2 text-sm hover:bg-slate-100">Karangpucung</a>
                                        <a href="../teluk/index.html" class="block px-4 py-2 text-sm hover:bg-slate-100">Teluk</a>
                                    </div>
                                </div>
                                <a href="../../index.html#about" class="nav-link px-4 py-2 text-sm font-medium rounded-md hover:bg-white/5 transition">Tentang Saya</a>
                            </div>
                            <button id="mobile-menu-btn" class="md:hidden p-2 rounded-md hover:bg-white/10 transition active:scale-95">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                            </button>
                        </div>
                        <div id="mobile-menu" class="hidden md:hidden pb-4 bg-indigo-900 absolute left-0 right-0 px-4 shadow-xl border-t border-indigo-800">
                            <a href="../../index.html" class="block px-3 py-3 text-base font-medium hover:bg-white/10 rounded-md border-b border-white/5">Beranda</a>
                            <a href="../../purwokerto selatan/index.html" class="block px-3 py-3 text-base font-medium hover:bg-white/10 rounded-md border-b border-white/5">Peta Kecamatan</a>
                            <a href="../berkoh/index.html" class="block px-3 py-3 text-base font-medium hover:bg-white/10 rounded-md border-b border-white/5">Berkoh</a>
                            <a href="../karangklesem/index.html" class="block px-3 py-3 text-base font-medium hover:bg-white/10 rounded-md border-b border-white/5">Karangklesem</a>
                            <a href="../karangpucung/index.html" class="block px-3 py-3 text-base font-medium hover:bg-white/10 rounded-md border-b border-white/5">Karangpucung</a>
                            <a href="../teluk/index.html" class="block px-3 py-3 text-base font-medium hover:bg-white/10 rounded-md border-b border-white/5">Teluk</a>
                            <a href="../../index.html#about" class="block px-3 py-3 text-base font-medium hover:bg-white/10 rounded-md">Tentang</a>
                        </div>
                    </nav>
                </header>'''

# Update karangpucung
with open('desa/karangpucung/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(old_header, new_header)

with open('desa/karangpucung/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ karangpucung navbar updated")

# Update teluk
with open('desa/teluk/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(old_header, new_header)

with open('desa/teluk/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ teluk navbar updated")
print("\n✅ Semua navbar desa pages sudah diupdate!")
