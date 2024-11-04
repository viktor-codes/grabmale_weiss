/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['**/templates/**/*.html'],
	theme: {
		screens: {
			lg: { max: '1999.99px' },
			md: { max: '991.99px' },
			sm: { max: '767.99px' },
			xs: { max: '479.99px' },
		},
		extend: {
			fontFamily: {
				armarante: ['Amarante', 'serif'],
				rethink: ['Rethink Sans', 'sans-serif'],
			},
			backgroundImage: {
				bannerImg: "url('/static/assets/banner.png')",
			},
			colors: {
				white: '#FFFFFF',
				lightgrey: '#EDEDED',
				mediumgrey: '#E1E1E1',
				darkgrey: '#636363',
				black: '#000000',
				gradient:
					'linear-gradient(90deg, rgba(0, 0, 0, 0.00) 0%, rgba(0, 0, 0, 0.10) 44.88%)',
			},
		},
		container: {
			padding: '7rem',
		},
	},
	plugins: [],
}
