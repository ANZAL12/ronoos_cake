<template>
  <div class="dashboard">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="logo">
        <div class="logo-icon">
          <img :src="logoUrl" alt="Logo" style="width: 32px; height: 32px;" />
        </div>
        <div class="logo-text">Ronoos Cake</div>
      </div>
      <div class="nav-section">
        <div class="nav-title">Main</div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'dashboard' }" @click="setActiveTab('dashboard')">
            <i data-lucide="layout-dashboard" style="width: 20px; height: 20px;"></i>
            Dashboard
          </a>
        </div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'add-cake' }" @click="setActiveTab('add-cake')">
            <i data-lucide="plus-circle" style="width: 20px; height: 20px;"></i>
            Add Cake
          </a>
        </div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'my-cakes' }" @click="setActiveTab('my-cakes')">
            <i data-lucide="cake" style="width: 20px; height: 20px;"></i>
            My Cakes
          </a>
        </div>
      </div>
      <div class="nav-section">
        <div class="nav-title">Business</div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'orders' }" @click="setActiveTab('orders')">
            <i data-lucide="shopping-bag" style="width: 20px; height: 20px;"></i>
            Orders
          </a>
        </div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'reviews' }" @click="setActiveTab('reviews')">
            <i data-lucide="star" style="width: 20px; height: 20px;"></i>
            Reviews
          </a>
        </div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'payments' }" @click="setActiveTab('payments')">
            <i data-lucide="credit-card" style="width: 20px; height: 20px;"></i>
            Payments
          </a>
        </div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'analytics' }" @click="setActiveTab('analytics')">
            <i data-lucide="bar-chart-3" style="width: 20px; height: 20px;"></i>
            Analytics
          </a>
        </div>
      </div>
      <div class="nav-section">
        <div class="nav-title">Account</div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'profile' }" @click="setActiveTab('profile')">
            <i data-lucide="user" style="width: 20px; height: 20px;"></i>
            Profile
          </a>
        </div>
      </div>
    </div>
    <!-- Main Content -->
    <div class="main-content">
      <div class="top-bar">
        <div class="welcome">
          <h1>Hi, {{ bakerName }}! ☀️</h1>
          <p>Let's bake some magic today</p>
        </div>
        <div class="user-info">
          <div class="user-details">
            <h3>{{ bakerName }}</h3>
            <span>Master Baker</span>
          </div>
          <div class="user-avatar">{{ bakerInitials }}</div>
        </div>
      </div>
      <div class="content">
        <transition name="fade" mode="out-in">
          <!-- Dashboard Content -->
          <div v-if="activeTab === 'dashboard'" key="dashboard">
            <div class="quick-actions">
              <button class="action-btn" @click="setActiveTab('add-cake')">
                <i data-lucide="plus" style="width: 18px; height: 18px;"></i>
                Create New Cake
              </button>
              <button class="action-btn" @click="setActiveTab('orders')">
                <i data-lucide="shopping-bag" style="width: 18px; height: 18px;"></i>
                View Orders
              </button>
              <button class="action-btn" @click="setActiveTab('analytics')">
                <i data-lucide="trending-up" style="width: 18px; height: 18px;"></i>
                Analytics
              </button>
            </div>
            <div class="dashboard-grid">
              <div class="metric-card">
                <div class="metric-icon">
                  <i data-lucide="cake" style="color: white; width: 24px; height: 24px;"></i>
                </div>
                <div class="metric-value">{{ stats.totalCakes }}</div>
                <div class="metric-label">Active Cakes</div>
              </div>
              <div class="metric-card">
                <div class="metric-icon">
                  <i data-lucide="shopping-cart" style="color: white; width: 24px; height: 24px;"></i>
                </div>
                <div class="metric-value">{{ stats.totalOrders }}</div>
                <div class="metric-label">Total Orders</div>
              </div>
              <div class="metric-card">
                <div class="metric-icon">
                  <i data-lucide="dollar-sign" style="color: white; width: 24px; height: 24px;"></i>
                </div>
                <div class="metric-value">${{ stats.totalRevenue }}</div>
                <div class="metric-label">This Month</div>
              </div>
              <div class="metric-card">
                <div class="metric-icon">
                  <i data-lucide="star" style="color: white; width: 24px; height: 24px;"></i>
                </div>
                <div class="metric-value">{{ stats.averageRating }}</div>
                <div class="metric-label">Average Rating</div>
              </div>
            </div>
            <div class="recent-activity">
              <div class="section-header">
                <i data-lucide="activity" style="width: 24px; height: 24px;"></i>
                <h3 class="section-title">Recent Activity</h3>
              </div>
              <div class="activity-list">
                <div class="activity-item" v-for="activity in recentActivity" :key="activity.id">
                  <div class="activity-icon">
                    <i :data-lucide="activity.icon" style="color: white; width: 20px; height: 20px;"></i>
                  </div>
                  <div class="activity-details">
                    <div class="activity-title">{{ activity.title }}</div>
                    <div class="activity-desc">{{ activity.description }}</div>
                  </div>
                  <div class="activity-time">{{ activity.time }}</div>
                </div>
              </div>
            </div>
          </div>
          <!-- Orders Content -->
          <div v-else-if="activeTab === 'orders'" key="orders">
            <div class="orders-header">
              <button class="action-btn primary" @click="showOrderModal = true">
                <i data-lucide="plus"></i>
                Add Order
              </button>
            </div>
            <div v-if="orders.length" class="orders-list">
              <div class="orders-table-header">
                <div class="orders-col customer">Customer</div>
                <div class="orders-col cake">Cake</div>
                <div class="orders-col price">Price</div>
                <div class="orders-col notes">Notes</div>
              </div>
              <div class="order-item" v-for="(order, idx) in orders" :key="idx">
                <div class="orders-col customer order-customer">{{ order.customer }}</div>
                <div class="orders-col cake order-cake">{{ order.cake }}</div>
                <div class="orders-col price order-price">${{ order.price }}</div>
                <div class="orders-col notes order-notes">{{ order.notes }}</div>
              </div>
            </div>
            <!-- Modal -->
            <div v-if="showOrderModal" class="modal-overlay" @click.self="showOrderModal = false">
              <div class="modal">
                <h2>Add Order</h2>
                <form @submit.prevent="addOrder">
                  <div class="form-group">
                    <label>Customer Name</label>
                    <input v-model="orderForm.customer" type="text" required />
                  </div>
                  <div class="form-group">
                    <label>Cake Name</label>
                    <input v-model="orderForm.cake" type="text" required />
                  </div>
                  <div class="form-group">
                    <label>Price</label>
                    <input v-model.number="orderForm.price" type="number" min="0" required />
                  </div>
                  <div class="form-group">
                    <label>Notes</label>
                    <textarea v-model="orderForm.notes" rows="2" placeholder="Optional"></textarea>
                  </div>
                  <div class="modal-actions">
                    <button type="button" class="action-btn secondary" @click="showOrderModal = false">Cancel</button>
                    <button type="submit" class="action-btn primary">Add</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <!-- Profile Content -->
          <div v-else-if="activeTab === 'profile'" key="profile">
            <div class="content">
              <h2 class="section-title">Baker Profile</h2>
              <div class="profile-details">
                <img :src="logoUrl" alt="Logo" style="width: 64px; height: 64px; border-radius: 12px; margin-bottom: 16px;" />
                <p><strong>Name:</strong> {{ bakerName }}</p>
                <p><strong>Email:</strong> baker@example.com</p>
                <p><strong>Role:</strong> Master Baker</p>
                <input type="file" @change="onLogoChange" accept="image/*" />
                <button class="action-btn">Edit Profile</button>
              </div>
            </div>
          </div>
          <!-- Other Content -->
          <div v-else key="other" class="coming-soon">
            <div class="coming-soon-icon">
              <i data-lucide="hammer" style="color: white; width: 40px; height: 40px;"></i>
            </div>
            <h2>{{ getTabTitle(activeTab) }}</h2>
            <p>This amazing feature is being crafted with love. Stay tuned!</p>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'

