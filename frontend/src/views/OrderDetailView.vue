<template>
  <div class="order-detail-container">
    <h1 class="order-detail-title">Order Details</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="!order" class="empty">Order not found.</div>
    <div v-else>
      <div class="order-info">
        <p><strong>Order ID:</strong> {{ order.id }}</p>
        <p><strong>Status:</strong> {{ order.status }}</p>
        <p><strong>Total Amount:</strong> ₹{{ order.total_amount }}</p>
        <p><strong>Date:</strong> {{ new Date(order.created_at).toLocaleString() }}</p>
      </div>
      <div class="order-items">
        <h2>Items</h2>
        <ul>
          <li v-for="item in order.items" :key="item.cake">
            <span><strong>Cake ID:</strong> {{ item.cake }}</span> |
            <span><strong>Quantity:</strong> {{ item.quantity }}</span> |
            <span><strong>Price:</strong> ₹{{ item.price }}</span>
          </li>
        </ul>
      </div>
      <div v-if="delivery" class="delivery-info">
        <h2>Delivery Details</h2>
        <p><strong>Name:</strong> {{ delivery.customer_name }}</p>
        <p><strong>Mobile:</strong> {{ delivery.mobile_number }}</p>
        <p><strong>Location:</strong> {{ delivery.location }}</p>
        <p><strong>Address:</strong> {{ delivery.address }}</p>
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
    console.error(e);
  }
  loading.value = false
}

onMounted(fetchOrderAndDelivery)
</script>

<style scoped>
.order-detail-container {
  max-width: 600px;
  margin: 3rem auto;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(255,107,53,0.10);
  padding: 2.5rem 2rem 2.5rem 2rem;
}
.order-detail-title {
  font-size: 2rem;
  color: #4a90e2;
  margin-bottom: 2rem;
  text-align: center;
}
.order-info, .order-items, .delivery-info {
  background: #f7f7fa;
  border-radius: 10px;
  padding: 1rem 1.2rem;
  margin: 1.2rem 0;
}
.order-items ul {
  list-style: none;
  padding: 0;
}
.order-items li {
  margin-bottom: 0.5rem;
}
.loading {
  font-size: 1.2rem;
  color: #888;
  margin: 2rem 0;
  text-align: center;
}
.empty {
  font-size: 1.1rem;
  color: #888;
  margin: 2rem 0;
  text-align: center;
}
</style> 