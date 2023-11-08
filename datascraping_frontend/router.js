import Vue from 'vue';
import VueRouter from 'vue-router';
import officelist from './src/components/officelist.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: officelist },
];

const router = new VueRouter({
  routes,
});

export default router;