const bakerName = ref('Anzal')
const bakerInitials = computed(() => bakerName.value.split(' ').map(n => n[0]).join(''))

const activeTab = ref('dashboard')
const stats = ref({
  totalCakes: 47,
  totalOrders: 156,
  totalRevenue: 3248,
  averageRating: 4.8
})
const recentActivity = ref([
  { id: 1, icon: 'shopping-cart', title: 'New Order Received', description: 'Chocolate Birthday Cake - John Doe', time: '2 mins ago' },
  { id: 2, icon: 'star', title: 'New Review', description: '⭐⭐⭐⭐⭐ "Amazing red velvet cake!"', time: '15 mins ago' },
  { id: 3, icon: 'plus-circle', title: 'Cake Added', description: 'Strawberry Cheesecake added to menu', time: '1 hour ago' },
  { id: 4, icon: 'credit-card', title: 'Payment Received', description: '$85 for Wedding Cake order', time: '2 hours ago' },
  { id: 5, icon: 'truck', title: 'Order Delivered', description: 'Vanilla Cake delivered successfully', time: '3 hours ago' }
])

const showOrderModal = ref(false)
const orderForm = ref({ customer: '', cake: '', price: '', notes: '' })
const orders = ref([])
const logoUrl = ref('/default-logo.png')

