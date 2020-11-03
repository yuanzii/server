import Vue from "vue";
import Vuex from "vuex";
import print from "./print";
import orders from "./orders";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    print,
    orders,
  },
  // state: {},
  // mutations: {},
  // getters:{},
  // actions: {},
  // modules: {}
});

