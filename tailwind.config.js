/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: ['./src/**/*.{html, js, jsx}', './src/static/tw/*.css'],
  safelist: ['collapse', 'btn'],
  theme: {
    extend: {},
  },
  plugins: [
    // require('@tailwindcss/forms'),
  ],
}
