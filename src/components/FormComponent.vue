<template>
  <div
    class="form-component w-75 d-flex justify-content-center align-items-stretch pt-3"
  >
    <!-- crear formulario con los campos: nombre completo, rut, edad, etapa cancer, grado, receptor de estrogeno, receptor de progesterona, indice ki67, cN, cT -->

    <form action="">
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
            <label for="cancer_stage">Etapa del cancer</label>
            <select
              v-model="form.stage"
              name="cancer_stage"
              id="cancer_stage"
              class="form-control"
            >
              <option value="1">Etapa 1</option>
              <option value="2">Etapa 2</option>
              <option value="3">Etapa 3</option>
              <option value="4">Etapa 4</option>
            </select>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="grade">Grado</label>
            <select
              v-model="form.grade"
              name="grade"
              id="grade"
              class="form-control"
            >
              <option value="1">Grado 1</option>
              <option value="2">Grado 2</option>
              <option value="3">Grado 3</option>
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
              <option value="1">Positivo</option>
              <option value="2">Negativo</option>
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
              <option value="1">Positivo</option>
              <option value="2">Negativo</option>
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
              <option value="1">Positivo</option>
              <option value="2">Negativo</option>
            </select>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col m-2">
          <div class="form-group">
            <label for="cN">cN</label>
            <select v-model="form.cn" name="cN" id="cN" class="form-control">
              <option value="1">0</option>
              <option value="2">1</option>
              <option value="1">2</option>
              <option value="2">3</option>
            </select>
          </div>
        </div>
        <div class="col m-2">
          <div class="form-group">
            <label for="cT">cT</label>
            <select v-model="form.ct" name="cT" id="cT" class="form-control">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="1">3</option>
              <option value="2">4</option>
            </select>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>
<script>
export default {
  name: "FormComponent",

  data() {
    return {
      form: {
        name: "",
        rut: "",
        age: "",
        stage: "",
        grade: "",
        estrogen: "",
        progesterone: "",
        ki67: "",
        cn: "",
        ct: "",
      },
    };
  },
};
</script>
<style scoped>
.form-component {
  width: 80vw;
  height: 90vh;
}
</style>
