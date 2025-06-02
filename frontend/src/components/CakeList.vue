<template>
  <div class="cake-list">
    <h2>Cakes</h2>
    <ul>
      <li v-for="cake in cakes" :key="cake.id">
        <img v-if="cake.image" :src="getImageUrl(cake.image)" alt="Cake" width="80" />
        <div>
          <strong>{{ cake.name }}</strong> - ${{ cake.price }}
          <p>{{ cake.description }}</p>
        </div>
        <button @click="$emit('edit', cake)">Edit</button>
        <button @click="deleteCake(cake.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "CakeList",
  props: {
    cakes: Array,
    token: String
  },
  methods: {
    async deleteCake(id) {
      if (!confirm("Delete this cake?")) return;
      await fetch(`/api/v1/cakes/${id}/`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${this.token}` }
      });
      this.$emit("refresh");
    },
    getImageUrl(path) {
      if (!path) return '';
      if (path.startsWith('http')) return path;
      return `http://localhost:8000${path}`;
    }
  }
};
</script>

<style scoped>
.cake-list {
  background: #23232b;
  border-radius: 25px;
  padding: 40px;
  border: 1px solid #24242e;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
  margin: 2rem auto;
  max-width: 700px;
}
.cake-list h2 {
  color: #ff6b35;
  margin-bottom: 1.5rem;
  font-weight: 700;
}
.cake-list ul {
  list-style: none;
  padding: 0;
}
.cake-list li {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
  background: #18181b;
  padding: 1.2rem;
  border-radius: 16px;
  border: 1px solid #24242e;
  box-shadow: 0 8px 24px rgba(255, 107, 53, 0.04);
}
.cake-list img {
  border-radius: 12px;
  object-fit: cover;
  width: 80px;
  height: 80px;
  background: #23232b;
  border: 1px solid #24242e;
}
.cake-list strong {
  color: #fff;
  font-size: 1.1rem;
}
.cake-list p {
  color: #b0b0b8;
  font-size: 1rem;
  margin: 0.2rem 0 0 0;
}
.cake-list button {
  background: linear-gradient(135deg, #ff6b35, #f7931e);
  color: #fff;
  border: none;
  padding: 0.5rem 1.1rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  font-size: 1rem;
  margin-left: 0.5rem;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 8px 24px rgba(255, 107, 53, 0.08);
}
.cake-list button:hover {
  background: linear-gradient(135deg, #f7931e, #ff006e);
}
</style> 