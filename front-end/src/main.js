import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './routes'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { BootstrapVue, IconsPlugin, TableLitePlugin} from "bootstrap-vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";


Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(TableLitePlugin)
Vue.use(VueAxios, axios)
Vue.use(VueRouter)

Vue.config.productionTip = false
const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes
})

axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
