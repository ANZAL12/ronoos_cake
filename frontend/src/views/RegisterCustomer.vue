<template>
  <div class="register-wrapper">
    <div class="background-shapes">
      <div class="cake-float cake-1">🎂</div>
      <div class="cake-float cake-2">🧁</div>
      <div class="cake-float cake-3">🍰</div>
      <div class="cake-float cake-4">🎂</div>
      <div class="cake-float cake-5">🧁</div>
      <div class="cake-float cake-6">🍰</div>
      <div class="cake-float cake-7">🎂</div>
      <div class="cake-float cake-8">🧁</div>
    </div>
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
        <div class="input-group">
          <label for="mobile_number">Mobile Number</label>
          <input v-model="mobile_number" id="mobile_number" type="text" required />
        </div>
        <button type="submit" :disabled="loading">Register</button>
        <div v-if="error" class="error">{{ error }}</div>
        <div v-if="success" class="success">Registration successful! You can now log in.</div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'

const username = ref('')
const email = ref('')
const first_name = ref('')
const last_name = ref('')
const password = ref('')
const mobile_number = ref('')
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
      mobile_number: mobile_number.value,
      is_customer: true
    })
    success.value = true
    username.value = ''
    email.value = ''
    first_name.value = ''
    last_name.value = ''
    password.value = ''
    mobile_number.value = ''
  } catch (err) {
    const data = err.response?.data
    if (data?.email && data.email[0].toLowerCase().includes('exist')) {
      Swal.fire({
        icon: 'error',
        title: 'Email Already Registered',
        text: 'This email is already registered. Please use a different email.',
      })
    } else if (data?.username && data.username[0].toLowerCase().includes('exist')) {
      Swal.fire({
        icon: 'error',
        title: 'Username Taken',
        text: 'This username is already taken. Please choose another username.',
      })
    } else {
      error.value = data?.detail || 'Registration failed. Please check your details.'
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
  overflow: hidden;
}
.background-shapes {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
}
.cake-float {
  position: absolute;
  font-size: 2rem;
  animation: cakeFloat 8s ease-in-out infinite;
  opacity: 0.7;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}
.cake-1 { top: 15%; left: 10%; animation-delay: 0s; animation-duration: 7s; }
.cake-2 { top: 25%; right: 15%; animation-delay: 1s; animation-duration: 9s; }
.cake-3 { bottom: 30%; left: 8%; animation-delay: 2s; animation-duration: 8s; }
.cake-4 { top: 60%; right: 8%; animation-delay: 3s; animation-duration: 6s; }
.cake-5 { bottom: 15%; left: 60%; animation-delay: 4s; animation-duration: 10s; }
.cake-6 { top: 40%; left: 5%; animation-delay: 2.5s; animation-duration: 7.5s; }
.cake-7 { bottom: 45%; right: 20%; animation-delay: 1.5s; animation-duration: 8.5s; }
.cake-8 { top: 80%; left: 25%; animation-delay: 3.5s; animation-duration: 9.5s; }
@keyframes cakeFloat {
  0% { transform: translate(0px, 0px); }
  25% { transform: translate(15px, -20px); }
  50% { transform: translate(-10px, -35px); }
  75% { transform: translate(20px, -15px); }
  100% { transform: translate(0px, 0px); }
}
.register-container {
  width: 100%;
  max-width: 400px;
  box-sizing: border-box;
  margin: 40px auto;
  margin-top: -20px;
  padding: 1.5rem 3rem 1.5rem 2rem;
  border-radius: 14px;
  background-color: #f9fafb;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  border: 1px solid #ececec;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  z-index: 1;
}
h2 {
  text-align: center;
  color: #1f2937;
  margin-bottom: 1.1rem;
  font-size: 1.3rem;
}
.input-group {
  margin-bottom: 0.8rem;
}
.input-group input {
  width: 96%;
  margin: 0 auto;
  display: block;
}
.input-group:last-of-type {
  margin-bottom: 1.2rem;
}
label {
  display: block;
  margin-bottom: 0.4rem;
  font-weight: 600;
  color: #374151;
  font-size: 0.95rem;
}
input {
  width: 100%;
  padding: 0.65rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  outline: none;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  font-size: 1rem;
  background-color: #fff;
}
input:focus {
  border-color: #f37022;
  box-shadow: 0 0 0 3px rgba(243, 112, 34, 0.2);
}
button {
  width: 100%;
  padding: 0.8rem;
  background-color: #f37022;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-top: 1rem;
}
button:hover:not(:disabled) {
  background-color: #e0631c;
}
button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
.error,
.success {
  margin-top: 1rem;
  text-align: center;
  font-weight: 500;
  padding: 0.7rem;
  border-radius: 6px;
}
.error {
  background-color: #fee2e2;
  color: #dc2626;
}
.success {
  background-color: #dcfce7;
  color: #16a34a;
}
</style>