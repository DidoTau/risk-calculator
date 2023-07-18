<template>
  <div class="sidebar pt-2 px-3">
    <div class="current-prediction">
      <div class="title mb-4">
        <h3>Efectividad de tratamiento neoadyuvante</h3>
      </div>
      <div v-if="tSchemePercentage && tpSchemePercentage" class="mx-auto">
        <h5 class="text-center">
          <strong> {{ name }}, {{ age }} años</strong>
        </h5>
        <ul>
          <li class="my-2">
            <strong>{{ tSchemePercentage }}% ({{ tSchemeLabel }})</strong> con
            esquema
            <strong>Trastuzumab</strong>
          </li>
          <li>
            <strong>{{ tpSchemePercentage }}% ({{ tpSchemeLabel }})</strong> con
            esquema
            <strong>Trastuzumab y Pertuzumab</strong>
          </li>
        </ul>
      </div>
      <div v-else class="text-center mx-auto">
        No has hecho ninguna predicción
      </div>
    </div>
    <div class="last-predictions py-2">
      <div class="title">
        <h3>Últimas predicciones</h3>
      </div>
      <div class="row">
        <div class="col text-table text-center">Fecha</div>
        <div class="col text-table text-center">Nombre</div>
        <div class="col text-table text-center">T</div>
        <div class="col text-table text-center">TP</div>
      </div>
      <div v-for="request in requests" :key="request.id" class="row">
        <div class="col text-center">{{ request.date }}</div>
        <div class="col text-center">{{ request.input_data.nombre }}</div>
        <div class="col text-center">
          {{ Math.round(request.response_data.t_scheme.prob * 100) }} %
        </div>
        <div class="col text-center">
          {{ Math.round(request.response_data.tp_scheme.prob * 100) }} %
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import apiService from "@/services/apiService";
export default {
  // define the name of the component
  name: "SideBar",
  // define the data of the component in vue 3
  data() {
    return {
      requests: [],
    };
  },
  mounted() {
    this.getRequests();
  },
  computed: {
    isResultsEmpty() {
      return Object.keys(this.$store.state.results).length === 0;
    },
    tSchemePercentage() {
      return !this.isResultsEmpty
        ? Math.round(this.$store.state.results["t_scheme"].prob * 100)
        : "";
    },
    tSchemeLabel() {
      return !this.isResultsEmpty
        ? this.$store.state.results["t_scheme"].label
        : "";
    },
    tpSchemePercentage() {
      return !this.isResultsEmpty
        ? Math.round(this.$store.state.results["tp_scheme"].prob * 100)
        : "";
    },
    tpSchemeLabel() {
      return !this.isResultsEmpty
        ? this.$store.state.results["tp_scheme"].label
        : "";
    },
    name() {
      return !this.isResultsEmpty
        ? this.$store.state.results["name"].trim()
        : "";
    },
    age() {
      return !this.isResultsEmpty ? this.$store.state.results["age"] : "";
    },
  },
  watch: {
    isResultsEmpty: {
      handler: function () {
        this.getRequests();
      },
      deep: true,
    },
  },
  methods: {
    getRequests() {
      apiService.getRequests().then((data) => {
        this.requests = data;
      });
    },
  },
};
</script>
<style scoped>
.sidebar {
  width: 35vw;
  position: fixed;
  bottom: 0;
  right: 0;
  height: 100vh;
  border-left: 1px solid #ebebeb;
}
.title {
  text-align: center;
  color: #004e91;
}

.current-prediction {
  height: 50%;
  border-bottom: 1px solid #ebebeb;
}
.last-predictions {
  height: 50%;
}
.text-table {
  color: #004e91;
}
</style>
