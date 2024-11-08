/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/templates/**/*.html"],
  theme: {
    extend: {
      minHeight: {
        "100svh": "90svh", // This sets a custom min-height with 100 small viewport height
      },
      fontSize: {
        "h1-desktop": ["72px", { lineHeight: "120%" }],
        "h1-mobile": ["36px", { lineHeight: "120%" }],
        "h2-desktop": ["50px", { lineHeight: "120%" }],
        "h2-mobile": ["26px", { lineHeight: "120%" }],
        "h3-desktop": ["28px", { lineHeight: "120%" }],
        "h3-mobile": ["20px", { lineHeight: "120%" }],
        body1: ["16px", { lineHeight: "160%" }, { paragraphSpacing: "8px" }],
        body2: ["16px"],
        body3: ["14px", { lineHeight: "160%" }, { paragraphSpacing: "8px" }],
      },
      fontWeight: {
        regular: "400",
        bold: "700",
      },
      fontFamily: {
        armarante: ["Amarante", "serif"],
        rethink: ["Rethink Sans", "sans-serif"],
      },
      backgroundImage: {
        bannerImg: "url('/static/assets/banner.png')",
        bannerImgMobile: "url('/static/assets/banner-mobile.png')",
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
