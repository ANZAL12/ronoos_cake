<template>
  <div class="checkout-container">
    <h1 class="checkout-title">Checkout</h1>
    <div v-if="loading" class="checkout-loading">Loading...</div>
    <div v-else>
      <div v-if="cart.items && cart.items.length">
        <transition-group name="list" tag="div" class="checkout-list">
          <div 
            class="checkout-item" 
            v-for="item in cart.items" 
            :key="item.id"
            :class="{ 'updating': updatingItems.has(item.id) }"
          >
            <img :src="getImageUrl(item.cake.image)" :alt="item.cake.name" class="checkout-cake-image" />
            <div class="checkout-cake-info">
              <div class="checkout-cake-name">{{ item.cake.name }}</div>
              <div class="checkout-cake-desc">{{ item.cake.description }}</div>
              <div class="checkout-cake-price">
                <template v-if="item.cake.offer_price">
                  <span class="original-price">Rs {{ Number(item.cake.price).toFixed(2) }}</span>
                  <span class="offer-price">Rs {{ Number(item.cake.offer_price).toFixed(2) }}</span>
                </template>
                <template v-else>
                  Rs {{ Number(item.cake.price).toFixed(2) }}
                </template>
              </div>
            </div>
            <div class="checkout-actions">
              <button 
                class="qty-btn" 
                @click="changeQty(item, -1)"
                :disabled="updatingItems.has(item.id)"
              >-</button>
              <span>Qty: {{ item.quantity }}</span>
              <button 
                v-if="item.quantity < 4" 
                class="qty-btn" 
                @click="changeQty(item, 1)"
                :disabled="updatingItems.has(item.id)"
              >+</button>
            </div>
          </div>
        </transition-group>
        <div class="checkout-summary">
          <div class="checkout-total">
            Total: Rs {{ Number(cart.total_price).toFixed(2) }}
          </div>
          <div class="checkout-payment-options">
            <button class="checkout-pay-btn">Pay Now</button>
            <button class="checkout-cod-btn" @click="handlePayOnDelivery">Pay on Delivery</button>
          </div>
        </div>
      </div>
      <div v-else class="checkout-empty">Your cart is empty.</div>
    </div>

    <!-- Custom Modal -->
    <div v-if="showModal" class="modal-overlay" @click="cancelRemove">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>Remove Item</h2>
        </div>
        <div class="modal-body">
          <p>Are you sure you want to remove this item from your cart?</p>
          <div class="modal-item-preview" v-if="itemToRemove">
            <img :src="getImageUrl(itemToRemove.cake.image)" :alt="itemToRemove.cake.name" />
            <div class="modal-item-details">
              <h3>{{ itemToRemove.cake.name }}</h3>
              <p class="modal-item-price">
                Rs {{ Number(itemToRemove.cake.offer_price || itemToRemove.cake.price).toFixed(2) }}
              </p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="modal-btn cancel-btn" @click="cancelRemove">Cancel</button>
          <button class="modal-btn confirm-btn" @click="confirmRemove">Remove</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const cart = ref({ items: [] })
const loading = ref(true)
const showModal = ref(false)
const itemToRemove = ref(null)
const updatingItems = ref(new Set())

function getImageUrl(path) {
  if (!path) return 'https://via.placeholder.com/220x180?text=No+Image';
  if (path.startsWith('http')) return path;
  return `http://localhost:8000${path}`;
}

// Function to get auth token
function getAuthToken() {
  const token = localStorage.getItem('access_token')
  if (!token) {
    // If no token, redirect to login
    router.push('/login')
    return null
  }
  return token
}

// Function to handle auth errors
function handleAuthError() {
  // Clear invalid token
  localStorage.removeItem('access_token')
  // Redirect to login
  router.push('/login')
}

