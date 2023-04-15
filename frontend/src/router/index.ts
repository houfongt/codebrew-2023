import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import Home from "../views/Home.vue"
import Capture from '../views/Capture.vue'
import RecipeResult from '../views/RecipeResult.vue'
import Intro from '../views/Intro.vue'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/', name: 'Home', component: Home
    },
    {
        path: '/Capture', name: 'Capture' , component: Capture
    },
    {
        path: '/Result', name: 'Result', component: RecipeResult
    },
    {
        path: '/Welcome', name: 'Intro', component: Intro
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router