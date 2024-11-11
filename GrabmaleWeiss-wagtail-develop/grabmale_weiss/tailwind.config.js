/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/templates/**/*.html"],
  theme: {
    extend: {
      minHeight: {
        "100svh": "90svh", // This sets a custom min-height with 100 small viewport height
      },
      fontWeight: {
        bold: "700",
      },
      fontFamily: {
        armarante: ["Amarante", "serif"],
        rethink: ["Rethink Sans", "sans-serif"],
      },
      backgroundImage: {
        footerImg: "url('/static/assets/footer-bg.png')",
      },
      colors: {
        white: "#FFFFFF",
        lightgrey: "#EDEDED",
        mediumgrey: "#E1E1E1",
        darkgrey: "#636363",
        black: "#000000",
        gradient: "rgba(237, 237, 237, 0.5)",
      },
    },
  },
  plugins: [],
};
