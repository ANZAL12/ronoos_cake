<template>
  <div class="delivery-container">
    <h1 class="delivery-title">Delivery Details</h1>
    <form @submit.prevent="submitDeliveryDetails" class="delivery-form">
      <div class="form-group">
        <label for="customerName">Full Name</label>
        <input 
          type="text" 
          id="customerName" 
          v-model="deliveryDetails.customer_name" 
          required
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label for="mobileNumber">Mobile Number</label>
        <input 
          type="tel" 
          id="mobileNumber" 
          v-model="deliveryDetails.mobile_number" 
          required
          pattern="[0-9]{10}"
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label for="location">Location/Landmark</label>
        <input 
          type="text" 
          id="location" 
          v-model="deliveryDetails.location" 
          required
          placeholder="Enter nearby landmark or location"
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label for="address">Full Address</label>
        <textarea 
          id="address" 
          v-model="deliveryDetails.address" 
          required
          rows="4"
          class="form-textarea"
        ></textarea>
      </div>

      <div class="form-actions">
        <button type="button" @click="goBack" class="btn-secondary">Back</button>
        <button type="submit" :disabled="loading" class="btn-primary">
          {{ loading ? 'Saving...' : 'Save Delivery Details' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const loading = ref(false)

const deliveryDetails = ref({
  customer_name: '',
  mobile_number: '',
  location: '',
  address: '',
  order: route.params.orderId
})

function getAuthToken() {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return null
  }
  return token
}

async function submitDeliveryDetails() {
  const token = getAuthToken()
  if (!token) return

  loading.value = true
  try {
    const response = await fetch('/api/v1/delivery/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(deliveryDetails.value)
    })

    if (response.status === 401) {
      localStorage.removeItem('access_token')
      router.push('/login')
      return
    }

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || 'Failed to save delivery details')
    }

    // Redirect to order confirmation or success page
    router.push(`/order-confirmation/${deliveryDetails.value.order}`)
  } catch (error) {
    console.error('Error saving delivery details:', error)
    alert(error.message)
  } finally {
    loading.value = false
  }
}

function goBack() {
  router.back()
}
</script>

<style scoped>
.delivery-container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.delivery-title {
  text-align: center;
  color: #333;
  margin-bottom: 2rem;
}

.delivery-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-weight: 500;
  color: #555;
}

.form-input,
.form-textarea {
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.2s;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #4a90e2;
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 1rem;
}

.btn-primary,
.btn-secondary {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary {
  background: #4a90e2;
  color: white;
}

.btn-primary:hover {
  background: #357abd;
}

.btn-primary:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.btn-secondary {
  background: #f5f5f5;
  color: #333;
}

.btn-secondary:hover {
  background: #e5e5e5;
}
</style> 