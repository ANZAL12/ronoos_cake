import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import HomePage from '@/views/HomePage.vue';
import AdminWelcome from '@/views/AdminWelcome.vue';
import BakerWelcome from '@/views/BakerWelcome.vue';
import RegisterCustomer from '@/views/RegisterCustomer.vue';
import CakesView from '@/views/CakesView.vue';
import CheckoutView from '../views/CheckoutView.vue'
import DeliveryDetailsView from '../views/DeliveryDetailsView.vue'
import OrderConfirmationView from '../views/OrderConfirmationView.vue'
import OrderListView from '../views/OrderListView.vue'
import OrderDetailView from '../views/OrderDetailView.vue'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/register',
    name: 'RegisterCustomer',
    component: RegisterCustomer,
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/admin-welcome',
    name: 'AdminWelcome',
    component: AdminWelcome,
  },
  {
    path: '/baker-welcome',
    name: 'BakerWelcome',
    component: BakerWelcome,
  },
  {
    path: '/cakes',
    name: 'Cakes',
    component: CakesView,
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: CheckoutView,
    meta: { requiresAuth: true }
  },
  {
    path: '/delivery-details/:orderId',
    name: 'delivery-details',
    component: DeliveryDetailsView,
    meta: { requiresAuth: true }
  },
  {
    path: '/order-confirmation/:orderId',
    name: 'order-confirmation',
    component: OrderConfirmationView,
    meta: { requiresAuth: true }
  },
  {
    path: '/orders',
    name: 'orders',
    component: OrderListView,
    meta: { requiresAuth: true }
  },
  {
    path: '/orders/:orderId',
    name: 'order-detail',
    component: OrderDetailView,
    meta: { requiresAuth: true }
  },
  {
    path: '/',
    redirect: '/login'
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Store last route after each navigation
router.afterEach((to) => {
  if (to.path !== '/login' && to.path !== '/register') {
    localStorage.setItem('lastRoute', to.fullPath);
  }
});

export default router;
