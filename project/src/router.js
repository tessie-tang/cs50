import Vue from 'vue'
import Router from 'vue-router'
import IndexPage from "./components/IndexPage.vue";
import SearchPage from "./components/SearchPage.vue";
import MyCove from "./components/MyCove.vue"

Vue.use(Router)

const router = new Router({
    routes: [{
        path: '/',
        component: IndexPage
    }, {
        path: '/search',
        component: SearchPage
    }, {
        path: '/mycove',
        component: MyCove
    }]
})

export default router