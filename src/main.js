import { createApp } from "vue";
import App from "./App.vue";
import Vuex from "vuex";
import store from "./store";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
import "popper.js/dist/umd/popper.js";

const app = createApp(App);

app.use(Vuex);
app.use(store);

app.mount("#app");
