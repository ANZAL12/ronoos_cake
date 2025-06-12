<template>
  <div class="homepage-bg">
    <header class="main-header">
      <div class="header-content">
        <img src="/logo.png" alt="Ronoos Cake Logo" class="logo" />
        <h1 class="brand-title">Ronoos <span class="highlight">Cake</span></h1>
        <nav class="main-nav">
          <ul>
            <li @click="scrollToCakes">Cakes</li>
            <li @click="showAboutUs">About</li>
            <li>Offers</li>
            <li>Track Order</li>
            <li @click="showContactUs">Contact</li>
          </ul>
        </nav>
        <button class="cart-btn" @click="showCart = true">
          <span class="cart-icon">🛒</span>
        </button>
      </div>
    </header>
    <section class="hero-section">
      <div class="hero-content">
        <h2>Delight in Every Slice</h2>
        <p>Discover our handcrafted cakes, baked fresh for every occasion. Order online and enjoy doorstep delivery!</p>
        <button class="explore-btn" @click="scrollToCakes">Explore Cakes</button>
      </div>
      <img src="/hero-cake.png" alt="Hero Cake" class="hero-img" />
    </section>
    <section class="search-section">
      <div class="search-bar">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search for your favorite cake..."
        />
        <button class="search-btn">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="9" cy="9" r="7" stroke="#ff6b35" stroke-width="2"/>
            <line x1="14.4142" y1="14" x2="18" y2="17.5858" stroke="#ff6b35" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
    </section>
    <template v-if="showAbout">
      <AboutUs />
    </template>
    <template v-else-if="showContact">
      <ContactUs />
    </template>
    <template v-else>
      <section id="cake-collection" class="cakes-section">
        <h3 class="section-title">Our Cake Collection</h3>
        <div v-if="filteredCakes.length === 0" class="no-cakes">No cakes found.</div>
        <div
          class="cakes-grid"
          :class="{ 'single-cake': filteredCakes.length === 1 }"
        >
          <div v-for="cake in filteredCakes" :key="cake.name" class="cake-card-new">
            <img :src="getImageUrl(cake.image)" :alt="cake.name" class="cake-img" />
            <div class="cake-info">
              <h4 class="cake-title">{{ cake.name }}</h4>
              <p class="cake-desc">{{ cake.description }}</p>
              <div class="cake-bottom">
                <span class="cake-price">
                  <template v-if="cake.offer_price">
                    <span class="original-price">₹{{ Number(cake.price).toFixed(2) }}</span>
                    <span class="offer-price">₹{{ Number(cake.offer_price).toFixed(2) }}</span>
                  </template>
                  <template v-else>
                    ₹{{ Number(cake.price).toFixed(2) }}
                  </template>
                </span>
                <button class="view-btn" @click="openCakeModal(cake)">View</button>
              </div>
            </div>
          </div>
        </div>
      </section>
      <div v-if="showCakeModal" class="modal-overlay" @click.self="closeCakeModal">
        <div class="modal-content">
          <button class="modal-close" @click="closeCakeModal">&times;</button>
          <img :src="getImageUrl(selectedCake.image)" :alt="selectedCake.name" class="modal-img" />
          <h2 class="modal-title">{{ selectedCake.name }}</h2>
          <div class="modal-price">₹{{ Number(selectedCake.price).toFixed(2) }}</div>
          <div v-if="selectedCake.offer_price" class="modal-offer-price">
            <span class="original-price">₹{{ Number(selectedCake.price).toFixed(2) }}</span>
            <span class="offer-price">₹{{ Number(selectedCake.offer_price).toFixed(2) }}</span>
          </div>
          <p class="modal-desc">{{ selectedCake.description }}</p>
          <button class="add-cart-btn" @click="addToCart(selectedCake)">Add to Cart</button>
        </div>
      </div>
    </template>
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
.homepage-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #fff7f0 0%, #ffe0e9 100%);
  font-family: 'Montserrat', 'Segoe UI', Arial, sans-serif;
}
.main-header {
  background: #fff;
  box-shadow: 0 2px 12px rgba(255,107,53,0.07);
  padding: 0.5rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
}
.header-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2rem;
}
.logo {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  box-shadow: 0 2px 8px rgba(255,107,53,0.12);
}
.brand-title {
  font-size: 2.1rem;
  font-weight: 800;
  color: #23232b;
  margin-left: 1rem;
}
.brand-title .highlight {
  color: #ff6b35;
}
.main-nav ul {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.main-nav li {
  color: #ff6b35;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: color 0.2s;
  padding: 0.3rem 0.7rem;
  border-radius: 6px;
}
.main-nav li:hover {
  background: #ffe0e9;
  color: #23232b;
}
.cart-btn {
  background: #fff7f0;
  border: none;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  font-size: 1.7rem;
  box-shadow: 0 2px 8px rgba(255,107,53,0.07);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}
.cart-btn:hover {
  background: #ffe0e9;
}
.hero-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 2.5rem auto 0 auto;
  padding: 2rem 2rem 0 2rem;
  gap: 2rem;
}
.hero-content {
  flex: 1;
}
.hero-content h2 {
  font-size: 2.5rem;
  font-weight: 900;
  color: #ff6b35;
  margin-bottom: 1rem;
}
.hero-content p {
  font-size: 1.2rem;
  color: #23232b;
  margin-bottom: 2rem;
}
.explore-btn {
  background: #ff6b35;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 0.9rem 2.5rem;
  font-size: 1.1rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s;
}
.explore-btn:hover {
  background: #ff9b6a;
}
.hero-img {
  width: 340px;
  max-width: 40vw;
  border-radius: 18px;
  box-shadow: 0 8px 32px rgba(255,107,53,0.13);
}
@media (max-width: 900px) {
  .hero-section {
    flex-direction: column;
    align-items: flex-start;
    gap: 1.5rem;
  }
  .hero-img {
    width: 100%;
    max-width: 100vw;
    margin-top: 1.5rem;
  }
}
.search-section {
  display: flex;
  justify-content: center;
  margin: 2rem 0 0 0;
}
.search-bar {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(255,107,53,0.07);
  display: flex;
  align-items: center;
  padding: 0.5rem 1.2rem;
  width: 400px;
  max-width: 90vw;
}
.search-bar input {
  border: none;
  outline: none;
  font-size: 1.1rem;
  padding: 0.7rem 1rem;
  flex: 1;
  background: transparent;
}
.search-btn {
  background: none;
  border: none;
  cursor: pointer;
  margin-left: 0.5rem;
  display: flex;
  align-items: center;
}
.cakes-section {
  max-width: 1200px;
  margin: 3rem auto 0 auto;
  padding: 0 2rem;
}
.section-title {
  font-size: 2rem;
  font-weight: 800;
  color: #ff6b35;
  margin-bottom: 2rem;
  text-align: center;
}
.cakes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2.5rem;
}
.cakes-grid.single-cake {
  justify-content: center;
  display: flex;
  grid-template-columns: none;
  gap: 0;
}
.cakes-grid.single-cake .cake-card-new {
  max-width: 350px;
  width: 100%;
}
.cake-card-new {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 16px rgba(255,107,53,0.09);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: box-shadow 0.2s;
  position: relative;
}
.cake-card-new:hover {
  box-shadow: 0 8px 32px rgba(255,107,53,0.18);
}
.cake-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-bottom: 1px solid #ffe0e9;
}
.cake-info {
  padding: 1.2rem 1.2rem 1.5rem 1.2rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.cake-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #23232b;
  margin-bottom: 0.5rem;
}
.cake-desc {
  font-size: 1rem;
  color: #6d6d6d;
  margin-bottom: 1.2rem;
  min-height: 48px;
}
.cake-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.cake-price {
  font-size: 1.1rem;
  color: #ff6b35;
  font-weight: 700;
}
.view-btn {
  background: #ff6b35;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 0.6rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.view-btn:hover {
  background: #ff9b6a;
}
.no-cakes {
  grid-column: 1/-1;
  text-align: center;
  color: #ff6b35;
  font-size: 1.2rem;
  font-weight: 600;
  padding: 2rem 0;
}
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(24,24,27,0.85);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal-content {
  background: #fff;
  border-radius: 18px;
  padding: 2.5rem 2.2rem 2rem 2.2rem;
  min-width: 320px;
  max-width: 95vw;
  box-shadow: 0 8px 32px rgba(255,107,53,0.18);
  color: #23232b;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.modal-close {
  position: absolute;
  top: 12px;
  right: 18px;
  background: none;
  border: none;
  font-size: 2rem;
  color: #ff6b35;
  cursor: pointer;
  z-index: 10;
}
.modal-img {
  width: 220px;
  height: 180px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 1.2rem;
}
.modal-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #ff6b35;
}
.modal-price {
  font-size: 1.2rem;
  color: #ff6b35;
  margin-bottom: 1rem;
}
.modal-desc {
  font-size: 1.08rem;
  color: #23232b;
  margin-bottom: 1.5rem;
  text-align: center;
}
.add-cart-btn {
  background: #ff6b35;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 0.8rem 2.5rem;
  font-size: 1.08rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.add-cart-btn:hover {
  background: #ff9b6a;
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
  box-shadow: 0 8px 32px rgba(255,107,53,0.18);
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
  color: #ff6b35;
  cursor: pointer;
  z-index: 10;
}
@media (max-width: 600px) {
  .header-content, .hero-section, .cakes-section {
    padding: 0 0.5rem;
  }
  .search-bar {
    width: 100%;
    max-width: 100vw;
  }
  .cakes-grid {
    grid-template-columns: 1fr;
    gap: 1.2rem;
  }
  .hero-img {
    width: 100%;
    margin-top: 1rem;
  }
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
.modal-offer-price {
  margin-bottom: 0.5em;
}
</style> 