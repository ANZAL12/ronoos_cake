<template>
  <div class="dashboard">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="logo">
        <div class="logo-icon">
          <i data-lucide="cake" style="color: white; width: 24px; height: 24px;"></i>
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
          <h1>Good morning, {{ bakerName }}! ☀️</h1>
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

const bakerName = ref('Sarah Chen')
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
</style> 