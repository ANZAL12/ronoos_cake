<template>
  <div>
    <div class="home-header">
      <img src="/logo.png" alt="Ronoos Cake Logo" class="home-logo" />
      <h1 class="home-title">Ronoos <span>Cake</span></h1>
      <button class="cart-icon-btn" @click="showCart = true">
        🛒
      </button>
    </div>
    <nav class="navbar">
      <ul>
        <li @click="scrollToCakes">Our Collection</li>
        <li @click="showAboutUs">About Us</li>
        <li>X-Mas And New Year cakes</li>
        <li>Offers</li>
        <li>Track Your Order</li>
        <li @click="showContactUs">Contact Us</li>
        <li>Menu Item</li>
      </ul>
    </nav>
    <div class="cake-search-outer">
      <div class="cake-search-wrapper">
        <span class="cake-search-icon">
          <svg width="18" height="18" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="9" cy="9" r="7" stroke="#f37022" stroke-width="2"/>
            <line x1="14.4142" y1="14" x2="18" y2="17.5858" stroke="#f37022" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </span>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search cake"
          class="cake-search-box"
        />
      </div>
    </div>
    <template v-if="showAbout">
      <AboutUs />
    </template>
    <template v-else-if="showContact">
      <ContactUs />
    </template>
    <template v-else>
      <div id="cake-collection" class="cake-grid">
        <div v-if="filteredCakes.length === 0" class="no-cakes-message">
          No cakes available
        </div>
        <div v-for="cake in filteredCakes" :key="cake.name" class="cake-card">
          <img :src="getImageUrl(cake.image)" :alt="cake.name" class="cake-image" />
          <div class="cake-name">{{ cake.name }}</div>
          <div class="cake-price">Rs {{ Number(cake.price).toFixed(2) }}</div>
          <button class="view-cakes-btn" @click="openCakeModal(cake)">VIEW CAKE &rarr;</button>
        </div>
      </div>
      <div v-if="showCakeModal" class="cake-modal-overlay" @click.self="closeCakeModal">
        <div class="cake-modal">
          <button class="close-btn" @click="closeCakeModal">&times;</button>
          <img :src="getImageUrl(selectedCake.image)" :alt="selectedCake.name" class="modal-cake-image" />
          <h2 class="modal-cake-title">{{ selectedCake.name }}</h2>
          <div class="modal-cake-price">Rs {{ Number(selectedCake.price).toFixed(2) }}</div>
          <p class="modal-cake-desc">{{ selectedCake.description }}</p>
          <button class="add-to-cart-btn" @click="addToCart(selectedCake)">Add to Cart</button>
        </div>
      </div>
    </template>
    <!-- Always render cart modal -->
    <div v-if="showCart" class="cart-modal-overlay" @click.self="showCart = false">
      <div class="cart-modal-content">
        <button class="close-btn" @click="showCart = false">&times;</button>
        <CartView />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import AboutUs from './AboutUs.vue'
import CartView from './CartView.vue'
import ContactUs from './ContactUs.vue'

const cakes = ref([])
const showAbout = ref(false)
const showContact = ref(false)
const showCakeModal = ref(false)
const selectedCake = ref({})
const showCart = ref(false)
const searchQuery = ref("")

const filteredCakes = computed(() => {
  if (!searchQuery.value) return cakes.value;
  return cakes.value.filter(cake =>
    cake.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
})

function getImageUrl(path) {
  if (!path) return 'https://via.placeholder.com/220x180?text=No+Image';
  if (path.startsWith('http')) return path;
  return `http://localhost:8000${path}`;
}

function scrollToCakes() {
  showAbout.value = false
  showContact.value = false
  const el = document.getElementById('cake-collection');
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
  }
}

function showAboutUs() {
  showAbout.value = true
  showContact.value = false
}

function showContactUs() {
  showContact.value = true
  showAbout.value = false
}

function openCakeModal(cake) {
  selectedCake.value = cake
  showCakeModal.value = true
}

function closeCakeModal() {
  showCakeModal.value = false
  selectedCake.value = {}
}

async function addToCart(cake) {
  const token = localStorage.getItem('access_token')
  await fetch('/api/v1/cart/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({ cake_id: cake.id, quantity: 1 })
  })
  showCakeModal.value = false
  showCart.value = true
}

onMounted(async () => {
  try {
    const res = await fetch('/api/v1/cakes/')
    if (res.ok) {
      cakes.value = await res.json()
    }
  } catch (e) {
    cakes.value = []
  }
})
</script>

