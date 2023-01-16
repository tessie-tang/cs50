import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

import ideas from './ideas'

const store = new Vuex.Store({
    state: {
        control: {
            composer: false,
            project: false,
            login: false,
            register: false,
            search: false,
            index: true
        },
        ideas: ideas,
        query: '',
        currentViewingProject: {}
    }
})

export default store