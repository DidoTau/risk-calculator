<template>
  <div :class="{ 'modal-backdrop': showModal }"></div>
  <div
    v-if="showModal"
    class="modal fade show"
    id="modal"
    aria-labelledby="modal"
    aria-modal="true"
    role="dialog"
    style="display: block"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header title d-flex justify-content-center">
          <h3 class=""><strong>Resultados</strong></h3>
        </div>
        <div class="modal-body">
          <div v-if="!isResultsEmpty">
            A partir de las características clínicas e histopatológicas
            entregadas, la paciente {{ name }} tiene:

            <ul class="mt-2">
              <li>
                <strong>{{ tSchemePercentage }}%</strong> de probabilidad de
                tener respuesta al tratamiento neoadyuvante siendo tratada solo
                con <strong>Trastuzumab</strong>.
              </li>
              <li>
                <strong>{{ tpSchemePercentage }}%</strong> de probabilidad de
                tener respuesta al tratamiento neoadyuvante siendo tratada con
                <strong>Trastuzumab y Pertuzumab</strong>.
              </li>
            </ul>
          </div>
          <div v-else class="text-center">
            <div class="spinner-border text-info"></div>
          </div>
        </div>

        <div class="modal-footer d-flex justify-content-center">
          <button class="custom-button" @click="$emit('close-modal')">
            Cerrar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "ResultsPatientModal",
  emits: ["close-modal"],
  props: {
    visible: {
      type: Boolean,
      default: false,
    },
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

    tpSchemePercentage() {
      return !this.isResultsEmpty
        ? Math.round(this.$store.state.results["tp_scheme"].prob * 100)
        : "";
    },

    name() {
      return !this.isResultsEmpty
        ? this.$store.state.results["name"]?.replace(/\s/g, "")
        : "";
    },
  },
  data() {
    return {
      showModal: false,
    };
  },
  watch: {
    visible(newVal) {
      this.showModal = newVal;
    },
  },
};
</script>
<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(
    0,
    0,
    0,
    0.5
  ); /* Ajusta la opacidad según tus preferencias */
  backdrop-filter: blur(
    5px
  ); /* Ajusta el valor de blur según tus preferencias */
  z-index: 999; /* Asegúrate de que la capa de fondo esté por encima de otros elementos */
}

.modal {
  /* Estilos para el modal */
  z-index: 1000; /* Asegúrate de que el modal esté por encima de la capa de fondo */
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}
.modal-dialog {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}
.custom-button {
  background-color: #004e91;
  border: 1px solid #004e91;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1.2rem;
  font-weight: 600;
  color: #ffffff;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}
.title {
  color: #004e91;
}
</style>
