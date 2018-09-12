
import Vue from 'vue/dist/vue.js';
import App2 from './App2'
import ToggleButton from 'vue-js-toggle-button'

// ~~~~~~~~ TESTVUEJS ~~~~~~~~~~ //

// new Vue({
//     el: '#app',
//     render: h => h(App),
// });

// ~~~~~~~~ SWITCHES ~~~~~~~~~~ //

Vue.use(ToggleButton)
new Vue({
    el: '#app-3',
    render: h => h(App2),
})
