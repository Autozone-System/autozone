import { defineConfig } from 'vite'
import { djangoVitePlugin } from 'django-vite-plugin'

export default defineConfig({
  plugins: [
    djangoVitePlugin([
      "js/app.js",
      "js/bootstrap.js",
      "css/app.css",
      "scss/app.scss",
    ])
  ],
});