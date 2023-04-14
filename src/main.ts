import { createApp, h } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'


import router from './router'

const app = createApp({
    render: () => h(App)
});

app.use(router)
app.use(VueAxios, axios)

app.mount('#app')