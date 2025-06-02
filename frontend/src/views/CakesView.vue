<template>
  <div>
    <CakeForm
      v-if="showForm"
      :cake="selectedCake"
      :isEdit="!!selectedCake"
      :token="token"
      @success="fetchCakes; showForm = false; selectedCake = null"
    />
    <button v-else @click="showForm = true">Add Cake</button>
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