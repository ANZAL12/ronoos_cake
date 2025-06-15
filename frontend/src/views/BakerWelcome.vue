<template>
  <div class="dashboard">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="logo">
        <div class="logo-icon">
          <!-- Logo icon removed -->
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
          <a class="nav-link" :class="{ active: activeTab === 'view-cakes' }" @click="setActiveTab('view-cakes')">
            <i data-lucide="eye" style="width: 20px; height: 20px;"></i>
            View Cakes
          </a>
        </div>
        <div class="nav-item">
          <a class="nav-link" :class="{ active: activeTab === 'all-orders' }" @click="setActiveTab('all-orders')">
            <i data-lucide="list" style="width: 20px; height: 20px;"></i>
            All Orders
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
      <div class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'messages' }" @click="setActiveTab('messages')">
          <i data-lucide="mail" style="width: 20px; height: 20px;"></i>
          Messages
        </a>
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
              <div class="metric-card">
                <div class="metric-icon">
                  <i data-lucide="mail" style="color: white; width: 24px; height: 24px;"></i>
                </div>
                <div class="metric-value">{{ stats.totalMessages }}</div>
                <div class="metric-label">Messages</div>
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
                <div class="orders-col customer">Order ID</div>
                <div class="orders-col customer">Customer</div>
                <div class="orders-col cake">Items</div>
                <div class="orders-col price">Total Amount</div>
                <div class="orders-col notes">Status</div>
              </div>
              <div class="order-item" v-for="(order, idx) in orders" :key="idx">
                <div class="orders-col customer order-customer">#{{ order.id }}</div>
                <div class="orders-col customer order-customer">
                  <div class="customer-details">
                    <div class="customer-name">
                      {{ order.customer ? 
                        (order.customer.first_name || '') + 
                        (order.customer.last_name ? ' ' + order.customer.last_name : '') || 
                        order.customer.username : 
                        order.customer_name 
                      }}
                    </div>
                    <div class="customer-contact">
                      {{ order.customer ? order.customer.mobile_number : order.mobile_number }}
                    </div>
                    <div class="customer-location" v-if="order.location">
                      {{ order.location }}
                    </div>
                  </div>
                </div>
                <div class="orders-col cake order-cake">
                  <div v-for="item in order.items" :key="item.cake">
                    Cake #{{ item.cake }} ({{ item.quantity }}x)
                  </div>
                </div>
                <div class="orders-col price order-price">${{ order.total_amount }}</div>
                <div class="orders-col notes order-notes">
                  <span :class="['status-badge', order.status]">{{ order.status }}</span>
                  <select v-model="order.newStatus" @change="updateOrderStatus(order)" style="margin-left: 10px;">
                    <option disabled value="">Change status</option>
                    <option v-for="status in ORDER_STATUSES" :key="status.value" :value="status.value">
                      {{ status.label }}
                    </option>
                  </select>
                </div>
                <div class="orders-col">
                  <button @click="viewCustomerDetails(order)">View</button>
                </div>
              </div>
            </div>
            <!-- Modal -->
            <div v-if="showOrderModal" class="modal-overlay" @click.self="showOrderModal = false">
              <div class="modal">
                <h2>Add New Order</h2>
                <form @submit.prevent="addOrder">
                  <div class="form-group">
                    <label>Customer Details</label>
                    <div class="customer-form-grid">
                      <div class="form-group">
                        <label>Search Existing Customer (Optional)</label>
                        <div class="search-container">
                          <select v-model="orderForm.customer_id" class="customer-input" @change="onCustomerSelect">
                            <option value="">Select a customer</option>
                            <option v-for="customer in allCustomers" :key="customer.id" :value="customer.id">
                              {{ customer.username }} ({{ customer.mobile_number }})
                            </option>
                          </select>
                        </div>
                      </div>
                      <div class="form-group">
                        <label>Customer Name</label>
                        <input 
                          v-model="orderForm.customer_name" 
                          type="text" 
                          placeholder="Enter customer name" 
                          class="customer-input"
                          :readonly="!!orderForm.customer_id"
                        />
                      </div>
                      <div class="form-group">
                        <label>Mobile Number</label>
                        <input 
                          v-model="orderForm.mobile_number" 
                          type="tel" 
                          placeholder="10-digit mobile number" 
                          required 
                          class="customer-input"
                          :readonly="!!orderForm.customer_id"
                        />
                      </div>
                      <div class="form-group">
                        <label>Location</label>
                        <div class="location-input-container">
                          <input 
                            v-model="orderForm.location" 
                            type="text" 
                            placeholder="Delivery Location" 
                            required 
                            class="customer-input"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label>Order Items</label>
                    <div v-for="(item, index) in orderForm.items" :key="index" class="order-item-form">
                      <div class="item-row">
                        <select v-model="item.cake" @change="updateItemPrice(index)" required class="cake-select">
                          <option value="">Select a Cake</option>
                          <option v-for="cake in availableCakes" :key="cake.id" :value="cake.id">
                            {{ cake.name }} - ${{ cake.price }}
                          </option>
                        </select>
                        <input 
                          v-model.number="item.quantity" 
                          type="number" 
                          min="1" 
                          placeholder="Qty" 
                          required 
                          @input="calculateTotal"
                          class="quantity-input"
                        />
                        <input 
                          v-model.number="item.price" 
                          type="number" 
                          step="0.01" 
                          placeholder="Price" 
                          required 
                          @input="calculateTotal"
                          class="price-input"
                        />
                        <button 
                          type="button" 
                          class="remove-item" 
                          @click="orderForm.items.splice(index, 1); calculateTotal()" 
                          v-if="orderForm.items.length > 1"
                        >
                          <i data-lucide="x"></i>
                        </button>
                      </div>
                    </div>
                    <button type="button" class="add-item-btn" @click="orderForm.items.push({ cake: '', quantity: 1, price: '' })">
                      <i data-lucide="plus"></i> Add Another Item
                    </button>
                  </div>
                  <div class="form-group">
                    <label>Total Amount</label>
                    <input 
                      v-model.number="orderForm.total_amount" 
                      type="number" 
                      step="0.01" 
                      placeholder="Total Amount" 
                      readonly 
                      class="total-input"
                    />
                  </div>
                  <div class="form-group">
                    <label>Status</label>
                    <select v-model="orderForm.status" class="status-select">
                      <option value="pending">Pending</option>
                      <option value="completed">Completed</option>
                      <option value="cancelled">Cancelled</option>
                    </select>
                  </div>
                  <div class="modal-actions">
                    <button type="button" class="action-btn secondary" @click="showOrderModal = false">Cancel</button>
                    <button type="submit" class="action-btn primary">Create Order</button>
                  </div>
                </form>
              </div>
            </div>
            <!-- Customer Details Modal -->
            <div v-if="showCustomerModal" class="modal-overlay" @click.self="showCustomerModal = false">
              <div class="modal">
                <h2>Delivery Details</h2>
                <template v-if="selectedOrder.delivery">
                  <p><strong>Recipient Name:</strong> {{ selectedOrder.delivery.customer_name }}</p>
                  <p><strong>Mobile:</strong> {{ selectedOrder.delivery.mobile_number }}</p>
                  <p><strong>Location:</strong> {{ selectedOrder.delivery.location }}</p>
                  <p><strong>Address:</strong> {{ selectedOrder.delivery.address }}</p>
                </template>
                <template v-else>
                  <p>No delivery details available.</p>
                </template>
                <button @click="showCustomerModal = false">Close</button>
              </div>
            </div>
          </div>
          <!-- Profile Content -->
          <div v-else-if="activeTab === 'profile'" key="profile">
            <div class="content">
              <h2 class="section-title">Baker Profile</h2>
              <div class="profile-details">
                <!-- Profile logo removed -->
                <p><strong>Name:</strong> {{ bakerName }}</p>
                <p><strong>Email:</strong> baker@example.com</p>
                <p><strong>Role:</strong> Master Baker</p>
                <!-- Logo upload removed -->
                <button class="action-btn">Edit Profile</button>
              </div>
            </div>
          </div>
          <!-- Add Cake Tab -->
          <div v-else-if="activeTab === 'add-cake'" key="add-cake">
            <CakesView :token="token" />
          </div>
          <!-- View Cakes Tab -->
          <div v-else-if="activeTab === 'view-cakes'" key="view-cakes">
            <ViewCake :token="token" />
          </div>
          <!-- Messages Content -->
          <div v-else-if="activeTab === 'messages'" key="messages">
            <div class="messages-section">
              <h2>Customer Messages</h2>
              <div v-if="messages.length === 0" class="no-messages">No messages yet.</div>
              <div v-for="msg in messages" :key="msg.id" class="message-card">
                <div class="message-header">
                  <span class="message-name">{{ msg.name }}</span>
                  <span class="message-email">{{ msg.email }}</span>
                  <span class="message-date">{{ new Date(msg.created_at).toLocaleString() }}</span>
                </div>
                <div class="message-body">{{ msg.message }}</div>
              </div>
            </div>
          </div>
          <!-- All Orders Content -->
          <div v-else-if="activeTab === 'all-orders'" key="all-orders">
            <div class="orders-header">
              <h2>All Orders (Baker View)</h2>
            </div>
            <div v-if="allOrders.length" class="orders-list">
              <div class="orders-table-header">
                <div class="orders-col customer">Order ID</div>
                <div class="orders-col customer">Customer</div>
                <div class="orders-col cake">Items</div>
                <div class="orders-col price">Total Amount</div>
                <div class="orders-col notes">Status</div>
                <div class="orders-col notes">Delivery</div>
              </div>
              <div class="order-item" v-for="order in allOrders" :key="order.id">
                <div class="orders-col customer order-customer">#{{ order.id }}</div>
                <div class="orders-col customer order-customer">
                  <div class="customer-details">
                    <div class="customer-name">
                      {{ order.customer_name || (order.customer ? ((order.customer.first_name || '') + (order.customer.last_name ? ' ' + order.customer.last_name : '')) : '') || (order.customer ? order.customer.username : '') }}
                    </div>
                    <div class="customer-contact">
                      {{ order.customer && order.customer.mobile_number ? order.customer.mobile_number : order.mobile_number }}
                    </div>
                    <div class="customer-location" v-if="order.location">
                      {{ order.location }}
                    </div>
                  </div>
                </div>
                <div class="orders-col cake order-cake">
                  <div v-for="item in order.items" :key="item.cake">
                    Cake #{{ item.cake }} ({{ item.quantity }}x)
                  </div>
                </div>
                <div class="orders-col price order-price">${{ order.total_amount }}</div>
                <div class="orders-col notes order-notes">
                  <span :class="['status-badge', order.status]">{{ order.status }}</span>
                </div>
                <div class="orders-col notes">
                  <div v-if="order.delivery">
                    <div><strong>Name:</strong> {{ order.delivery.customer_name }}</div>
                    <div><strong>Mobile:</strong> {{ order.delivery.mobile_number }}</div>
                    <div><strong>Location:</strong> {{ order.delivery.location }}</div>
                    <div><strong>Address:</strong> {{ order.delivery.address }}</div>
                  </div>
                  <div v-else>
                    <span>No delivery details</span>
                  </div>
                </div>
              </div>
            </div>
            <div v-else class="no-messages">No orders found.</div>
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
import { ref, computed, onMounted, nextTick, onUnmounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import CakesView from './CakesView.vue'
import ViewCake from './ViewCake.vue'

const route = useRoute()
const router = useRouter()

const bakerName = ref('Anzal')
const bakerInitials = computed(() => bakerName.value.split(' ').map(n => n[0]).join(''))

const activeTab = ref(route.query.tab || 'dashboard')
const stats = ref({
  totalCakes: 0,
  totalOrders: 156,
  totalRevenue: 3248,
  averageRating: 4.8,
  totalMessages: 0
})
const recentActivity = ref([])

const showOrderModal = ref(false)
const orderForm = ref({
  customer_id: '',
  customer_name: '',
  mobile_number: '',
  items: [{ cake: '', quantity: 1, price: '' }],
  total_amount: '',
  status: 'pending',
  location: ''
})
const orders = ref([])
const token = ref(localStorage.getItem('access_token') || "")
const messages = ref([])
const messagesLoaded = ref(false)
const availableCakes = ref([])
const allCustomers = ref([])
const ORDER_STATUSES = [
  { value: 'pending', label: 'Pending' },
  { value: 'processing', label: 'Processing' },
  { value: 'completed', label: 'Completed' },
  { value: 'cancelled', label: 'Cancelled' }
]
const showCustomerModal = ref(false)
const selectedOrder = ref(null)
const allOrders = ref([])
let messageInterval = null
let ordersInterval = null

async function fetchActiveCakesCount() {
  try {
    const res = await fetch('/api/v1/cakes/active/', {
      headers: { Authorization: `Bearer ${token.value}` }
    });
    if (res.ok) {
      const data = await res.json();
      stats.value.totalCakes = data.count;
    }
  } catch (e) { /* handle error if needed */ }
}

function fetchMessages(force = false) {
  if (messagesLoaded.value && !force) return;
  const token = localStorage.getItem('access_token')
  fetch('http://localhost:8000/api/v1/message/list/', {
    headers: { Authorization: `Bearer ${token}` }
  })
    .then(res => res.json())
    .then(data => {
      console.log('Fetched messages:', data)
      if (Array.isArray(data)) {
        messages.value = data
      } else if (data && Array.isArray(data.messages)) {
        messages.value = data.messages
      } else {
        messages.value = []
      }
      messagesLoaded.value = true
      stats.value.totalMessages = messages.value.length
      if (messages.value.length > 0) {
        const messageActivities = messages.value.slice(0, 5).map(msg => ({
          id: 'msg-' + msg.id,
          icon: 'mail',
          title: 'New Message',
          description: `From ${msg.name}: "${msg.message.substring(0, 40)}${msg.message.length > 40 ? '...' : ''}"`,
          time: new Date(msg.created_at).toLocaleString()
        }))
        recentActivity.value = [
          ...messageActivities,
          ...recentActivity.value.filter(act => !String(act.id).startsWith('msg-'))
        ].slice(0, 10)
      }
    })
    .catch((err) => {
      console.error('Error fetching messages:', err)
      messages.value = []
      messagesLoaded.value = false
    })
}

function fetchRecentActivity() {
  const token = localStorage.getItem('access_token')
  
  fetch('http://localhost:8000/api/v1/orders/', {
    headers: { Authorization: `Bearer ${token}` }
  })
    .then(res => {
      if (!res.ok) {
        throw new Error('Failed to fetch orders');
      }
      return res.json();
    })
    .then(orders => {
      // Transform orders into activity items
      const orderActivities = orders.slice(0, 5).map(order => ({
        id: `order-${order.id}`,
        icon: 'shopping-bag',
        title: 'New Order',
        description: `Order #${order.id} - ${order.items.length} item(s) - $${order.total_amount}`,
        time: new Date(order.created_at).toLocaleString()
      }));

      // Add a welcome message if there are no orders
      if (orderActivities.length === 0) {
        orderActivities.push({
          id: 'welcome',
          icon: 'cake',
          title: 'Welcome to Ronoos Cake',
          description: 'Start managing your cake orders and business',
          time: new Date().toLocaleString()
        });
      }

      recentActivity.value = orderActivities;
    })
    .catch((error) => {
      console.error('Error fetching recent activity:', error);
      // Provide default activity data when API fails
      recentActivity.value = [
        {
          id: 'default-1',
          icon: 'cake',
          title: 'Welcome to Ronoos Cake',
          description: 'Start managing your cake orders and business',
          time: new Date().toLocaleString()
        },
        {
          id: 'default-2',
          icon: 'shopping-bag',
          title: 'Ready to Take Orders',
          description: 'Your dashboard is set up and ready to go',
          time: new Date().toLocaleString()
        }
      ];
    });
}

async function fetchOrders() {
  try {
    console.log('Fetching orders...');
    const response = await fetch('http://localhost:8000/api/v1/orders/', {
      headers: { Authorization: `Bearer ${token.value}` }
    });
    console.log('Orders response status:', response.status);
    if (response.ok) {
      const data = await response.json();
      console.log('Fetched orders:', data);
      orders.value = data.map(order => ({
        ...order,
        newStatus: '',
        // Ensure these fields are available for both types of orders
        customer_name: order.customer_name || (order.customer ? order.customer.username : ''),
        mobile_number: order.mobile_number || (order.customer ? order.customer.mobile_number : ''),
        location: order.location || ''
      }));
      // Update stats with new order count
      stats.value.totalOrders = data.length;
      // Update total revenue
      stats.value.totalRevenue = data.reduce((sum, order) => sum + parseFloat(order.total_amount), 0).toFixed(2);
    } else {
      console.error('Failed to fetch orders:', await response.text());
    }
  } catch (error) {
    console.error('Error fetching orders:', error);
  }
}

async function fetchAvailableCakes() {
  try {
    const response = await fetch('http://localhost:8000/api/v1/cakes/', {
      headers: { Authorization: `Bearer ${token.value}` }
    });
    if (response.ok) {
      const data = await response.json();
      availableCakes.value = data;
    }
  } catch (error) {
    console.error('Error fetching cakes:', error);
  }
}

function updateItemPrice(index) {
  const item = orderForm.value.items[index];
  const selectedCake = availableCakes.value.find(cake => cake.id === item.cake);
  if (selectedCake) {
    item.price = selectedCake.price;
    calculateTotal();
  }
}

function calculateTotal() {
  orderForm.value.total_amount = orderForm.value.items.reduce((sum, item) => {
    return sum + (parseFloat(item.price || 0) * item.quantity);
  }, 0).toFixed(2);
}

function setActiveTab(tab) {
  activeTab.value = tab
  router.replace({ query: { ...route.query, tab } })
  if (tab === 'dashboard') {
    fetchActiveCakesCount();
    fetchRecentActivity();
  }
  if (tab === 'orders') {
    fetchOrders();
    if (!ordersInterval) {
      ordersInterval = setInterval(fetchOrders, 10000);
    }
  } else {
    if (ordersInterval) {
      clearInterval(ordersInterval);
      ordersInterval = null;
    }
  }
  if (tab === 'all-orders') {
    fetchAllOrders();
  }
  if (tab === 'messages') {
    fetchMessages(true)
    if (!messageInterval) {
      messageInterval = setInterval(() => fetchMessages(true), 30000)
    }
  } else {
    if (messageInterval) {
      clearInterval(messageInterval)
      messageInterval = null
    }
  }
  nextTick(() => {
    if (window.lucide) window.lucide.createIcons()
  })
}

// Watch for route changes (e.g., browser back/forward)
watch(() => route.query.tab, (newTab) => {
  if (newTab) activeTab.value = newTab
})

// Watch for modal opening
watch(showOrderModal, (newValue) => {
  if (newValue) {
    fetchAllCustomers();
    fetchAvailableCakes();
  }
});

function getTabTitle(tab) {
  const titles = {
    'add-cake': 'Add New Cake',
    'my-cakes': 'My Cake Collection',
    'orders': 'Order Management',
    'reviews': 'Customer Reviews',
    'payments': 'Payment History',
    'analytics': 'Analytics & Reports',
    'profile': 'Baker Profile',
    'view-cakes': 'View Cakes'
  }
  return titles[tab] || 'Dashboard'
}

async function fetchAllCustomers() {
  try {
    const response = await fetch('http://localhost:8000/api/v1/customers/', {
      headers: {
        Authorization: `Bearer ${token.value}`,
        'Content-Type': 'application/json'
      }
    });
    if (response.ok) {
      allCustomers.value = await response.json();
    } else {
      allCustomers.value = [];
    }
  } catch (error) {
    allCustomers.value = [];
    console.error('Error fetching all customers:', error);
  }
}

function onCustomerSelect() {
  const selected = allCustomers.value.find(c => c.id === orderForm.value.customer_id);
  if (selected) {
    orderForm.value.customer_name = selected.username;
    orderForm.value.mobile_number = selected.mobile_number;
  } else {
    orderForm.value.customer_name = '';
    orderForm.value.mobile_number = '';
  }
}

async function addOrder() {
  try {
    const orderData = {
      items: orderForm.value.items.map(item => ({
        cake: item.cake,
        quantity: item.quantity
      }))
    };

    // Add customer details if manually entered
    if (!orderForm.value.customer_id) {
      orderData.customer_name = orderForm.value.customer_name;
      orderData.mobile_number = orderForm.value.mobile_number;
      orderData.location = orderForm.value.location;
    } else {
      orderData.customer_id = orderForm.value.customer_id;
    }

    console.log('Sending order data:', orderData);

    const response = await fetch('http://localhost:8000/api/v1/orders/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token.value}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(orderData)
    });

    console.log('Response status:', response.status);
    const responseData = await response.json();
    console.log('Response data:', responseData);

    if (response.ok) {
      const createdOrder = responseData;
      // If user selected a different status, update it
      if (orderForm.value.status && orderForm.value.status !== 'pending') {
        await fetch(`http://localhost:8000/api/v1/orders/${createdOrder.id}/status/`, {
          method: 'PATCH',
          headers: {
            'Authorization': `Bearer ${token.value}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ status: orderForm.value.status })
        });
      }
      await fetchOrders();
      orderForm.value = {
        customer_id: '',
        customer_name: '',
        mobile_number: '',
        items: [{ cake: '', quantity: 1, price: '' }],
        total_amount: '',
        status: 'pending',
        location: ''
      };
      showOrderModal.value = false;
    } else {
      alert(responseData.detail || 'Failed to create order');
    }
  } catch (error) {
    console.error('Error adding order:', error);
    alert('Failed to create order. Please try again.');
  }
}

async function updateOrderStatus(order) {
  if (!order.newStatus || order.newStatus === order.status) return;
  try {
    console.log('Updating order status:', order.id, order.newStatus);
    const response = await fetch(`http://localhost:8000/api/v1/orders/${order.id}/status/`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token.value}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ status: order.newStatus })
    });
    console.log('Status update response:', response.status);
    if (response.ok) {
      const data = await response.json();
      console.log('Status updated successfully:', data);
      await fetchOrders();
    } else {
      const error = await response.json();
      console.error('Failed to update status:', error);
      alert(error.detail || 'Failed to update status');
    }
  } catch (error) {
    console.error('Error updating status:', error);
    alert('Failed to update status');
  }
}

function viewCustomerDetails(order) {
  selectedOrder.value = {
    ...order,
    customer: order.customer || {
      first_name: order.customer_name,
      last_name: '',
      mobile_number: order.mobile_number,
      email: ''
    },
    delivery: {
      customer_name: order.customer_name,
      mobile_number: order.mobile_number,
      location: order.location,
      address: order.location
    }
  };
  showCustomerModal.value = true;
}

async function fetchAllOrders() {
  try {
    const response = await fetch('http://localhost:8000/api/v1/orders/all-details/', {
      headers: { Authorization: `Bearer ${token.value}` }
    });
    if (response.ok) {
      const data = await response.json();
      console.log('Fetched all orders:', data);
      allOrders.value = data;
    } else {
      allOrders.value = [];
    }
  } catch (error) {
    allOrders.value = [];
    console.error('Error fetching all orders:', error);
  }
}

onMounted(() => {
  fetchActiveCakesCount();
  fetchMessages(true)
  fetchRecentActivity();
  fetchOrders();
  if (window.lucide) window.lucide.createIcons()
})

onUnmounted(() => {
  if (messageInterval) {
    clearInterval(messageInterval)
    messageInterval = null
  }
  if (ordersInterval) {
    clearInterval(ordersInterval)
    ordersInterval = null
  }
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
.messages-section {
  background: #fff7f0;
  border-radius: 12px;
  padding: 2rem;
  margin-top: 2rem;
  box-shadow: 0 2px 8px rgba(243,112,34,0.07);
}
.message-card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
  margin-bottom: 1.5rem;
  padding: 1.2rem 1.5rem;
}
.message-header {
  display: flex;
  gap: 1.5rem;
  font-size: 1.05rem;
  margin-bottom: 0.7rem;
  color: #ff6b35;
  font-weight: 600;
}
.message-name {
  flex: 1;
}
.message-email {
  color: #23232b;
  font-size: 0.98rem;
}
.message-date {
  color: #b0b0b0;
  font-size: 0.95rem;
}
.message-body {
  color: #23232b;
  font-size: 1.08rem;
  margin-top: 0.5rem;
}
.no-messages {
  color: #b0b0b0;
  text-align: center;
  margin: 2rem 0;
  font-size: 1.1rem;
}
.status-badge {
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
  text-transform: capitalize;
}
.status-badge.pending {
  background: #fef3c7;
  color: #92400e;
}
.status-badge.completed {
  background: #dcfce7;
  color: #166534;
}
.status-badge.cancelled {
  background: #fee2e2;
  color: #991b1b;
}
.order-item-form {
  margin-bottom: 10px;
}
.item-row {
  display: flex;
  gap: 10px;
  align-items: center;
}
.item-row input {
  flex: 1;
}
.remove-item {
  background: #fee2e2;
  color: #991b1b;
  border: none;
  border-radius: 6px;
  padding: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}
.add-item-btn {
  background: #f3f4f6;
  color: #374151;
  border: none;
  border-radius: 6px;
  padding: 8px 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 10px;
}
.add-item-btn:hover {
  background: #e5e7eb;
}
.cake-select {
  flex: 2;
  background: #23232b;
  border: 1px solid #24242e;
  border-radius: 8px;
  color: #fff;
  padding: 10px 12px;
  font-size: 1rem;
  outline: none;
  transition: border 0.2s;
}
.quantity-input {
  flex: 1;
  min-width: 80px;
}
.price-input {
  flex: 1;
  min-width: 100px;
}
.total-input {
  background: #2a2a35;
  color: #fff;
  font-weight: 600;
}
.status-select {
  background: #23232b;
  border: 1px solid #24242e;
  border-radius: 8px;
  color: #fff;
  padding: 10px 12px;
  font-size: 1rem;
  outline: none;
  transition: border 0.2s;
  width: 100%;
}
.status-select:focus,
.cake-select:focus {
  border: 1.5px solid #ff6b35;
}
.customer-form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
  margin-bottom: 20px;
}
.customer-input {
  width: 100%;
  background: #23232b;
  border: 1px solid #24242e;
  border-radius: 8px;
  color: #fff;
  padding: 10px 12px;
  font-size: 1rem;
  outline: none;
  transition: border 0.2s;
}
.customer-input:focus {
  border: 1.5px solid #ff6b35;
}
.customer-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.customer-name {
  font-weight: 600;
  color: #fff;
}
.customer-contact {
  color: #b0b0b8;
  font-size: 0.9rem;
}
.customer-location {
  color: #b0b0b8;
  font-size: 0.9rem;
  font-style: italic;
}
.search-container {
  position: relative;
}
.search-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: #23232b;
  border: 1px solid #24242e;
  border-radius: 8px;
  margin-top: 4px;
  max-height: 200px;
  overflow-y: auto;
  z-index: 1000;
}
.search-result-item {
  padding: 10px;
  cursor: pointer;
  transition: background 0.2s;
}
.search-result-item:hover {
  background: #2a2a35;
}
.error-message {
  color: #ef4444;
  font-size: 0.85rem;
  margin-top: 4px;
}
.customer-input.error {
  border-color: #ef4444;
}
.location-input-container {
  position: relative;
  display: flex;
  gap: 8px;
}
.map-button {
  background: #23232b;
  border: 1px solid #24242e;
  border-radius: 8px;
  padding: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}
.map-button:hover {
  background: #2a2a35;
}
.map-container {
  margin-top: 10px;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #24242e;
}
.map {
  height: 300px;
  width: 100%;
}
.map-search-input {
  margin: 10px;
  padding: 8px 12px;
  border: 1px solid #24242e;
  border-radius: 8px;
  background: #23232b;
  color: #fff;
  font-size: 14px;
  width: 250px;
  outline: none;
}
.map-search-input:focus {
  border-color: #ff6b35;
}
</style> 