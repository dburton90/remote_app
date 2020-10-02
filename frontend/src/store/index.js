import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';

// import example from './module-example'

const CURRENT_KEY = 'vuex';

Vue.use(Vuex);
const vuexPersist = new VuexPersistence({
  strictMode: process.env.DEV,
  storage: window.localStorage,
  key: CURRENT_KEY,
});

Vue.use(Vuex);

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      // example
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    mutations: {
      RESTORE_MUTATION: vuexPersist.RESTORE_MUTATION,
    },
    plugins: [vuexPersist.plugin],

    strict: process.env.DEV,
  });

  return Store;
}
