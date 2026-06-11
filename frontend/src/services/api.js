import axios from "axios";

export const AUTH_API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/auth",
});

export const USER_API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/users",
});

export default USER_API;