<template>
  <div class="contactus-container">
    <div class="contactus-header">
      <h1 class="contactus-title">Contact <span>Ronoos Cake</span></h1>
      <p class="contactus-desc">We'd love to hear from you! Reach out for orders, feedback, or just to say hello.</p>
    </div>
    <div class="contactus-content">
      <div class="contactus-info">
        <h2>Contact Information</h2>
        <ul>
          <li><strong>Email:</strong> ronooscake@example.com</li>
          <li><strong>Phone:</strong> +91 98765 43210</li>
          <li><strong>Address:</strong> 123, Sweet Street, Cake City, India</li>
        </ul>
      </div>
      <form class="contactus-form" @submit.prevent="submitForm">
        <h2>Send us a message</h2>
        <input v-model="name" type="text" placeholder="Your Name" required />
        <input v-model="email" type="email" placeholder="Your Email" required />
        <textarea v-model="message" placeholder="Your Message" rows="4" required></textarea>
        <button type="submit">Send Message</button>
        <div v-if="success" class="contactus-success">Thank you! We'll get back to you soon.</div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const name = ref('')
const email = ref('')
const message = ref('')
const success = ref(false)

function submitForm() {
  name.value = ''
  email.value = ''
  message.value = ''
  success.value = true
  setTimeout(() => { success.value = false }, 2500)
}
</script>

<style scoped>
.contactus-container {
  background: #fff;
  min-height: 100vh;
  padding: 0 0 3rem 0;
}
.contactus-header {
  text-align: center;
  padding: 2.5rem 0 1.5rem 0;
}
.contactus-title {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(90deg, #f37022, #ff8c42, #ff6b35);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-fill-color: transparent;
  margin-bottom: 0.5rem;
}
.contactus-title span {
  color: #f37022;
}
.contactus-desc {
  color: #23232b;
  font-size: 1.15rem;
  margin-bottom: 1.5rem;
}
.contactus-content {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  gap: 3rem;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.07);
  padding: 2rem 2.5rem;
  font-size: 1.15rem;
  color: #23232b;
  flex-wrap: wrap;
  justify-content: center;
}
.contactus-info {
  flex: 1 1 250px;
  min-width: 220px;
}
.contactus-info ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.contactus-info li {
  margin-bottom: 1rem;
  font-size: 1.08rem;
}
.contactus-form {
  flex: 1 1 320px;
  min-width: 260px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  background: #fff7f0;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(243,112,34,0.07);
  padding: 1.5rem 1.5rem 1.2rem 1.5rem;
}
.contactus-form input,
.contactus-form textarea {
  border: 1.5px solid #f37022;
  border-radius: 8px;
  padding: 0.7rem 1rem;
  font-size: 1.08rem;
  font-family: inherit;
  outline: none;
  transition: border 0.2s;
}
.contactus-form input:focus,
.contactus-form textarea:focus {
  border: 2px solid #ff6b35;
}
.contactus-form button {
  background: #f37022;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 0.8rem 2.5rem;
  font-size: 1.08rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.contactus-form button:hover {
  background: #ff8c42;
}
.contactus-success {
  color: #388e3c;
  background: #e8f5e9;
  border-radius: 6px;
  padding: 0.7rem 1rem;
  margin-top: 0.7rem;
  text-align: center;
  font-weight: 600;
  font-size: 1.05rem;
}
</style> 