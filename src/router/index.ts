import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import Home from "../views/Home.vue"
import Capture from '../views/Capture.vue'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/', name: 'Home', component: Home
    },
    {
        path: '/Capture', name: 'Capture' , component: Capture
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router