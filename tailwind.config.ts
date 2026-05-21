import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        headline: ["var(--font-plus-jakarta-sans)", "sans-serif"],
        body: ["var(--font-be-vietnam-pro)", "sans-serif"],
        sans: ["var(--font-be-vietnam-pro)", "system-ui", "sans-serif"],
      },
      colors: {
        bg: "#ffffff",
        "bg-dim": "#f8fafc", // Softer slate background
        fg: "#0f172a", // Deep blue-gray for better contrast
        "fg-muted": "#64748b",
        
        // Premium Dribbble Vibrant Colors
        "duo-green": "#22c55e", 
        "duo-green-border": "#16a34a",
        "duo-red": "#f43f5e",
        "duo-red-border": "#e11d48",
        "duo-red-bg": "#fff1f2",
        "duo-blue": "#3b82f6",
        "duo-blue-border": "#2563eb",
        "duo-blue-bg": "#eff6ff",
        "duo-gold": "#f59e0b",
        "duo-gold-border": "#d97706",
        "duo-gray": "#f1f5f9",
        "duo-gray-border": "#cbd5e1",

        // High-Fidelity Path Colors (from HTML draft)
        "path-primary": "#84fb42",
        "path-primary-dim": "#76ec33",
        "path-primary-container": "#58cc02",
        "path-on-primary-container": "#143b00",
        "path-surface": "#041015",
        "path-surface-variant": "#17282f",
        "path-surface-container": "#0d1c21",
        "path-surface-container-low": "#07151a",
        "path-surface-container-high": "#122228",
        "path-surface-container-highest": "#17282f",
        "path-on-surface": "#e9f6fd",
        "path-on-surface-variant": "#a0adb4",
        "path-outline": "#6b777d",
        "path-outline-variant": "#3e4a4f",
        "path-error": "#ff7351",
        "path-error-dim": "#d53d18",

        // Keep old colors mapping temporarily to avoid crashing existing components
        coin: "#f59e0b",
        "bg-card": "#ffffff",
      },
      animation: {
        "slide-up-duo": "slideUpDuo 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.1) forwards",
        "bounce-duo": "bounceDuo 2s ease-in-out infinite",
        "mascot-think": "mascotThinkDuo 3s ease-in-out infinite",
        "mascot-wiggle": "mascotWiggleDuo 1.5s ease-in-out infinite",
        "mascot-shake": "mascotShakeDuo 0.4s ease",
      },
      keyframes: {
        slideUpDuo: {
          "0%": { transform: "translateY(100%)" },
          "100%": { transform: "translateY(0)" },
        },
        bounceDuo: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-8px)" },
        },
        mascotThinkDuo: {
          "0%, 100%": { transform: "translateY(0) rotate(0deg)" },
          "50%": { transform: "translateY(-2px) rotate(2deg)" },
        },
        mascotWiggleDuo: {
          "0%, 100%": { transform: "translateY(0) rotate(0deg)" },
          "25%": { transform: "translateY(-4px) rotate(-5deg)" },
          "75%": { transform: "translateY(-4px) rotate(5deg)" },
        },
        mascotShakeDuo: {
          "0%, 100%": { transform: "translateX(0)" },
          "25%": { transform: "translateX(-4px)" },
          "75%": { transform: "translateX(4px)" },
        }
      }
    },
  },
  plugins: [],
};
export default config;
