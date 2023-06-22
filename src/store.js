import Vuex from "vuex";

const store = new Vuex.Store({
  state: {
    results: { t_scheme: [], tp_scheme: [] },
    last_requests: [],
  },
  mutations: {
    setResults(state, payload) {
      state.results = payload;
    },
    setRequests(state, payload) {
      state.last_requests = payload;
    },
  },
  actions: {
    setResults({ commit }, payload) {
      commit("setResults", payload);
    },
    setRequests({ commit }, payload) {
      commit("setRequests", payload);
    },
  },
});

export default store;
