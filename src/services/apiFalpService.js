import axios from "axios";
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const api = axios.create({
  baseURL: "http://srvcodautoqa.falp.org:3000",
  timeout: 500000,
  headers: {
    "Content-Type": "application/json",
    Authorization: {
      toString() {
        return `Token ${localStorage.getItem("token")}`;
      },
    },
  },
});

export default {
  getMetadata() {
    return api.post("metadata/").then((response) => response.data);
  },
  getPatientData(rut) {
    return new Promise((resolve, reject) => {
      let body = {
        id: rut,
        fields: [
          { field: "PACIENTE" },
          { field: "FECHA_NACIMIENTO" },
          { field: "FECHA_INGRESO" },
          { field: "INT_mama_histologia" },
          { field: "INT_mama_receptorEstrogeno" },
          { field: "INT_mama_receptorProgesterona" },
          { field: "INT_mama_ki67" },
          { field: "INT_mama_fechaDgHistologico" },
          { field: "INT_mama_lateralidad" },
          { field: "INFORME_COMITE" },
          { field: "INT_mama_examenFisico" },
        ],
      };
      api
        .post("data/", body)
        .then((response) => {
          let clean_fields = [];
          let fields = response.data;
          console.log(fields);
          // delete duplicates and use the most recent register of the field
          const sortedData = fields.sort(
            (a, b) => (b.timestamp || 0) - (a.timestamp || 0)
          );
          const uniqueData = [
            ...sortedData
              .reduce((map, item) => {
                if (
                  !map.has(item.field) ||
                  (item.timestamp || 0) > (map.get(item.field).timestamp || 0)
                ) {
                  map.set(item.field, item);
                }
                return map;
              }, new Map())
              .values(),
          ];

          uniqueData.forEach((f) => {
            switch (f.field) {
              case "FECHA_NACIMIENTO": {
                const birthday = new Date(f.value);
                const actualday = new Date();
                clean_fields.push({
                  field: "Edad",
                  value: Math.floor(
                    (actualday - birthday) / (1000 * 60 * 60 * 24 * 365.25)
                  ),
                });
                break;
              }
              case "PACIENTE":
                clean_fields.push({
                  field: "Nombre",
                  value: f.value,
                });
                break;
              case "INFORME_COMITE":
                clean_fields.push({
                  field: "Informe del comité",
                  value: f.value,
                });
                break;
              case "INT_mama_examenFisico":
                clean_fields.push({ field: "Examen físico", value: f.value });
                break;
              case "INT_mama_histologia":
                clean_fields.push({
                  field: "Tipo histológico",
                  value: f.value,
                });
                break;
              case "INT_mama_receptorEstrogeno":
                clean_fields.push({
                  field: "Receptor de estrógeno",
                  value: f.value == 1 ? "POSITIVO" : "NEGATIVO",
                });
                break;
              case "INT_mama_receptorProgesterona":
                clean_fields.push({
                  field: "Receptor de progesterona",
                  value: f.value == 1 ? "POSITIVO" : "NEGATIVO",
                });
                break;
              case "INT_mama_ki67":
                clean_fields.push({
                  field: "Ki67",
                  value: f.value == 1 ? "POSITIVO" : "NEGATIVO",
                });
                break;
              case "INT_mama_fechaDgHistologico":
                clean_fields.push({
                  field: "Fecha de diagnóstico",
                  value: f.value,
                });
                break;
              case "INT_mama_lateralidad":
                clean_fields.push({
                  field: "Laterialidad",
                  value: f.value,
                });
                break;
            }
          });

          resolve(clean_fields);
        })
        .catch((error) => {
          reject(error);
        });
    });
  },
};
