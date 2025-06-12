<template>
  <div class="cart-modal-bg" @click.self="$emit('close')">
    <div class="cart-container">
      <button class="cart-close-btn" @click="$emit('close')">&times;</button>
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
                <div class="cart-cake-price">
                  <template v-if="item.cake.offer_price">
                    <span class="original-price">Rs {{ Number(item.cake.price).toFixed(2) }}</span>
                    <span class="offer-price">Rs {{ Number(item.cake.offer_price).toFixed(2) }}</span>
                  </template>
                  <template v-else>
                    Rs {{ Number(item.cake.price).toFixed(2) }}
                  </template>
                </div>
              </div>
              <div class="cart-actions">
                <input type="number" min="1" v-model.number="item.quantity" @change="updateQuantity(item)" class="cart-qty-input" />
                <button class="cart-remove-btn" @click="removeItem(item.id)">&times;</button>
              </div>
            </div>
          </div>
          <div class="cart-summary">
            <div class="cart-total">
              Total: Rs {{ Number(cart.total_price).toFixed(2) }}
            </div>
            <button class="cart-checkout-btn">Proceed to Checkout</button>
          </div>
        </div>
        <div v-else class="cart-empty">Your cart is empty.</div>
      </div>
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
.cart-modal-bg {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(24,24,27,0.18);
  z-index: 3000;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  min-width: 100vw;
  backdrop-filter: blur(2px);
}
.cart-container {
  max-width: 480px;
  width: 95vw;
  background: rgba(255,255,255,0.98);
  border-radius: 24px;
  box-shadow: 0 8px 40px rgba(255,107,53,0.18), 0 1.5px 8px rgba(0,0,0,0.07);
  padding: 2.5rem 2rem 2rem 2rem;
  margin: 0 auto;
  position: relative;
  animation: fadeInCart 0.25s cubic-bezier(0.4,0,0.2,1);
  max-height: 90vh;
  overflow: hidden;
}
@keyframes fadeInCart {
  from { opacity: 0; transform: translateY(40px) scale(0.98); }
  to { opacity: 1; transform: none; }
}
.cart-title {
  font-size: 2rem;
  font-weight: 900;
  color: #f37022;
  margin-bottom: 2rem;
  text-align: center;
  letter-spacing: 0.5px;
}
.cart-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  max-height: 45vh;
  overflow-y: auto;
  padding-right: 6px;
  scrollbar-width: thin;
  scrollbar-color: #ff6b35 #ffe0e9;
}
.cart-list::-webkit-scrollbar {
  width: 8px;
  background: #ffe0e9;
  border-radius: 8px;
}
.cart-list::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #ff6b35, #ff006e);
  border-radius: 8px;
}
.cart-item {
  display: flex;
  align-items: center;
  gap: 1.2rem;
  background: #fff7f0;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(243,112,34,0.07);
  padding: 1.2rem 1.5rem;
  transition: box-shadow 0.18s;
}
.cart-item:hover {
  box-shadow: 0 8px 24px rgba(255,107,53,0.13);
}
.cart-cake-image {
  width: 80px;
  height: 60px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(255,107,53,0.08);
}
.cart-cake-info {
  flex: 1;
  min-width: 0;
}
.cart-cake-name {
  font-weight: 700;
  font-size: 1.1rem;
  margin-bottom: 0.2rem;
  color: #23232b;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.cart-cake-desc {
  color: #6d6d6d;
  font-size: 0.98rem;
  margin-bottom: 0.3rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.cart-cake-price {
  color: #f37022;
  font-size: 1rem;
  font-weight: 600;
}
.cart-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.cart-qty-input {
  width: 50px;
  padding: 0.3rem;
  border-radius: 8px;
  border: 1.5px solid #f37022;
  text-align: center;
  font-size: 1rem;
  font-weight: 600;
  background: #fff;
  color: #23232b;
  box-shadow: 0 1px 4px rgba(255,107,53,0.04);
}
.cart-remove-btn {
  background: #ff6b35;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  width: 32px;
  height: 32px;
  cursor: pointer;
  transition: background 0.2s;
  box-shadow: 0 1px 4px rgba(255,107,53,0.08);
}
.cart-remove-btn:hover {
  background: #f37022;
}
.cart-summary {
  margin-top: 2.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff7f0;
  border-radius: 14px;
  padding: 1.2rem 1.5rem;
  box-shadow: 0 1px 8px rgba(255,107,53,0.07);
}
.cart-total {
  font-size: 1.3rem;
  font-weight: 700;
  color: #23232b;
}
.cart-total .original-price {
  text-decoration: line-through;
  color: #b0b0b0;
  margin-right: 0.5em;
  font-size: 1.1rem;
  font-weight: 500;
}
.cart-total .offer-price {
  color: #ff006e;
  font-weight: bold;
  font-size: 1.18em;
}
.cart-checkout-btn {
  background: linear-gradient(90deg, #ff6b35 60%, #ff006e 100%);
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 0.9rem 2.5rem;
  font-size: 1.13rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 12px rgba(255,107,53,0.13);
}
.cart-checkout-btn:hover {
  background: linear-gradient(90deg, #ff006e 60%, #ff6b35 100%);
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
.original-price {
  text-decoration: line-through;
  color: #b0b0b0;
  margin-right: 0.5em;
}
.offer-price {
  color: #ff006e;
  font-weight: bold;
  font-size: 1.15em;
}
.cart-close-btn {
  position: absolute;
  top: 18px;
  right: 22px;
  background: none;
  border: none;
  font-size: 2.1rem;
  color: #ff6b35;
  cursor: pointer;
  z-index: 10;
  transition: color 0.18s;
}
.cart-close-btn:hover {
  color: #ff006e;
}
</style> 