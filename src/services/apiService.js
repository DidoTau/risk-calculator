import axios from "axios";
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const api = axios.create({
  baseURL: "http://localhost:8000/api/",
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
  getRequests() {
    return api.get("requests/").then((response) => response.data);
  },
  submitForm(data) {
    return api
      .post("dsgd_classifier/predict/", data)
      .then((response) => response.data);
  },
};