async function fetchCart() {
  loading.value = true
  try {
    const token = getAuthToken()
    if (!token) return

    const res = await fetch('/api/v1/cart/', {
      headers: { 
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    })
    
    if (res.status === 401) {
      handleAuthError()
      return
    }
    
    if (res.ok) {
      cart.value = await res.json()
    }
  } catch (error) {
    console.error('Error fetching cart:', error)
  } finally {
    loading.value = false
  }
}

// Update cart total price
function updateCartTotal() {
  if (!cart.value.items) return;
  cart.value.total_price = cart.value.items.reduce((total, item) => {
    const price = item.cake.offer_price || item.cake.price;
    return total + (price * item.quantity);
  }, 0);
}

function showRemoveConfirmation(item) {
  itemToRemove.value = item;
  showModal.value = true;
}

function cancelRemove() {
  showModal.value = false;
  itemToRemove.value = null;
}

async function confirmRemove() {
  if (!itemToRemove.value) return;
  
  const token = getAuthToken()
  if (!token) return

  try {
    // Mark item as updating
    updatingItems.value.add(itemToRemove.value.id)

    // Optimistically remove item from local state with animation
    const itemId = itemToRemove.value.id;
    cart.value.items = cart.value.items.filter(i => i.id !== itemId);
    updateCartTotal();
    
    // Then remove from backend
    const removeResponse = await fetch(`/api/v1/cart/item/${itemId}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    if (removeResponse.status === 401) {
      handleAuthError()
      return
    }

    if (!removeResponse.ok) {
      // If backend update fails, revert the change
      const errorData = await removeResponse.json();
      console.error('Failed to remove item:', errorData);
      // Revert only this specific item
      const item = itemToRemove.value;
      cart.value.items.push(item);
      updateCartTotal();
    }
  } catch (error) {
    // If there's an error, revert only this specific item
    const item = itemToRemove.value;
    cart.value.items.push(item);
    updateCartTotal();
    console.error('Error removing item:', error);
  } finally {
    updatingItems.value.delete(itemToRemove.value.id)
    showModal.value = false;
    itemToRemove.value = null;
  }
}

async function changeQty(item, delta) {
  // Store original quantity for potential revert
  const originalQty = item.quantity;
  
  try {
    const newQty = item.quantity + delta;
    const token = getAuthToken()
    if (!token) return

    // Check quantity limit
    if (newQty > 4) {
      return;
    }

    // Show confirmation if trying to remove item
    if (newQty < 1) {
      showRemoveConfirmation(item);
      return;
    }

    // Mark this item as updating
    updatingItems.value.add(item.id)

    // Update quantity in local state
    const itemIndex = cart.value.items.findIndex(i => i.id === item.id);
    if (itemIndex !== -1) {
      cart.value.items[itemIndex].quantity = newQty;
      updateCartTotal();
    }

    // Then update backend
    const updateResponse = await fetch(`/api/v1/cart/item/${item.id}/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ quantity: newQty })
    });

    if (updateResponse.status === 401) {
      handleAuthError()
      return
    }

    if (!updateResponse.ok) {
      // If backend update fails, revert only this specific item
      if (itemIndex !== -1) {
        cart.value.items[itemIndex].quantity = originalQty;
        updateCartTotal();
      }
      console.error('Failed to update quantity:', await updateResponse.text());
    }
  } catch (error) {
    // If there's an error, revert only this specific item
    const itemIndex = cart.value.items.findIndex(i => i.id === item.id);
    if (itemIndex !== -1) {
      cart.value.items[itemIndex].quantity = originalQty;
      updateCartTotal();
    }
    console.error('Error in changeQty:', error);
  } finally {
    // Remove from updating set
    updatingItems.value.delete(item.id)
  }
}

async function handlePayOnDelivery() {
  try {
    const token = getAuthToken()
    if (!token) return

    // Create order first
    const orderResponse = await fetch('/api/v1/orders/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        items: cart.value.items.map(item => ({
          cake: item.cake.id,
          quantity: item.quantity
        }))
      })
    })

    if (orderResponse.status === 401) {
      handleAuthError()
      return
    }

    if (!orderResponse.ok) {
      throw new Error('Failed to create order')
    }

    const orderData = await orderResponse.json()
    
    // Navigate to delivery details page
    router.push(`/delivery-details/${orderData.id}`)
  } catch (error) {
    console.error('Error creating order:', error)
    alert('Failed to create order. Please try again.')
  }
}

onMounted(fetchCart)
</script>

