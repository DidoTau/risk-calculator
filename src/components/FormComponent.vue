<template>
  <div
    class="form-component w-75 d-flex justify-content-center align-items-stretch pt-3"
  >
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
              v-model="v$.form.rut.$model"
              name="rut"
              id="rut"
              class="form-control"
              @change="validateRut(form.rut)"
            />
            <div
              class="input-errors"
              v-for="(error, index) of v$.form.rut.$errors"
              :key="index"
            >
              <div class="error-msg">{{ error.$message }}</div>
            </div>
          </div>
        </div>

        <div class="col m-2">
          <div class="form-group">
            <label for="age">Edad</label>
            <input
              type="number"
              v-model="v$.form.age.$model"
              name="age"
              id="age"
              class="form-control"
            />
            <div
              class="input-errors"
              v-for="(error, index) of v$.form.age.$errors"
              :key="index"
            >
              <div class="error-msg">{{ error.$message }}</div>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
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
      </div>

      <div class="row">
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

        <div class="col m-2">
          <div class="form-group">
            <label for="histological_type">Tipo Histológico</label>

            <select
              v-model="form.histological_type"
              name="histological_type"
              id="histological_type"
              class="form-control"
            >
              <option value="CDI">CDI</option>
              <option value="CLI">CLI</option>
            </select>
          </div>
        </div>
      </div>
      <div class="text-center py-2">
        <button
          class="custom-button"
          type="submit"
          :disabled="v$.form.$invalid"
        >
          Calcular
        </button>
      </div>
    </form>
  </div>
</template>
<script>
import useVuelidate from "@vuelidate/core";
import { required, minLength } from "@vuelidate/validators";
import apiService from "@/services/apiService";
export default {
  name: "FormComponent",

  data() {
    return {
      v$: useVuelidate(),
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
        histological_type: "",
      },
    };
  },
  computed: {
    rutIsValid() {
      return this.validateRut(this.form.rut);
    },
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
        tipo_histologico: this.form.histological_type,
        perfil_molecular: this.form.molecular_profile,
        etapa: this.form.stage,
        axila_en_eco: 0,
      };

      apiService.submitForm(input).then((response) => {
        this.$store.dispatch("setResults", response);
      });
    },
    validateRut(rut) {
      rut = rut.replace(/[^0-9kK]+/g, "");
      let body = rut.slice(0, -1);
      let dv = rut.slice(-1).toUpperCase();
      if (!rut || rut.length < 7) {
        return false;
      }
      let sum = 0;
      let multiple = 2;
      for (let i = 1; i <= body.length; i++) {
        let index = multiple * body.charAt(body.length - i);

        sum += index;
        if (multiple < 7) {
          multiple += 1;
        } else {
          multiple = 2;
        }
      }
      let dvExpected = 11 - (sum % 11);
      dv = dv === "K" ? 10 : dv;
      dv = dv === 0 ? 11 : dv;

      return dvExpected.toString() === dv.toString();
    },
    validateAge(age) {
      return age > 0 && age < 100;
    },
    validateBMI(bmi) {
      return bmi > 0 && bmi < 100;
    },
  },
  validations() {
    return {
      form: {
        name: {
          required,
          minLength: minLength(3),
        },
        rut: {
          required,
          minLength: minLength(7),
          rut_validation: {
            $validator: this.validateRut,
            $message: "Rut inválido",
          },
        },
        age: {
          required,
          age_validation: {
            $validator: this.validateAge,
            $message: "Edad inválida",
          },
        },
        bmi: {
          bmi_validation: {
            $validator: this.validateBMI,
            $message: "IMC inválido",
          },
        },
        stage: {
          required,
        },
        molecular_profile: {
          required,
        },
        status_menopause: {
          required,
        },
        estrogen: {
          required,
        },
        progesterone: {
          required,
        },
        ki67: {
          required,
        },
        cn: {
          required,
        },
        ct: {
          required,
        },
        copies: {
          required,
        },
        relation_cen: {
          required,
        },
        histological_type: {
          required,
        },
      },
    };
  },
};
</script>
<style scoped>
.form-component {
  width: 70vw;
  height: 88vh;
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
</style>
