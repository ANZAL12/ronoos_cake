<template>
  <div>
    <CakeForm
      v-if="showForm"
      :cake="selectedCake"
      :isEdit="!!selectedCake"
      :token="token"
      @success="fetchCakes; showForm = false; selectedCake = null"
    />
    <button v-else class="add-cake-btn" @click="showForm = true">Add Cake</button>
    <CakeList
      :cakes="cakes"
      :token="token"
      @edit="editCake"
      @refresh="fetchCakes"
    />
  </div>
</template>

<script>
import CakeForm from "@/components/CakeForm.vue";
import CakeList from "@/components/CakeList.vue";

export default {
  components: { CakeForm, CakeList },
  props: {
    token: String
  },
  data() {
    return {
      cakes: [],
      showForm: false,
      selectedCake: null
    };
  },
  methods: {
    async fetchCakes() {
      const res = await fetch("/api/v1/cakes/", {
        headers: { Authorization: `Bearer ${this.token}` }
      });
      this.cakes = await res.json();
    },
    editCake(cake) {
      this.selectedCake = cake;
      this.showForm = true;
    }
  },
  mounted() {
    this.fetchCakes();
    this.pollInterval = setInterval(this.fetchCakes, 5000); // Poll every 5 seconds
  },
  beforeUnmount() {
    clearInterval(this.pollInterval);
  }
};
</script>

<style scoped>
.add-cake-btn {
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
  margin: 1.5rem auto 2.5rem auto;
  display: block;
  box-shadow: 0 2px 8px rgba(243,112,34,0.07);
}
.add-cake-btn:hover {
  background: #ff8c42;
}
</style> 