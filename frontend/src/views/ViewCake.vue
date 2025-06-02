<template>
  <div class="cake-card-grid">
    <div v-for="cake in cakes" :key="cake.id" class="cake-card">
      <img v-if="cake.image" :src="getImageUrl(cake.image)" alt="Cake Image" class="cake-image" />
      <div class="cake-info">
        <h3 class="cake-title">{{ cake.name }}</h3>
        <p class="cake-desc">{{ cake.description }}</p>
        <div class="cake-meta">
          <span class="cake-price">${{ cake.price }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ViewCake',
  props: {
    token: String
  },
  data() {
    return {
      cakes: []
    };
  },
  async mounted() {
    const res = await fetch('/api/v1/cakes/', {
      headers: { Authorization: `Bearer ${this.token}` }
    });
    this.cakes = await res.json();
  },
  methods: {
    getImageUrl(path) {
      if (!path) return '';
      if (path.startsWith('http')) return path;
      return `http://localhost:8000${path}`;
    }
  }
};
</script>

<style scoped>
.cake-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 2rem;
  padding: 2rem;
  background: #23232b;
  border-radius: 25px;
  border: 1px solid #24242e;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
}
.cake-card {
  background: #18181b;
  border-radius: 18px;
  box-shadow: 0 8px 24px rgba(255, 107, 53, 0.08);
  border: 1px solid #24242e;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem 1rem 1rem 1rem;
  transition: box-shadow 0.2s, transform 0.2s;
}
.cake-card:hover {
  box-shadow: 0 16px 32px rgba(255, 107, 53, 0.18);
  transform: translateY(-4px) scale(1.03);
}
.cake-image {
  width: 100%;
  max-width: 200px;
  height: 140px;
  object-fit: cover;
  border-radius: 12px;
  margin-bottom: 1rem;
  background: #23232b;
  border: 1px solid #24242e;
}
.cake-info {
  width: 100%;
  text-align: center;
}
.cake-title {
  color: #ff6b35;
  font-size: 1.3rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}
.cake-desc {
  color: #b0b0b8;
  font-size: 1rem;
  margin-bottom: 0.7rem;
}
.cake-meta {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
.cake-price {
  color: #fff;
  font-size: 1.1rem;
  font-weight: 600;
  background: linear-gradient(135deg, #ff6b35, #f7931e);
  padding: 0.3rem 1rem;
  border-radius: 8px;
}
</style> 