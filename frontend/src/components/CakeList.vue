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
        <button @click="openDeleteModal(cake.id)">Delete</button>
      </li>
    </ul>
    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteModal" class="modal-overlay">
      <div class="modal-content">
        <div class="modal-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="none" viewBox="0 0 24 24"><path fill="#ff6b35" d="M15.5 4l-1-1h-5l-1 1H5v2h14V4h-3.5zM6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zm2-9h8v10H8V10z"/></svg>
        </div>
        <h3>Delete Cake</h3>
        <p>Are you sure you want to delete this cake?</p>
        <div class="modal-actions">
          <button class="cancel-btn" @click="closeDeleteModal">Cancel</button>
          <button class="delete-btn" @click="confirmDelete">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CakeList",
  props: {
    cakes: Array,
    token: String
  },
  data() {
    return {
      showDeleteModal: false,
      deleteId: null
    };
  },
  methods: {
    openDeleteModal(id) {
      this.deleteId = id;
      this.showDeleteModal = true;
    },
    closeDeleteModal() {
      this.showDeleteModal = false;
      this.deleteId = null;
    },
    async confirmDelete() {
      if (!this.deleteId) return;
      await fetch(`/api/v1/cakes/${this.deleteId}/`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${this.token}` }
      });
      this.$emit("refresh");
      this.closeDeleteModal();
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
.modal-overlay {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  pointer-events: auto;
}
.modal-content {
  background: #fff;
  color: #23232b;
  width: 220px;
  height: 220px;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.14);
  border: 1.5px solid #ffe0d6;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  animation: fadeScaleIn 0.22s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  min-width: unset;
  max-width: unset;
  padding: 0;
}
.modal-icon {
  font-size: 2rem;
  color: #ff6b35;
  margin-bottom: 0.2rem;
}
.modal-content h3 {
  color: #ff6b35;
  font-size: 1.08rem;
  font-weight: 700;
  margin-bottom: 0.2rem;
  margin-top: 0.2rem;
}
.modal-content p {
  color: #23232b;
  font-size: 0.92rem;
  margin-bottom: 0.7rem;
  margin-top: 0.1rem;
}
.modal-actions {
  display: flex;
  justify-content: center;
  gap: 0.7rem;
  margin-top: 0.2rem;
}
.cancel-btn, .delete-btn {
  padding: 0.35rem 0.8rem;
  font-size: 0.92rem;
  border-radius: 5px;
}
.cancel-btn {
  background: #f3f3f7;
  color: #23232b;
  border: 1.5px solid #e0e0e0;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s, border 0.2s;
}
.cancel-btn:hover {
  background: #ececec;
  border: 1.5px solid #ff6b35;
}
.delete-btn {
  background: linear-gradient(135deg, #ff6b35, #f7931e);
  color: #fff;
  border: none;
  cursor: pointer;
  font-weight: 700;
  box-shadow: 0 4px 16px rgba(255, 107, 53, 0.10);
  transition: background 0.2s, box-shadow 0.2s;
}
.delete-btn:hover {
  background: linear-gradient(135deg, #f7931e, #ff006e);
  box-shadow: 0 8px 24px rgba(255, 107, 53, 0.18);
}
@media (max-width: 600px) {
  .modal-content {
    width: 90vw;
    height: 90vw;
    min-width: unset;
    max-width: unset;
  }
}
@keyframes fadeScaleIn {
  from {
    transform: scale(0.92);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
</style> 