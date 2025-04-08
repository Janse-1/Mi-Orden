import axios from "axios";

export async function login(username, password) {
    try {
        const response = await axios.post("http://127.0.0.1:8000/api/token/", {
            username,
            password
        });

        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);

        console.log("Login exitoso");
        return true;
    } catch (error) {
        console.error("Error en login", error.response.data);
        return false;
    }
}


export async function register(username, email, password) {
    try {
        await axios.post("http://127.0.0.1:8000/api/register/", {
            username,
            email,
            password
        });
        console.log("Registro exitoso");
        return true;
    } catch (error) {
        console.error("Error en el registro", error.response.data);
        return false;
    }
}
