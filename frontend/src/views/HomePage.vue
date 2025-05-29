<template>
  <div>
    <nav class="navbar">
      <ul>
        <li>Our Collection</li>
        <li>About Us</li>
        <li>X-Mas And New Year cakes</li>
        <li>Offers</li>
        <li>Track Your Order</li>
        <li>Contact Us</li>
        <li>Menu Item</li>
      </ul>
    </nav>
    <div class="cake-grid">
      <div v-for="cake in cakes" :key="cake.name" class="cake-card">
        <img :src="cake.image" :alt="cake.name" class="cake-image" />
        <div class="cake-name">{{ cake.name }}</div>
        <div class="cake-price">Rs {{ cake.price.toFixed(2) }}</div>
        <button class="view-cakes-btn">VIEW CAKES &rarr;</button>
      </div>
    </div>
  </div>
</template>

<script setup>
const cakes = [
  {
    name: 'Almond Chocolate',
    price: 990,
    image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=400&q=80',
  },
  {
    name: 'Black Forest',
    price: 740,
    image: 'https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=400&q=80',
  },
  {
    name: 'Bounty Chocolate',
    price: 890,
    image: 'https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?auto=format&fit=crop&w=400&q=80',
  },
  {
    name: 'Cappuccino',
    price: 940,
    image: 'https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=400&q=80',
  },
  {
    name: 'Chocolate Truffle',
    price: 1050,
    image: 'https://images.unsplash.com/photo-1505250469679-203ad9ced0cb?auto=format&fit=crop&w=400&q=80',
  },
  {
    name: 'Fruit Overload',
    price: 1200,
    image: 'https://images.unsplash.com/photo-1464306076886-debca5e8a6b0?auto=format&fit=crop&w=400&q=80',
  },
]
</script>

<style scoped>
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
</style> 