<template>
  <div class="orders-container">
    <h1 class="orders-title">My Orders</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="orders.length === 0" class="empty">No orders found.</div>
    <div v-else>
      <table class="orders-table">
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Status</th>
            <th>Total</th>
            <th>Date</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in orders" :key="order.id">
            <td>{{ order.id }}</td>
            <td>{{ order.status }}</td>
            <td>₹{{ order.total_amount }}</td>
            <td>{{ new Date(order.created_at).toLocaleString() }}</td>
            <td>
              <router-link :to="`/orders/${order.id}`" class="btn-primary">View Details</router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const orders = ref([])
const loading = ref(true)

function getAuthToken() {
  return localStorage.getItem('access_token')
}

async function fetchOrders() {
  loading.value = true
  const token = getAuthToken()
  try {
    const res = await fetch('/api/v1/orders/', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    if (res.ok) {
      orders.value = await res.json()
    }
  } catch (e) {
    console.error(e);
  }
  loading.value = false
}

onMounted(fetchOrders)
</script>

<style scoped>
.orders-container {
  max-width: 900px;
  margin: 3rem auto;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(255,107,53,0.10);
  padding: 2.5rem 2rem 2.5rem 2rem;
}
.orders-title {
  font-size: 2rem;
  color: #4a90e2;
  margin-bottom: 2rem;
  text-align: center;
}
.orders-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}
.orders-table th, .orders-table td {
  padding: 0.8rem 1rem;
  border-bottom: 1px solid #eee;
  text-align: left;
}
.orders-table th {
  background: #f7f7fa;
}
.btn-primary {
  background: #4a90e2;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.2rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: background 0.2s;
}
.btn-primary:hover {
  background: #357abd;
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