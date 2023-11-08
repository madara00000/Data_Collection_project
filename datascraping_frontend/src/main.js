import Vue from 'vue'
import App from './App.vue'
import router from '../router'
import 'bootstrap/dist/css/bootstrap.css';


new Vue({
  render: (h) => h(App),  //Specifies that the main component of the app is App.
  router,                 // Use the router
}).$mount('#app');        //Attaches the Vue app to an HTML element with the ID app