<style scoped>
:deep(body) {
  overflow-x: hidden;
}
.home-header,
.cake-grid,
.cake-search-outer,
.cake-search-wrapper {
  max-width: 100vw;
  box-sizing: border-box;
}
.navbar {
  background: #f37022;
  padding: 0.5rem 0;
  display: flex;
  justify-content: center;
}
.navbar ul {
  display: flex;
  gap: 2.5rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.navbar li {
  color: #fff;
  font-size: 1.25rem;
  font-family: 'Montserrat', sans-serif;
  cursor: pointer;
  transition: color 0.2s;
}
.navbar li:hover {
  color: #ffe0b2;
}
.cake-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2.5rem;
  padding: 2.5rem 2rem;
  background: #fff;
}
.cake-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.07);
  padding: 2rem 1.5rem 1.5rem 1.5rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: box-shadow 0.2s;
}
.cake-card:hover {
  box-shadow: 0 8px 32px rgba(243,112,34,0.15);
}
.cake-image {
  width: 220px;
  height: 180px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 1.5rem;
}
.cake-name {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #222;
}
.cake-price {
  font-size: 1.1rem;
  color: #f37022;
  margin-bottom: 1.2rem;
}
.view-cakes-btn {
  background: #f37022;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 0.7rem 2.2rem;
  font-size: 1rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s;
}
.view-cakes-btn:hover {
  background: #ff8c42;
}
@media (max-width: 600px) {
  .cake-grid {
    grid-template-columns: 1fr;
    padding: 1rem 0.5rem;
  }
  .cake-card {
    padding: 1.2rem 0.5rem;
  }
  .cake-image {
    width: 100%;
    height: 160px;
  }
}
.cake-modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(24,24,27,0.85);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}
.cake-modal {
  background: #fff;
  border-radius: 18px;
  padding: 2.5rem 2.2rem 2rem 2.2rem;
  min-width: 320px;
  max-width: 95vw;
  box-shadow: 0 8px 32px rgba(0,0,0,0.18);
  color: #23232b;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.close-btn {
  position: absolute;
  top: 12px;
  right: 18px;
  background: none;
  border: none;
  font-size: 2rem;
  color: #f37022;
  cursor: pointer;
  z-index: 10;
}
.modal-cake-image {
  width: 220px;
  height: 180px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 1.2rem;
}
.modal-cake-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #f37022;
}
.modal-cake-price {
  font-size: 1.2rem;
  color: #ff6b35;
  margin-bottom: 1rem;
}
.modal-cake-desc {
  font-size: 1.08rem;
  color: #23232b;
  margin-bottom: 1.5rem;
  text-align: center;
}
.add-to-cart-btn {
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
.add-to-cart-btn:hover {
  background: #ff8c42;
}
.cart-icon-btn {
  position: absolute;
  top: 2.2rem;
  right: 2.2rem;
  background: #fff7f0;
  border: none;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  font-size: 1.7rem;
  box-shadow: 0 2px 8px rgba(243,112,34,0.07);
  cursor: pointer;
  transition: background 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}
.cart-icon-btn:hover {
  background: #ffe0b2;
}
.cart-modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(24,24,27,0.85);
  z-index: 3000;
  display: flex;
  align-items: center;
  justify-content: center;
}
.cart-modal-content {
  background: #fff;
  border-radius: 18px;
  padding: 2.5rem 2.2rem 2rem 2.2rem;
  min-width: 340px;
  max-width: 95vw;
  box-shadow: 0 8px 32px rgba(0,0,0,0.18);
  color: #23232b;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.cake-search-outer {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  margin-top: 2rem;
  margin-bottom: -1.5rem;
  padding-right: 2rem;
}
.cake-search-wrapper {
  position: relative;
  width: 340px;
  max-width: 90vw;
}
.cake-search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  align-items: center;
  height: 100%;
  color: #f37022;
  pointer-events: none;
  z-index: 2;
}
.cake-search-box {
  width: 100%;
  height: 44px;
  padding: 0 1.2rem 0 2.5rem;
  border: 1.5px solid #f37022;
  border-radius: 8px;
  font-size: 1.08rem;
  font-family: 'Montserrat', sans-serif;
  outline: none;
  transition: border 0.2s;
  box-sizing: border-box;
}
.cake-search-box:focus {
  border: 2px solid #ff8c42;
}
@media (max-width: 600px) {
  .cake-search-outer {
    padding-right: 0.5rem;
    margin-top: 1rem;
    margin-bottom: -0.5rem;
  }
  .cake-search-wrapper {
    width: 100%;
    max-width: 100vw;
  }
}
.no-cakes-message {
  grid-column: 1/-1;
  text-align: center;
  color: #f37022;
  font-size: 1.2rem;
  font-family: 'Montserrat', sans-serif;
  padding: 2rem 0;
  font-weight: 600;
}
</style> 