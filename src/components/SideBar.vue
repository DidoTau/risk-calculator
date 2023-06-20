<template>
  <div class="sidebar">
    <div class="title">
      <h3>Efectividad de tratamiento neoadyuvante</h3>
    </div>
    <div>
      <p>Trastuzumab:</p>
      <p>{{ tSchemePercentage }} %</p>
      <p>{{ tSchemeLabel }}</p>
    </div>

    <div>
      <p>Trastuzumab y Pertuzumab:</p>
      <p>{{ tpSchemePercentage }} %</p>
      <p>{{ tpSchemeLabel }}</p>
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
      results: {},
      requests: [],
    };
  },
  mounted() {
    apiService.getRequests().then((data) => {
      this.requests = data;
    });
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
  },
};
</script>
<style scoped>
.sidebar {
  width: 20vw;
  position: fixed;
  bottom: 0;
  right: 0;
  height: 90vh;
}
.title {
  text-align: center;
}
</style>
