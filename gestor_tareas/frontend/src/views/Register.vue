<template>
  <div>
    <h2>Registro</h2>
    <input v-model="username" placeholder="Nombre de usuario" />
    <input v-model="email" placeholder="Correo electrónico" />
    <input v-model="password" type="password" placeholder="Contraseña" />
    <button @click="handleRegister">Registrarse</button>
  </div>
</template>

<script>
import { register } from "@/services/authService";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: ""
    };
  },
  methods: {
    async handleRegister() {
      const success = await register(this.username, this.email, this.password);
      if (success) {
        this.$router.push("/login");
      }
    }
  }
};
</script>
