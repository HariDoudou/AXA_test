import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import tsconfigPaths from 'vite-tsconfig-paths'
import tailwindcss from '@tailwindcss/vite'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    tsconfigPaths(),
    tailwindcss(),
    ui({ colorMode: false, ui: { colors: { primary: 'blue-axa' } } }),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
})
