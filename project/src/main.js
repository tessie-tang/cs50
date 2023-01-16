import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import store from './store'
import Icon from "ant-design-vue/lib/icon";
var VueScrollTo = require('vue-scrollto');
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.less';

Vue.component('icon', Icon)
Vue.use(VueAxios, axios)
Vue.use(Antd);
Vue.use(VueScrollTo)

// You can also pass in the default options
Vue.use(VueScrollTo, {
  container: "body",
  duration: 500,
  easing: "ease",
  offset: 0,
  force: true,
  cancelable: true,
  onStart: false,
  onDone: false,
  onCancel: false,
  x: false,
  y: true
})
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')