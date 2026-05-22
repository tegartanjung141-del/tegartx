// OpenCascade JavaScript Interop untuk Unity WebGL
// File ini harus di-copy ke Assets/OpenCascadeLib/occt_interop.js

/**
 * OpenCascade WASM Module Initialization
 */
var OCCTModule = (function() {
    var Module = typeof Module !== 'undefined' ? Module : {};
    
    Module.onRuntimeInitialized = function() {
        console.log('OpenCascade WASM initialized');
        OCCT_Initialize();
    };
    
    return Module;
})();

/**
 * Initialize OpenCascade
 */
function OCCT_Initialize() {
    try {
        // Initialize OCCT kernel
        if (typeof OCCTModule !== 'undefined') {
            console.log('OCCT Kernel initialized');
            return true;
        }
        return false;
    } catch (e) {
        console.error('Failed to initialize OCCT:', e);
        return false;
    }
}

/**
 * Cleanup OpenCascade resources
 */
function OCCT_Cleanup() {
    console.log('OCCT cleanup');
}

/**
 * Create box primitive
 * @param {number} x - X dimension
 * @param {number} y - Y dimension
 * @param {number} z - Z dimension
 * @returns {number} Shape ID
 */
function OCCT_CreateBox(x, y, z) {
    console.log(`Creating box: ${x} x ${y} x ${z}`);
    // Placeholder - implementasi actual tergantung OCCT WASM bindings
    return 1;
}

/**
 * Create cylinder primitive
 * @param {number} radius - Cylinder radius
 * @param {number} height - Cylinder height
 * @returns {number} Shape ID
 */
function OCCT_CreateCylinder(radius, height) {
    console.log(`Creating cylinder: r=${radius}, h=${height}`);
    return 2;
}

/**
 * Create sphere primitive
 * @param {number} radius - Sphere radius
 * @returns {number} Shape ID
 */
function OCCT_CreateSphere(radius) {
    console.log(`Creating sphere: r=${radius}`);
    return 3;
}

/**
 * Export shape to STL format
 * @param {number} shapeId - Shape ID
 * @param {string} filename - Output filename
 * @returns {boolean} Success status
 */
function OCCT_ExportToSTL(shapeId, filename) {
    console.log(`Exporting shape ${shapeId} to ${filename}`);
    return true;
}

/**
 * Import shape from STL file
 * @param {string} filename - Input filename
 * @returns {number} Shape ID
 */
function OCCT_ImportFromSTL(filename) {
    console.log(`Importing shape from ${filename}`);
    return 4;
}

/**
 * Get vertices dari shape
 * @param {number} shapeId - Shape ID
 * @returns {Object} Object containing vertices array and count
 */
function OCCT_GetShapeVertices(shapeId) {
    console.log(`Getting vertices for shape ${shapeId}`);
    
    // Placeholder data - actual implementation akan extract vertices dari OCCT shape
    var vertices = [];
    var count = 0;
    
    // Example: Box vertices (8 corners)
    if (shapeId === 1) {
        vertices = [
            -0.5, -0.5, -0.5,
             0.5, -0.5, -0.5,
             0.5,  0.5, -0.5,
            -0.5,  0.5, -0.5,
            -0.5, -0.5,  0.5,
             0.5, -0.5,  0.5,
             0.5,  0.5,  0.5,
            -0.5,  0.5,  0.5
        ];
        count = vertices.length;
    }
    
    return { vertices: vertices, count: count };
}

/**
 * Translate shape
 * @param {number} shapeId - Shape ID
 * @param {number} x - X translation
 * @param {number} y - Y translation
 * @param {number} z - Z translation
 */
function OCCT_TranslateShape(shapeId, x, y, z) {
    console.log(`Translating shape ${shapeId} by (${x}, ${y}, ${z})`);
}

/**
 * Rotate shape
 * @param {number} shapeId - Shape ID
 * @param {number} angle - Rotation angle in radians
 * @param {number} ax - Axis X
 * @param {number} ay - Axis Y
 * @param {number} az - Axis Z
 */
function OCCT_RotateShape(shapeId, angle, ax, ay, az) {
    console.log(`Rotating shape ${shapeId} by ${angle} rad around (${ax}, ${ay}, ${az})`);
}

/**
 * Scale shape
 * @param {number} shapeId - Shape ID
 * @param {number} factor - Scale factor
 */
function OCCT_ScaleShape(shapeId, factor) {
    console.log(`Scaling shape ${shapeId} by factor ${factor}`);
}

/**
 * Load WASM module
 */
function loadOCCTWasm() {
    var script = document.createElement('script');
    script.src = 'occt.wasm.js';
    script.onload = function() {
        console.log('OCCT WASM module loaded');
    };
    document.head.appendChild(script);
}

// Auto-load WASM module
if (typeof window !== 'undefined') {
    loadOCCTWasm();
}

// Export functions untuk Unity WebGL
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        OCCT_Initialize: OCCT_Initialize,
        OCCT_Cleanup: OCCT_Cleanup,
        OCCT_CreateBox: OCCT_CreateBox,
        OCCT_CreateCylinder: OCCT_CreateCylinder,
        OCCT_CreateSphere: OCCT_CreateSphere,
        OCCT_ExportToSTL: OCCT_ExportToSTL,
        OCCT_ImportFromSTL: OCCT_ImportFromSTL,
        OCCT_GetShapeVertices: OCCT_GetShapeVertices,
        OCCT_TranslateShape: OCCT_TranslateShape,
        OCCT_RotateShape: OCCT_RotateShape,
        OCCT_ScaleShape: OCCT_ScaleShape
    };
}
