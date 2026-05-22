# Quick Start Guide - Robotic + OpenCascade WebGL

## Langkah Cepat Setup Project

### 1. Persiapan Environment

```bash
# Pastikan Unity Hub terinstall
# Download dari: https://unity.com/download

# Install Unity Editor versi 2021.3 LTS atau lebih baru
# Via Unity Hub → Installs → Install Editor

# Install WebGL Build Support
# Via Unity Hub → Installs → Add Modules → WebGL Build Support
```

### 2. Setup Project di Unity

```bash
# Buka Unity Hub
# Klik "Add" → Pilih folder /workspace/robotic-occ-webgl
# Atau buka langsung dari Unity Editor: File → Open Project
```

### 3. Import OpenCascade WASM

**Option A: Download Pre-built OCCT WASM**
```bash
# Clone OCCT repository
cd /workspace/robotic-occ-webgl/OpenCascadeLib
git clone https://github.com/Open-Cascade-SAS/OCCT.git

# Atau download pre-built WASM dari:
# https://github.com/occt/occt/tree/master/js
```

**Option B: Build OCCT WASM dari Source**
```bash
cd /workspace/robotic-occ-webgl/OpenCascadeLib
git clone https://github.com/Open-Cascade-SAS/OCCT.git
cd OCCT

# Setup build environment (membutuhkan Emscripten)
mkdir build_wasm && cd build_wasm
cmake .. -DCMAKE_TOOLCHAIN_FILE=../cmake/toolchains/wasm.cmake
make -j4

# Copy hasil build ke folder project
cp js/occt.wasm ../../
cp js/occt.js ../../
```

### 4. Setup Unity Scene

1. **Buka/Buat Scene Baru**
   - File → New Scene atau buka `Assets/Scenes/MainScene`

2. **Tambahkan GameObjects**
   ```
   Hierarchy:
   ├── Main Camera
   ├── Directional Light
   ├── RoboticArm (Empty GameObject)
   │   └── RoboticArmController (component)
   ├── OpenCascadeManager (Empty GameObject)
   │   └── OpenCascadeWrapper (component)
   └── InteractionController (Empty GameObject)
       └── WebGLInteractionController (component)
   ```

3. **Attach Scripts**
   - Select `RoboticArm` → Add Component → RoboticArmController
   - Select `OpenCascadeManager` → Add Component → OpenCascadeWrapper
   - Select `InteractionController` → Add Component → WebGLInteractionController

4. **Configure Components**
   
   **RoboticArmController:**
   - Joint Count: 6
   - Segment Lengths: [1, 1, 1, 1, 1, 1]
   - Joint Radius: 0.1
   - Segment Radius: 0.05

   **OpenCascadeWrapper:**
   - WASM Module Path: "OpenCascadeLib/occt.wasm"
   - Memory Size: 256

   **WebGLInteractionController:**
   - Rotation Speed: 2.0
   - Zoom Speed: 5.0
   - Min Zoom: 1.0
   - Max Zoom: 50.0

### 5. Build Settings Configuration

1. **File → Build Settings**
2. **Pilih Platform: WebGL**
3. **Klik Player Settings**

**Player Settings:**
```
Company Name: [Your Company]
Product Name: Robotic OCC WebGL

Resolution:
- Default Width: 1920
- Default Height: 1080

Publishing Settings:
- Compression Format: Brotli
- Decompression Fallback: ✓
- Memory Size: 512 MB
- Enable Exceptions: Full With Stacktrace

Other Settings:
- Scripting Backend: IL2CPP
- API Compatibility: .NET Standard 2.1
- Color Space: Linear
```

### 6. Build & Run

1. **Build Project**
   - File → Build Settings → Build
   - Pilih folder output: `WebGLBuild/`

2. **Run Local Server**
   ```bash
   cd /workspace/robotic-occ-webgl/WebGLBuild
   
   # Python
   python -m http.server 8080
   
   # Atau Node.js
   npx http-server -p 8080
   ```

3. **Open Browser**
   ```
   http://localhost:8080
   ```

### 7. Testing Controls

**Camera Controls:**
- Left Mouse: Orbit/Rotate
- Right/Middle Mouse: Pan
- Scroll Wheel: Zoom
- R: Reset Camera
- H: Home View
- Tab: Toggle UI

**Demo Controls:**
- Space: Toggle Auto-Rotate
- 1: Create Box
- 2: Create Cylinder
- 3: Create Sphere
- P: Print End-Effector Position
- W: Workspace Info
- S: Screenshot
- F: Fullscreen

### 8. Troubleshooting

**Issue: WebGL tidak load**
```
Solution:
- Cek console browser untuk errors
- Pastikan file .wasm ter-load dengan benar
- Cek MIME types di web server
```

**Issue: Out of Memory**
```
Solution:
- Increase memory size di Player Settings
- Reduce model complexity
- Enable memory profiler
```

**Issue: Performance lambat**
```
Solution:
- Lower quality settings
- Disable shadows
- Reduce draw calls
- Use LOD
```

### 9. Next Steps

1. **Customize Robotic Arm**
   - Edit segment lengths
   - Set joint limits
   - Add custom materials

2. **Import CAD Models**
   - Export dari CAD software ke STL/STEP
   - Import via OpenCascade
   - Convert ke Unity mesh

3. **Add UI Controls**
   - Create Canvas UI
   - Add sliders untuk joint control
   - Add buttons untuk actions

4. **Deploy to Web**
   - Upload ke web hosting
   - Configure CDN
   - Enable HTTPS

## Resources

- **Unity WebGL Docs**: https://docs.unity3d.com/Manual/webgl.html
- **OpenCascade**: https://dev.opencascade.org/
- **WebAssembly**: https://webassembly.org/
- **Three.js** (alternatif): https://threejs.org/

## Support

Untuk pertanyaan atau issues:
1. Check dokumentasi di `/Documentation/`
2. Review README.md
3. Check Unity Console untuk errors
4. Test di multiple browsers

Happy Coding! 🚀
