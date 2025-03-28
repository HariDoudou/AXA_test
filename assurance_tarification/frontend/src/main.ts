import './assets/main.css'
import ui from '@nuxt/ui/vue-plugin'
import { createApp } from 'vue'
import { VueQueryPlugin } from '@tanstack/vue-query'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(VueQueryPlugin)
app.use(createPinia())
app.use(router)
app.use(ui)

app.mount('#app')
