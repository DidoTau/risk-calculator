<template>
  <div class="sidebar">
    <div class="title">
      <h3>Efectividad de tratamiento neoadyuvante</h3>
    </div>
    <div>
      <p>Trastuzumab : {{ tSchemePercentage }}</p>
    </div>

    <div>
      <p>Trastuzumab y Pertuzumab :{{ tpSchemePercentage }}</p>
    </div>
  </div>
</template>
<script>
export default {
  // define the name of the component
  name: "SideBar",
  // define the data of the component in vue 3
  data() {
    return {
      results: {},
    };
  },

  computed: {
    isResultsEmpty() {
      return Object.keys(this.results).length === 0;
    },
    tSchemePercentage() {
      return !this.isResultsEmpty ? this.results["t_scheme"].percent : "";
    },
    tpSchemePercentage() {
      return !this.isResultsEmpty ? this.results["tp_scheme"].percent : "";
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
