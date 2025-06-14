<template>
  <div class="confirmation-container">
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else>
      <h1 class="confirmation-title">Thank You for Your Order!</h1>
      <div class="confirmation-summary">
        <p>Your order has been placed successfully.</p>
        <div class="order-info">
          <p><strong>Order ID:</strong> {{ order?.id }}</p>
          <p><strong>Status:</strong> {{ order?.status }}</p>
          <p><strong>Total Amount:</strong> ₹{{ order?.total_amount }}</p>
        </div>
        <div class="delivery-info" v-if="delivery">
          <h2>Delivery Details</h2>
          <p><strong>Name:</strong> {{ delivery.customer_name }}</p>
          <p><strong>Mobile:</strong> {{ delivery.mobile_number }}</p>
          <p><strong>Location:</strong> {{ delivery.location }}</p>
          <p><strong>Address:</strong> {{ delivery.address }}</p>
        </div>
        <div class="confirmation-actions">
          <router-link to="/home" class="btn-primary">Go to Home</router-link>
          <router-link to="/orders" class="btn-secondary">View My Orders</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const orderId = route.params.orderId
const order = ref(null)
const delivery = ref(null)
const loading = ref(true)

function getAuthToken() {
  return localStorage.getItem('access_token')
}

async function fetchOrderAndDelivery() {
  loading.value = true
  const token = getAuthToken()
  try {
    // Fetch order
    const orderRes = await fetch(`/api/v1/orders/${orderId}/`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    if (orderRes.ok) {
      order.value = await orderRes.json()
    }
    // Fetch delivery
    const deliveryRes = await fetch(`/api/v1/delivery/?order=${orderId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    if (deliveryRes.ok) {
      const deliveries = await deliveryRes.json()
      delivery.value = deliveries.length ? deliveries[0] : null
    }
  } catch (e) {
    // handle error
  } finally {
    loading.value = false
  }
}

onMounted(fetchOrderAndDelivery)
</script>

<style scoped>
.confirmation-container {
  max-width: 500px;
  margin: 3rem auto;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(255,107,53,0.10);
  padding: 2.5rem 2rem 2.5rem 2rem;
  text-align: center;
}
.confirmation-title {
  font-size: 2rem;
  color: #4a90e2;
  margin-bottom: 1.5rem;
}
.confirmation-summary {
  font-size: 1.1rem;
  color: #23232b;
}
.order-info, .delivery-info {
  background: #f7f7fa;
  border-radius: 10px;
  padding: 1rem 1.2rem;
  margin: 1.2rem 0;
  text-align: left;
}
.confirmation-actions {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
}
.btn-primary, .btn-secondary {
  padding: 0.7rem 1.7rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: background 0.2s;
}
.btn-primary {
  background: #4a90e2;
  color: #fff;
}
.btn-secondary {
  background: #f5f5f5;
  color: #333;
}
.btn-primary:hover {
  background: #357abd;
}
.btn-secondary:hover {
  background: #e0e0e0;
}
.loading {
  font-size: 1.2rem;
  color: #888;
  margin: 2rem 0;
}
</style> 