import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/",
  headers: {
    "Content-Type": "application/json",
  },
});

// Chat / Apply loan
export const applyLoan = (payload) => API.post("/chat", payload);

export default API;
