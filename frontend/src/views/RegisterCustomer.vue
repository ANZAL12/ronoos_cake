<template>
  <div class="register-container">
    <h2>Register as Customer</h2>
    <form @submit.prevent="register">
      <div class="input-group">
        <label for="username">Username</label>
        <input v-model="username" id="username" type="text" required />
      </div>
      <div class="input-group">
        <label for="email">Email</label>
        <input v-model="email" id="email" type="email" required />
      </div>
      <div class="input-group">
        <label for="first_name">First Name</label>
        <input v-model="first_name" id="first_name" type="text" required />
      </div>
      <div class="input-group">
        <label for="last_name">Last Name</label>
        <input v-model="last_name" id="last_name" type="text" required />
      </div>
      <div class="input-group">
        <label for="password">Password</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <button type="submit" :disabled="loading">Register</button>
      <div v-if="error" class="error">{{ error }}</div>
      <div v-if="success" class="success">Registration successful! You can now log in.</div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const email = ref('')
const first_name = ref('')
const last_name = ref('')
const password = ref('')
const error = ref('')
const success = ref(false)
const loading = ref(false)

const register = async () => {
  error.value = ''
  success.value = false
  loading.value = true
  try {
    await axios.post('http://localhost:8000/api/v1/users/', {
      username: username.value,
      email: email.value,
      first_name: first_name.value,
      last_name: last_name.value,
      password: password.value,
      is_customer: true
    })
    success.value = true
    username.value = ''
    email.value = ''
    first_name.value = ''
    last_name.value = ''
    password.value = ''
  } catch (err) {
    error.value = err.response?.data?.detail || 'Registration failed. Please check your details.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 2rem;
  border: 1px solid #eee;
  border-radius: 8px;
  background: #fff;
}
.input-group {
  margin-bottom: 1.2rem;
}
label {
  display: block;
  margin-bottom: 0.3rem;
  font-weight: 600;
}
input {
  width: 100%;
  padding: 0.7rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}
button {
  width: 100%;
  padding: 0.8rem;
  background-color: #f37022;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
}
button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
.error {
  color: #c53030;
  margin-top: 1rem;
}
.success {
  color: #38a169;
  margin-top: 1rem;
}
</style> 