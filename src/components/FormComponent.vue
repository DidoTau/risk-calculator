<template>
  <div
    class="form-component w-75 d-flex justify-content-center align-items-stretch pt-3"
  >
    <!-- crear formulario con los campos: nombre completo, rut, edad, etapa cancer, grado, receptor de estrogeno, receptor de progesterona, indice ki67, cN, cT -->

    <form @submit.prevent="sendForm">
      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="name">Nombre completo</label>
            <input
              v-model="form.name"
              type="text"
              name="name"
              id="name"
              class="form-control"
            />
          </div>
        </div>
        <div class="col m-2">
          <div class="form-group">
            <label for="rut">Rut</label>
            <input
              type="text"
              v-model="form.rut"
              name="rut"
              id="rut"
              class="form-control"
            />
          </div>
        </div>
      </div>
      <!-- agrupar las próximas dos form-group en una row -->
      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="age">Edad</label>
            <input
              type="number"
              v-model="form.age"
              name="age"
              id="age"
              class="form-control"
            />
          </div>
        </div>

        <div class="col m-2">
          <div class="form-group">
            <label for="bmi">IMC</label>
            <input
              type="number"
              v-model="form.bmi"
              name="bmi"
              id="bmi"
              class="form-control"
            />
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="cancer_stage">Etapa del cancer</label>
            <select
              v-model="form.stage"
              name="cancer_stage"
              id="cancer_stage"
              class="form-control"
            >
              <option value="I">Etapa 1</option>
              <option value="II">Etapa 2</option>
              <option value="III">Etapa 3</option>
            </select>
          </div>
        </div>
        <div class="col m-2">
          <div class="form-group">
            <label for="molecular_profile"> Perfil Molecular </label>
            <select
              v-model="form.molecular_profile"
              name="molecular_profile"
              id="molecular_profile"
              class="form-control"
            >
              <option value="Luminal_Her2">Luminal</option>
              <option value="Her2_Puro">Puro</option>
            </select>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="status_menop">Estado menopausia</label>
            <select
              v-model="form.status_menopause"
              name="status_menop"
              id="status_menop"
              class="form-control"
            >
              <option value="PREMENOPAUSICA">PRE MENOPAUSICA</option>
              <option value="MENOPAUSICA">MENOPAUSICA</option>
              <option value="POSTMENOPAUSICA">OST MENOPAUSICA</option>
            </select>
          </div>
        </div>
        <div class="col m-2">
          <div class="form-group">
            <label for="estrogen_receptor">Receptor de estrogeno</label>
            <select
              v-model="form.estrogen"
              name="estrogen_receptor"
              id="estrogen_receptor"
              class="form-control"
            >
              <option :value="100">Positivo</option>
              <option :value="0">Negativo</option>
            </select>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="progesterone_receptor">Receptor de progesterona</label>
            <select
              v-model="form.progesterone"
              name="progesterone_receptor"
              id="progesterone_receptor"
              class="form-control"
            >
              <option :value="100">Positivo</option>
              <option :value="0">Negativo</option>
            </select>
          </div>
        </div>
        <div class="col m-2">
          <div class="form-group">
            <label for="ki67_index">Ki67</label>
            <select
              v-model="form.ki67"
              name="ki67_index"
              id="ki67_index"
              class="form-control"
            >
              <option :value="100">Positivo</option>
              <option :value="0">Negativo</option>
            </select>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="cN">cN</label>
            <select v-model="form.cn" name="cN" id="cN" class="form-control">
              <option value="cN0">0</option>
              <option value="cN1">1</option>
              <option value="cN2">2</option>
              <option value="cN3">3</option>
            </select>
          </div>
        </div>
        <div class="col m-2">
          <div class="form-group">
            <label for="cT">cT</label>
            <select v-model="form.ct" name="cT" id="cT" class="form-control">
              <option value="cT1">1</option>
              <option value="cT2">2</option>
              <option value="cT3">3</option>
              <option value="cT4">4</option>
            </select>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="copies">N° de copias</label>
            <input
              type="number"
              v-model="form.copies"
              name="copies"
              id="copies"
              class="form-control"
            />
          </div>
        </div>
        <div class="col m-2">
          <div class="form-group">
            <label for="relation_cen">Relacion cen </label>
            <input
              type="number"
              v-model="form.relation_cen"
              name="relation_cen"
              id="relation_cen"
              class="form-control"
            />
          </div>
        </div>
      </div>

      <div class="text-center my-3">
        <button type="submit">Enviar</button>
      </div>
    </form>
  </div>
</template>
<script>
import apiService from "@/services/apiService";
export default {
  name: "FormComponent",

  data() {
    return {
      form: {
        name: "",
        rut: "",
        age: "",
        bmi: "",
        stage: "",
        molecular_profile: "",
        status_menopause: "",
        estrogen: "",
        progesterone: "",
        ki67: "",
        cn: "",
        ct: "",
        copies: "",
        relation_cen: "",
      },
    };
  },
  methods: {
    sendForm() {
      let input = {
        rut: this.form.rut,
        nombre: this.form.name,
        edad: this.form.age,
        imc: this.form.bmi,
        ct: this.form.ct,
        cn: this.form.cn,
        ki67: this.form.ki67,
        "n°_de_copias": this.form.copies,
        relacion_her_2_cen: this.form.relation_cen,
        re: this.form.estrogen,
        rp: this.form.progesterone,
        status_menop_al_dg: this.form.status_menopause,
        tipo_histologico: "CDI",
        perfil_molecular: this.form.molecular_profile,
        etapa: this.form.stage,
        axila_en_eco: 0,
      };
      input.esquema = 0;
      apiService.submitForm(input).then((response) => {
        let payload = {
          key: "t_scheme",
          value: response,
        };
        this.$store.dispatch("setResults", payload);
        console.log(response);
      });
      input.esquema = 1;
      apiService.submitForm(input).then((response) => {
        let payload = {
          key: "tp_scheme",
          value: response,
        };
        this.$store.dispatch("setResults", payload);
      });
    },
  },
};
</script>
<style scoped>
.form-component {
  width: 80vw;
  height: 90vh;
}
</style>
