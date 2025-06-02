<template>
    <div class="login-wrapper">
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
      
      <div class="login-container">
        <div class="login-header">
          <div class="logo-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2C13.1046 2 14 2.89543 14 4V6H10V4C10 2.89543 10.8954 2 12 2Z" fill="currentColor"/>
              <path d="M8 6V4C8 1.79086 9.79086 0 12 0C14.2091 0 16 1.79086 16 4V6H18C19.1046 6 20 6.89543 20 8V20C20 21.1046 19.1046 22 18 22H6C4.89543 22 4 21.1046 4 20V8C4 6.89543 4.89543 6 6 6H8ZM12 14C13.1046 14 14 13.1046 14 12C14 10.8954 13.1046 10 12 10C10.8954 10 10 10.8954 10 12C10 13.1046 10.8954 14 12 14Z" fill="currentColor"/>
              <circle cx="12" cy="16" r="1" fill="white"/>
              <path d="M10 18H14C14.5523 18 15 18.4477 15 19C15 19.5523 14.5523 20 14 20H10C9.44772 20 9 19.5523 9 19C9 18.4477 9.44772 18 10 18Z" fill="white"/>
            </svg>
          </div>
          <h2>Sweet Login</h2>
          <p>Welcome to CakeWorld</p>
        </div>
  
        <form @submit.prevent="login" class="login-form">
          <div class="input-group">
            <label for="username">Username</label>
            <div class="input-wrapper">
              <svg class="input-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20 21V19C20 17.9391 19.5786 16.9217 18.8284 16.1716C18.0783 15.4214 17.0609 15 16 15H8C6.93913 15 5.92172 15.4214 5.17157 16.1716C4.42143 16.9217 4 17.9391 4 19V21" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <input 
                v-model="username" 
                id="username" 
                type="text" 
                required 
                placeholder="Enter your username"
                :class="{ 'error': error }"
              />
            </div>
          </div>
  
          <div class="input-group">
            <label for="password">Password</label>
            <div class="input-wrapper">
              <svg class="input-icon" viewBox="0 0 24 24" fill="none">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2" stroke="currentColor" stroke-width="2"/>
                <circle cx="12" cy="16" r="1" stroke="currentColor" stroke-width="2"/>
                <path d="M7 11V7C7 5.67392 7.52678 4.40215 8.46447 3.46447C9.40215 2.52678 10.6739 2 12 2C13.3261 2 14.5979 2.52678 15.5355 3.46447C16.4732 4.40215 17 5.67392 17 7V11" stroke="currentColor" stroke-width="2"/>
              </svg>
              <input 
                v-model="password" 
                :type="showPassword ? 'text' : 'password'" 
                id="password" 
                required 
                placeholder="Enter your password"
                :class="{ 'error': error }"
              />
              <span class="toggle-password" @click="showPassword = !showPassword">
                <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24">
                  <path stroke="#a0aec0" stroke-width="2" d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7S1 12 1 12Z"/>
                  <circle stroke="#a0aec0" stroke-width="2" cx="12" cy="12" r="3"/>
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24">
                  <path stroke="#a0aec0" stroke-width="2" d="M17.94 17.94C16.12 19.25 14.13 20 12 20c-7 0-11-8-11-8a21.77 21.77 0 0 1 5.06-6.06M9.53 9.53A3 3 0 0 1 12 9c1.66 0 3 1.34 3 3 0 .47-.11.91-.29 1.29M1 1l22 22"/>
                </svg>
              </span>
            </div>
          </div>
  
          <div class="input-group">
            <label for="role">Role</label>
            <div class="input-wrapper">
              <svg class="input-icon" viewBox="0 0 24 24" fill="none">
                <path d="M7 10l5 5 5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <select v-model="role" id="role" required class="styled-select">
              <option value="baker">Baker</option>
              <option value="customer">Customer</option>
                <option value="staff">Admin</option>
            </select>
            </div>
          </div>
  
          <button type="submit" :disabled="loading" class="login-button">
            <span v-if="!loading">Sign In</span>
            <div v-else class="loading-spinner">
              <div class="spinner"></div>
              <span>Signing in...</span>
            </div>
          </button>
  
          <div v-if="error" class="error-message">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
              <line x1="15" y1="9" x2="9" y2="15" stroke="currentColor" stroke-width="2"/>
              <line x1="9" y1="9" x2="15" y2="15" stroke="currentColor" stroke-width="2"/>
            </svg>
            {{ error }}
          </div>
        </form>
  
        <div class="login-footer">
          <a href="#" class="forgot-link">Forgot your password?</a>
          <br />
          <router-link to="/register" class="register-link">Don't have an account? Register as Customer</router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const username = ref('')
  const password = ref('')
  const error = ref('')
  const loading = ref(false)
  const router = useRouter()
  const role = ref('baker')
  const showPassword = ref(false)
  
  const login = async () => {
    error.value = ''
    loading.value = true
    let endpoint = ''
    if (role.value === 'baker') {
      endpoint = 'http://localhost:8000/api/v1/login/baker/'
    } else if (role.value === 'customer') {
      endpoint = 'http://localhost:8000/api/v1/login/customer/'
    } else if (role.value === 'staff') {
      endpoint = 'http://localhost:8000/api/v1/login/staff/'
    }
    try {
      const { data } = await axios.post(endpoint, {
        username: username.value,
        password: password.value,
      })
      localStorage.setItem('access_token', data.access)
      localStorage.setItem('refresh_token', data.refresh)
      if (data.user.is_staff) {
        router.push('/admin-welcome')
      } else if (data.user.is_baker) {
        router.push('/baker-welcome')
      } else if (data.user.is_customer) {
        router.push('/home')
      } else {
        router.push('/login')
      }
    } catch (err) {
      error.value = 'Invalid username or password'
    } finally {
      loading.value = false
    }
  }
  </script>
  
  <style scoped>
  * {
    box-sizing: border-box;
  }
  
  .login-wrapper {
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
  
  .cake-1 {
    top: 15%;
    left: 10%;
    animation-delay: 0s;
    animation-duration: 7s;
  }
  
  .cake-2 {
    top: 25%;
    right: 15%;
    animation-delay: 1s;
    animation-duration: 9s;
  }
  
  .cake-3 {
    bottom: 30%;
    left: 8%;
    animation-delay: 2s;
    animation-duration: 8s;
  }
  
  .cake-4 {
    top: 60%;
    right: 8%;
    animation-delay: 3s;
    animation-duration: 6s;
  }
  
  .cake-5 {
    bottom: 15%;
    left: 60%;
    animation-delay: 4s;
    animation-duration: 10s;
  }
  
  .cake-6 {
    top: 40%;
    left: 5%;
    animation-delay: 2.5s;
    animation-duration: 7.5s;
  }
  
  .cake-7 {
    bottom: 45%;
    right: 20%;
    animation-delay: 1.5s;
    animation-duration: 8.5s;
  }
  
  .cake-8 {
    top: 80%;
    left: 25%;
    animation-delay: 3.5s;
    animation-duration: 9.5s;
  }
  
  @keyframes cakeFloat {
    0% { 
      transform: translate(0px, 0px); 
    }
    25% { 
      transform: translate(15px, -20px); 
    }
    50% { 
      transform: translate(-10px, -35px); 
    }
    75% { 
      transform: translate(20px, -15px); 
    }
    100% { 
      transform: translate(0px, 0px); 
    }
  }
  
  @keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
  }
  
  .login-container {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 1.5rem;
    width: 100%;
    max-width: 400px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    position: relative;
    z-index: 1;
    animation: slideUp 0.6s ease-out;
  }
  
  @keyframes slideUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .login-header {
    text-align: center;
    margin-bottom: 2.5rem;
  }
  
  .logo-icon {
    width: 48px;
    height: 48px;
    margin: 0 auto 1rem;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    animation: pulse 2s infinite;
  }
  
  @keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
  }
  
  .logo-icon svg {
    width: 24px;
    height: 24px;
  }
  
  .login-header h2 {
    margin: 0 0 0.5rem 0;
    font-size: 2rem;
    font-weight: 700;
    color: #2d3748;
    letter-spacing: -0.02em;
  }
  
  .login-header p {
    margin: 0;
    color: #718096;
    font-size: 1rem;
  }
  
  .login-form {
    margin-bottom: 2rem;
  }
  
  .input-group {
    margin-bottom: 1.5rem;
  }
  
  .input-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #4a5568;
    font-size: 0.9rem;
  }
  
  .input-wrapper {
    position: relative;
  }
  
  .input-wrapper input {
    width: 100%;
    padding: 1rem 1rem 1rem 3rem;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    font-size: 1rem;
    transition: all 0.3s ease;
    background: #fff;
    color: #2d3748;
  }
  
  .input-wrapper input::placeholder {
    color: #a0aec0;
  }
  
  .input-wrapper input:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    transform: translateY(-2px);
  }
  
  .input-wrapper input:focus + .input-icon,
  .input-wrapper input:not(:placeholder-shown) + .input-icon {
    color: #667eea;
  }
  
  .input-wrapper input.error {
    border-color: #e53e3e;
    animation: shake 0.5s ease-in-out;
  }
  
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
  }
  
  .login-button {
    width: 100%;
    padding: 1rem;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }
  
  .login-button:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
  }
  
  .login-button:active {
    transform: translateY(0);
  }
  
  .login-button:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
  
  .loading-spinner {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }
  
  .spinner {
    width: 20px;
    height: 20px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-top: 2px solid white;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  
  .error-message {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: #fed7d7;
    color: #c53030;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1rem;
    font-size: 0.9rem;
    animation: fadeInShake 0.4s ease-out;
  }
  
  .error-message svg {
    width: 18px;
    height: 18px;
    flex-shrink: 0;
  }
  
  @keyframes fadeInShake {
    0% {
      opacity: 0;
      transform: translateX(-10px);
    }
    100% {
      opacity: 1;
      transform: translateX(0);
    }
  }
  
  .login-footer {
    text-align: center;
  }
  
  .forgot-link {
    color: #667eea;
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.3s ease;
  }
  
  .forgot-link:hover {
    color: #5a67d8;
    text-decoration: underline;
  }
  
  /* Responsive Design */
  @media (max-width: 480px) {
    .login-wrapper {
      padding: 1rem;
    }
    
    .login-container {
      padding: 2rem;
    }
    
    .login-header h2 {
      font-size: 1.75rem;
    }
  }
  
  .input-wrapper {
    position: relative;
  }
  
  .input-wrapper .styled-select {
    width: 100%;
    padding: 1rem 1rem 1rem 3rem;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    font-size: 1rem;
    transition: all 0.3s ease;
    background: #fff;
    color: #2d3748;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
  }
  
  .input-wrapper .styled-select:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    transform: translateY(-2px);
  }
  
  .input-wrapper .input-icon {
    position: absolute;
    left: 1rem;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    color: #a0aec0;
    z-index: 2;
    pointer-events: none;
  }
  
  .input-wrapper .styled-select:focus + .input-icon,
  .input-wrapper .styled-select:not(:placeholder-shown) + .input-icon {
    color: #667eea;
  }
  
  /* Hide default arrow for select */
  .input-wrapper .styled-select::-ms-expand {
    display: none;
  }
  .input-wrapper .styled-select {
    background-image: none;
  }
  
  .toggle-password {
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    z-index: 3;
    display: flex;
    align-items: center;
    height: 100%;
  }
  
  .toggle-password svg {
    width: 20px;
    height: 20px;
    color: #a0aec0;
    transition: color 0.2s;
  }
  
  .toggle-password:hover svg {
    color: #667eea;
    stroke: #667eea;
  }
  </style>