<style scoped>
.checkout-container {
  max-width: 600px;
  margin: 2rem auto;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 4px 24px rgba(255,107,53,0.10);
  padding: 2rem 1.5rem 2.5rem 1.5rem;
}
.checkout-title {
  font-size: 2rem;
  color: #f37022;
  text-align: center;
  margin-bottom: 2rem;
}
.checkout-list {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  max-height: 40vh;
  overflow-y: auto;
  position: relative;
}
.checkout-item {
  display: flex;
  align-items: center;
  gap: 1.2rem;
  background: #fff7f0;
  border-radius: 14px;
  box-shadow: 0 2px 8px rgba(243,112,34,0.07);
  padding: 1rem 1.2rem;
  transition: all 0.3s ease;
}
.checkout-cake-image {
  width: 70px;
  height: 55px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(255,107,53,0.08);
}
.checkout-cake-info {
  flex: 1;
  min-width: 0;
}
.checkout-cake-name {
  font-weight: 700;
  font-size: 1.1rem;
  margin-bottom: 0.2rem;
  color: #23232b;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.checkout-cake-desc {
  color: #6d6d6d;
  font-size: 0.98rem;
  margin-bottom: 0.3rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.checkout-cake-price {
  color: #f37022;
  font-size: 1rem;
  font-weight: 600;
}
.checkout-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.checkout-summary {
  margin-top: 2.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff7f0;
  border-radius: 14px;
  padding: 1.2rem 1.5rem;
  box-shadow: 0 1px 8px rgba(255,107,53,0.07);
}
.checkout-total {
  font-size: 1.3rem;
  font-weight: 700;
  color: #23232b;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}
.checkout-payment-options {
  display: flex;
  gap: 1.5rem;
}
.checkout-pay-btn, .checkout-cod-btn {
  background: linear-gradient(90deg, #ff6b35 60%, #ff006e 100%);
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 0.8rem 2.2rem;
  font-size: 1.1rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 12px rgba(255,107,53,0.13);
}
.checkout-cod-btn {
  background: linear-gradient(90deg, #ff006e 60%, #ff6b35 100%);
}
.checkout-pay-btn:hover, .checkout-cod-btn:hover {
  filter: brightness(1.1);
}
.checkout-empty {
  text-align: center;
  color: #888;
  font-size: 1.2rem;
  margin-top: 2.5rem;
  animation: fadeIn 0.5s ease;
}
.checkout-loading {
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
.qty-btn {
  background: #f37022;
  color: #fff;
  border: none;
  border-radius: 6px;
  width: 32px;
  height: 32px;
  font-size: 1.2rem;
  font-weight: bold;
  cursor: pointer;
  margin: 0 0.5rem;
  transition: all 0.2s ease;
}
.qty-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
  opacity: 0.7;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  width: 90%;
  max-width: 400px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.15);
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    transform: translateY(-20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.modal-header {
  margin-bottom: 1.5rem;
}

.modal-header h2 {
  color: #f37022;
  font-size: 1.5rem;
  margin: 0;
}

.modal-body {
  margin-bottom: 2rem;
}

.modal-body p {
  color: #666;
  margin-bottom: 1rem;
}

.modal-item-preview {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: #fff7f0;
  padding: 1rem;
  border-radius: 12px;
  margin-top: 1rem;
}

.modal-item-preview img {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 8px;
}

.modal-item-details h3 {
  margin: 0 0 0.5rem 0;
  color: #23232b;
  font-size: 1.1rem;
}

.modal-item-price {
  color: #f37022;
  font-weight: 600;
  margin: 0;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.modal-btn {
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.cancel-btn {
  background: #f5f5f5;
  color: #666;
}

.confirm-btn {
  background: linear-gradient(90deg, #ff6b35 60%, #ff006e 100%);
  color: white;
}

.cancel-btn:hover {
  background: #eee;
}

.confirm-btn:hover {
  filter: brightness(1.1);
}

/* List transition animations */
.list-enter-active,
.list-leave-active {
  transition: all 0.3s ease;
}

.list-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.list-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

/* Ensure smooth layout transitions */
.checkout-list {
  position: relative;
}

.checkout-item {
  transition: all 0.3s ease;
}

/* Add a subtle hover effect */
.checkout-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(243,112,34,0.12);
}

/* Smooth price updates */
.checkout-total {
  transition: all 0.3s ease;
}

/* Add a fade effect for the empty cart message */
.checkout-empty {
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Improve button transitions */
.qty-btn {
  transition: all 0.2s ease;
}

.qty-btn:hover {
  transform: scale(1.1);
}

.qty-btn:active {
  transform: scale(0.95);
}

/* Add a subtle pulse animation when quantity changes */
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

.checkout-actions span {
  display: inline-block;
  transition: all 0.3s ease;
}

.checkout-actions span:active {
  animation: pulse 0.3s ease;
}

/* Add updating state styles */
.checkout-item.updating {
  opacity: 0.7;
  pointer-events: none;
}

.checkout-item.updating .qty-btn {
  cursor: not-allowed;
}

/* Add loading indicator for updating items */
.checkout-item.updating::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 14px;
  z-index: 1;
}
</style> 