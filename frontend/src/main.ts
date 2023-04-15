import { createApp, h } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

import store from './state/index'
import router from './router'

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyB88uOHA-wtzmaaCIe5dZLfm9d8C8ZANvs",
    authDomain: "quahk-apis.firebaseapp.com",
    databaseURL: "https://quahk-apis.firebaseio.com",
    projectId: "quahk-apis",
    storageBucket: "quahk-apis.appspot.com",
    messagingSenderId: "982952632526",
    appId: "1:982952632526:web:9db8cab3c32739b877709f",
    measurementId: "G-938Q1G9ZHZ"
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);
const analytics = getAnalytics(firebaseApp);

const app = createApp({
    render: () => h(App)
});

app.use(router)
app.use(VueAxios, axios)
app.use(store)

app.mount('#app')