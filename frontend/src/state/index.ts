import { createStore, Store } from 'vuex'
import VuexPersistence from 'vuex-persist'

export interface State {
    introPageShown: boolean
}

const vuexLocal = new VuexPersistence<State>({
    storage: window.localStorage
})

const store = createStore({
    state: {
        introPageShown: false
    },
    mutations : {
        setIntroPageStatus(state, payload) {
            state.introPageShown = payload
            console.log('Thanks for completing the Intro Page!');
        },
    },
    plugins: [vuexLocal.plugin]
})

export default store