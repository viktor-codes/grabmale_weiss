/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/templates/**/*.html"],
  theme: {
    screens: {
      lg: { max: "1999.99px" },
      md: { max: "991.99px" },
      sm: { max: "767.99px" },
      xs: { max: "479.99px" },
    },
    extend: {
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
      },
      colors: {
        white: "#FFFFFF",
        lightgrey: "#EDEDED",
        mediumgrey: "#E1E1E1",
        darkgrey: "#636363",
        black: "#000000",
        gradient:
          "linear-gradient(90deg, rgba(0, 0, 0, 0.00) 0%, rgba(0, 0, 0, 0.10) 44.88%)",
      },
    },
    container: {
      padding: "7rem",
    },
  },
  plugins: [],
};
