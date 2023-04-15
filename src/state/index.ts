import { createStore } from 'vuex'

const store = createStore({
    state: {
        introPageShown: false
    },
    mutations : {
        setIntroPageStatus(state, payload) {
            state.introPageShown = payload
            
            console.log('Thanks for completing the Intro Page!');
        },
    }
    
})

export default store