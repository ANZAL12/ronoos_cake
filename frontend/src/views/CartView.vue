<template>
  <div class="cart-container">
    <h1 class="cart-title">Your Cart</h1>
    <div v-if="loading" class="cart-loading">Loading...</div>
    <div v-else>
      <div v-if="cart.items && cart.items.length">
        <div class="cart-list">
          <div class="cart-item" v-for="item in cart.items" :key="item.id">
            <img :src="getImageUrl(item.cake.image)" :alt="item.cake.name" class="cart-cake-image" />
            <div class="cart-cake-info">
              <div class="cart-cake-name">{{ item.cake.name }}</div>
              <div class="cart-cake-desc">{{ item.cake.description }}</div>
              <div class="cart-cake-price">Rs {{ Number(item.cake.price).toFixed(2) }}</div>
            </div>
            <div class="cart-actions">
              <input type="number" min="1" v-model.number="item.quantity" @change="updateQuantity(item)" class="cart-qty-input" />
              <button class="cart-remove-btn" @click="removeItem(item.id)">&times;</button>
            </div>
            <div class="cart-item-total">Rs {{ Number(item.total_price).toFixed(2) }}</div>
          </div>
        </div>
        <div class="cart-summary">
          <div class="cart-total">Total: <span>Rs {{ Number(cart.total_price).toFixed(2) }}</span></div>
          <button class="cart-checkout-btn">Proceed to Checkout</button>
        </div>
      </div>
      <div v-else class="cart-empty">Your cart is empty.</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const cart = ref({ items: [] })
const loading = ref(true)

function getImageUrl(path) {
  if (!path) return 'https://via.placeholder.com/220x180?text=No+Image';
  if (path.startsWith('http')) return path;
  return `http://localhost:8000${path}`;
}

async function fetchCart() {
  loading.value = true
  try {
    const token = localStorage.getItem('access_token')
    const res = await fetch('/api/v1/cart/', {
      headers: { Authorization: `Bearer ${token}` }
    })
    if (res.ok) {
      cart.value = await res.json()
    }
  } finally {
    loading.value = false
  }
}

async function updateQuantity(item) {
  const token = localStorage.getItem('access_token')
  await fetch(`/api/v1/cart/item/${item.id}/`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({ quantity: item.quantity })
  })
  fetchCart()
}

async function removeItem(itemId) {
  const token = localStorage.getItem('access_token')
  await fetch(`/api/v1/cart/item/${itemId}/`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${token}` }
  })
  fetchCart()
}

onMounted(fetchCart)
</script>

<style scoped>
.cart-container {
  max-width: 800px;
  margin: 2.5rem auto;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.07);
  padding: 2.5rem 2rem;
}
.cart-title {
  font-size: 2rem;
  font-weight: 800;
  color: #f37022;
  margin-bottom: 2rem;
  text-align: center;
}
.cart-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.cart-item {
  display: flex;
  align-items: center;
  gap: 1.2rem;
  background: #fff7f0;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(243,112,34,0.07);
  padding: 1.2rem 1.5rem;
}
.cart-cake-image {
  width: 80px;
  height: 60px;
  object-fit: cover;
  border-radius: 8px;
}
.cart-cake-info {
  flex: 1;
}
.cart-cake-name {
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 0.2rem;
}
.cart-cake-desc {
  color: #23232b;
  font-size: 0.98rem;
  margin-bottom: 0.3rem;
}
.cart-cake-price {
  color: #f37022;
  font-size: 1rem;
}
.cart-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.cart-qty-input {
  width: 50px;
  padding: 0.3rem;
  border-radius: 6px;
  border: 1px solid #f37022;
  text-align: center;
}
.cart-remove-btn {
  background: #ff6b35;
  color: #fff;
  border: none;
  border-radius: 6px;
  font-size: 1.2rem;
  width: 32px;
  height: 32px;
  cursor: pointer;
  transition: background 0.2s;
}
.cart-remove-btn:hover {
  background: #f37022;
}
.cart-item-total {
  font-weight: 700;
  color: #f37022;
  font-size: 1.1rem;
  margin-left: 1.2rem;
}
.cart-summary {
  margin-top: 2.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.cart-total {
  font-size: 1.3rem;
  font-weight: 700;
  color: #23232b;
}
.cart-total span {
  color: #f37022;
}
.cart-checkout-btn {
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
.cart-checkout-btn:hover {
  background: #ff8c42;
}
.cart-empty {
  text-align: center;
  color: #888;
  font-size: 1.2rem;
  margin-top: 2.5rem;
}
.cart-loading {
  text-align: center;
  color: #888;
  font-size: 1.2rem;
  margin-top: 2.5rem;
}
</style> 