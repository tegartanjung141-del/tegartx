# Robotic Arm + OpenCascade WebGL Project

Project standalone untuk visualisasi dan modeling robotic arm menggunakan WebGL murni (tanpa Unity).

## Struktur Folder

```
robotic-occ-webgl/
├── WebGLBuild/
│   └── index.html          # File utama preview 3D (Standalone)
├── OpenCascadeLib/
│   └── occt_interop.js     # Bindings untuk OpenCascade WASM (opsional)
└── Documentation/
    └── QUICKSTART.md       # Panduan penggunaan
```

## Cara Menjalankan Preview 3D

### Opsi 1: Langsung Buka File HTML (Paling Mudah)
1. Masuk ke folder `WebGLBuild`
2. Klik dua kali file `index.html`
3. Browser akan membuka tampilan robotic arm secara langsung

### Opsi 2: Menggunakan Local Server
Jika Anda ingin mengembangkan lebih lanjut atau load file eksternal:

**Windows (CMD):**
```cmd
cd path\to\robotic-occ-webgl\WebGLBuild
python -m http.server 8080
```
Lalu buka `http://localhost:8080` di browser.

**Linux/Mac:**
```bash
cd path/to/robotic-occ-webgl/WebGLBuild
python3 -m http.server 8080
```

## Fitur

- ✅ **3D Robotic Arm Visualization** - Render real-time dengan Three.js
- ✅ **Interactive Controls** - Slider untuk kontrol setiap sendi (J1-J4)
- ✅ **Gripper Control** - Buka/tutup gripper
- ✅ **Animation Mode** - Demo gerakan otomatis
- ✅ **Camera Controls** - Orbit, zoom, pan dengan mouse
- ✅ **Responsive Design** - UI modern yang adaptif
- ✅ **No Dependencies** - Tidak perlu install Unity atau engine lain

## Teknologi

- **Three.js** - Rendering 3D WebGL
- **Vanilla JavaScript** - Logika kinematika robot
- **HTML5/CSS3** - Interface pengguna
- **OpenCascade (Opsional)** - Untuk CAD modeling lanjutan (via WASM)

## Kontrol Mouse

- **Klik Kiri + Drag** - Rotasi kamera
- **Scroll Wheel** - Zoom in/out
- **Klik Kanan + Drag** - Pan kamera

## Customization

Untuk mengubah warna, ukuran, atau kinematika robot, edit file `WebGLBuild/index.html`:
- Bagian `<style>` untuk CSS/UI
- Bagian `// --- Robot Construction ---` untuk geometri robot
- Bagian `updateRobot()` untuk logika kinematika
