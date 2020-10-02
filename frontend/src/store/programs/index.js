import Vue from 'vue';
import { socket } from '../../boot/socket';

const defaultState = () => ({
  programs: {},
  defaultKeys: {},
  current: null,
});

export default {
  namespaced: true,
  state: defaultState(),
  actions: {
    load({ commit }) {
      Vue.prototype.$axios.get('/os-handler/programs')
        .then((resp) => {
          commit('setPrograms', resp.data);
        });
      Vue.prototype.$axios.get('/os-handler/default-keys')
        .then((resp) => {
          commit('setDefaultKeys', resp.data);
        });
    },
    programFocus({ commit }, program) {
      socket.emit('program', { action: 'focus', name: program.name });
      commit('setProgram', program.name);
    },
  },
  mutations: {
    setPrograms(s, data) {
      Vue.set(s, 'programs', data.programs);
    },
    setDefaultKeys(s, data) {
      Vue.set(s, 'defaultKeys', data.defaultKeys);
    },
    setProgram(s, program) {
      s.current = program;
    },
  },
  getters: {
    currentProgram: (s) => s.programs[s.current],
    currentKeys: (s, getter) => (getter.currentProgram || {}).keys || [],
    defaultKeys: (s) => s.defaultKeys || [],
  },
};
