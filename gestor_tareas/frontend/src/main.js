import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App)
  .use(router) // 💡 Aquí conecta Vue con el router
  .mount('#app')
