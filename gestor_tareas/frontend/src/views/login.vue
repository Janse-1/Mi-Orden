<template>
  <div>
    <input v-model="username" placeholder="Usuario" />
    <input v-model="password" type="password" placeholder="Contraseña" />
    <button @click="handleLogin">Iniciar sesión</button>
  </div>
</template>

<script>
import { login } from "@/services/authService";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async handleLogin() {
      const success = await login(this.username, this.password);
      if (success) {
        this.$router.push("/dashboard"); // o donde quieras redirigir
      }
    },
  },
};
</script>
