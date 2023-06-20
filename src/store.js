import Vuex from "vuex";

const store = new Vuex.Store({
  state: {
    results: { t_scheme: [], tp_scheme: [] },
  },
  mutations: {
    setResults(state, payload) {
      console.log(payload);
      state.results[payload.key] = payload.value;
      console.log(state.results);
    },
  },
  actions: {
    setResults({ commit }, payload) {
      console.log(payload);
      commit("setResults", payload);
    },
  },
});

export default store;