function setActiveTab(tab) {
  activeTab.value = tab
  nextTick(() => {
    if (window.lucide) window.lucide.createIcons()
  })
}
function getTabTitle(tab) {
  const titles = {
    'add-cake': 'Add New Cake',
    'my-cakes': 'My Cake Collection',
    'orders': 'Order Management',
    'reviews': 'Customer Reviews',
    'payments': 'Payment History',
    'analytics': 'Analytics & Reports',
    'profile': 'Baker Profile'
  }
  return titles[tab] || 'Dashboard'
}

function addOrder() {
  orders.value.push({ ...orderForm.value })
  orderForm.value = { customer: '', cake: '', price: '', notes: '' }
  showOrderModal.value = false
}

function onLogoChange(event) {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = e => {
      logoUrl.value = e.target.result // This sets the logo to the uploaded image (base64)
    }
    reader.readAsDataURL(file)
  }
}

onMounted(() => {
  if (window.lucide) window.lucide.createIcons()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body {
    margin: 0 !important;
    padding: 0 !important;
    width: 100vw;
    height: 100vh;
    min-height: 100vh;
    overflow: hidden !important;
    background: #222 !important;
}

.dashboard {
    display: flex;
    height: 100vh;
    min-height: 100vh;
    width: 100vw;
    margin: 0 !important;
    padding: 0 !important;
    box-sizing: border-box;
    overflow: hidden;
    background: #18181b;
}

body {
    font-family: 'Inter', sans-serif;
    color: #fff;
    height: 100vh;
    min-height: 100vh;
    width: 100vw;
    background: #aaa6a600 !important;
    overflow: hidden !important;
}

.dashboard::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: radial-gradient(circle at 20% 50%, #ff6b35 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, #f7931e 0%, transparent 50%),
                radial-gradient(circle at 40% 80%, #ff006e 0%, transparent 50%);
    opacity: 0.1;
    z-index: -1;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.sidebar {
    width: 280px;
    min-width: 220px;
    max-width: 320px;
    background: #1e1e23;
    backdrop-filter: blur(20px);
    border-right: 1px solid #23232b;
    padding: 30px 20px;
    transition: all 0.3s ease;
    box-sizing: border-box;
    height: 100vh;
    overflow-y: auto;
    overflow-x: hidden;
    scrollbar-width: thin;
    scrollbar-color: #444 #23232b;
}

.logo {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 50px;
    padding: 15px;
    background: linear-gradient(135deg, #ff6b35, #f7931e);
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(255, 107, 53, 0.3);
}

.logo-icon {
    width: 45px;
    height: 45px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.logo-text {
    font-size: 22px;
    font-weight: 700;
    color: white;
}

.nav-section {
    margin-bottom: 35px;
}

.nav-title {
    font-size: 12px;
    font-weight: 600;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 15px;
    padding-left: 10px;
}

.nav-item {
    margin-bottom: 5px;
}

.nav-link {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 15px 20px;
    border-radius: 15px;
    text-decoration: none;
    color: #cfcfd6;
    transition: all 0.3s ease;
    cursor: pointer;
    font-weight: 500;
    position: relative;
    overflow: hidden;
}

.nav-link::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.5s ease;
}

.nav-link:hover::before {
    left: 100%;
}

.nav-link:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    transform: translateX(5px);
}

.nav-link.active {
    background: linear-gradient(135deg, #ff6b35, #f7931e);
    color: #fff;
    box-shadow: 0 15px 30px rgba(255, 107, 53, 0.4);
}

.main-content {
    flex: 1 1 0%;
    min-width: 0;
    padding: 30px;
    background: #23232b;
    box-sizing: border-box;
    height: 100vh;
    overflow-y: auto;
    overflow-x: hidden;
    scrollbar-width: thin;
    scrollbar-color: #444 #23232b;
}

.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 40px;
    background: #23232b;
    backdrop-filter: blur(20px);
    padding: 20px 30px;
    border-radius: 20px;
    border: 1px solid #24242e;
}

.welcome {
    flex: 1;
}

.welcome h1 {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 8px;
    background: linear-gradient(135deg, #ff6b35, #f7931e, #ff006e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.welcome p {
    color: rgba(255, 255, 255, 0.7);
    font-size: 16px;
}

.user-info {
    display: flex;
    align-items: center;
    gap: 15px;
}

.user-avatar {
    width: 55px;
    height: 55px;
    background: linear-gradient(135deg, #ff006e, #8338ec);
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 18px;
    box-shadow: 0 15px 30px rgba(255, 0, 110, 0.3);
}

.user-details h3 {
    font-weight: 600;
    margin-bottom: 4px;
}

.user-details span {
    color: rgba(255, 255, 255, 0.6);
    font-size: 14px;
}

.content {
    background: #23232b;
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 40px;
    border: 1px solid #24242e;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
}

.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    margin-bottom: 40px;
}

.metric-card {
    background: #24242e;
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid #23232b;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #ff6b35, #f7931e, #ff006e, #8338ec);
}

.metric-card:hover {
    background: #282834;
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5);
}

.metric-header {
    display: flex;
    justify-content: between;
    align-items: center;
    margin-bottom: 20px;
}

.metric-icon {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #ff6b35, #f7931e);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    box-shadow: 0 15px 30px rgba(255, 107, 53, 0.3);
}

.metric-value {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 8px;
    background: linear-gradient(135deg, #fff, rgba(255, 255, 255, 0.8));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.metric-label {
    color: #b0b0b8;
    font-size: 14px;
    font-weight: 500;
}

.recent-activity {
    margin-top: 40px;
}

.section-header {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 24px;
    font-weight: 600;
}

.activity-list {
    background: #23232b;
    border-radius: 20px;
    border: 1px solid #24242e;
    overflow: hidden;
}

.activity-item {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 20px 25px;
    border-bottom: 1px solid #24242e;
    transition: all 0.3s ease;
    background: transparent;
}

.activity-item:hover {
    background: #24242e;
}

.activity-item:last-child {
    border-bottom: none;
}

.activity-icon {
    width: 45px;
    height: 45px;
    background: linear-gradient(135deg, #8338ec, #ff006e);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.activity-details {
    flex: 1;
}

.activity-title {
    font-weight: 600;
    margin-bottom: 4px;
}

.activity-desc {
    color: #b0b0b8;
    font-size: 14px;
}

.activity-time {
    color: #b0b0b8;
    font-size: 12px;
}

.quick-actions {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.action-btn {
    background: linear-gradient(135deg, #ff6b35, #f7931e);
    border: none;
    color: white;
    padding: 18px 25px;
    border-radius: 15px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 12px;
    justify-content: center;
    font-size: 15px;
}

.action-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 20px 40px rgba(255, 107, 53, 0.4);
    background: linear-gradient(135deg, #f7931e, #ff006e);
}

.fade-enter-active, .fade-leave-active {
    transition: all 0.4s ease;
}

.fade-enter-from, .fade-leave-to {
    opacity: 0;
    transform: translateY(20px);
}

.coming-soon {
    text-align: center;
    padding: 80px 20px;
    background: #23232b;
    border-radius: 20px;
}

.coming-soon-icon {
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, #ff6b35, #f7931e);
    border-radius: 25px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 30px;
    box-shadow: 0 25px 50px rgba(255, 107, 53, 0.3);
}

.coming-soon h2 {
    font-size: 28px;
    margin-bottom: 15px;
    background: linear-gradient(135deg, #fff, rgba(255, 255, 255, 0.8));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.coming-soon p {
    color: #b0b0b8;
    font-size: 16px;
}

@media (max-width: 768px) {
    .dashboard {
        flex-direction: column;
    }
    .sidebar {
        width: 100%;
        padding: 20px;
    }
    .main-content {
        padding: 20px;
    }
    .top-bar {
        flex-direction: column;
        gap: 20px;
        text-align: center;
    }
    .dashboard-grid {
        grid-template-columns: 1fr;
    }
}

.sidebar::-webkit-scrollbar, .main-content::-webkit-scrollbar {
  width: 7px;
  background: #23232b;
}
.sidebar::-webkit-scrollbar-thumb, .main-content::-webkit-scrollbar-thumb {
  background: #444;
  border-radius: 6px;
}
.sidebar::-webkit-scrollbar-thumb:hover, .main-content::-webkit-scrollbar-thumb:hover {
  background: #666;
}

.orders-header {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 24px;
}
.orders-list {
  display: flex;
  flex-direction: column;
  gap: 0;
}
.orders-table-header {
  display: flex;
  background: #18181b;
  border-radius: 8px 8px 0 0;
  border: 1px solid #24242e;
  border-bottom: none;
  color: #b0b0b8;
  font-weight: 700;
  font-size: 1rem;
  padding: 12px 0 12px 0;
  margin-bottom: 0;
}
.orders-col {
  flex: 1 1 0;
  padding: 0 12px;
  display: flex;
  align-items: center;
  min-width: 0;
  word-break: break-word;
}
.orders-col.customer { min-width: 120px; max-width: 200px; }
.orders-col.cake { min-width: 120px; max-width: 200px; }
.orders-col.price { min-width: 80px; max-width: 120px; justify-content: flex-start; }
.orders-col.notes { min-width: 120px; max-width:auto; }
.order-item {
  display: flex;
  background: #23232b;
  border-left: 1px solid #24242e;
  border-right: 1px solid #24242e;
  border-bottom: 1px solid #24242e;
  border-radius: 0;
  color: #fff;
  padding: 14px 0;
  gap: 0;
}
.order-item:last-child {
  border-radius: 0 0 8px 8px;
}
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(24,24,27,0.85);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal {
  background: #18181b;
  border-radius: 18px;
  padding: 32px 28px 24px 28px;
  min-width: 320px;
  max-width: 95vw;
  box-shadow: 0 8px 32px rgba(0,0,0,0.45);
  border: 1px solid #23232b;
  color: #fff;
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.modal h2 {
  margin-bottom: 12px;
  font-size: 1.3rem;
  color: #ff6b35;
  font-weight: 700;
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 12px;
}
.form-group label {
  font-size: 0.98rem;
  color: #f7931e;
  font-weight: 600;
}
.form-group input,
.form-group textarea {
  background: #23232b;
  border: 1px solid #24242e;
  border-radius: 8px;
  color: #fff;
  padding: 10px 12px;
  font-size: 1rem;
  outline: none;
  transition: border 0.2s;
}
.form-group input:focus,
.form-group textarea:focus {
  border: 1.5px solid #ff6b35;
}
.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 10px;
}
.profile-details {
  margin-top: 30px;
  background: #24242e;
  border-radius: 16px;
  padding: 30px;
  box-shadow: 0 10px 24px rgba(255, 107, 53, 0.08);
  color: #fff;
  font-size: 1.1rem;
}
.profile-details p {
  margin-bottom: 14px;
}
</style> 