<template>
  <form @submit.prevent="handleSubmit" enctype="multipart/form-data" class="cake-form">
    <div>
      <label>Name:</label>
      <input v-model="form.name" type="text" required />
    </div>
    <div>
      <label>Description:</label>
      <textarea v-model="form.description" required></textarea>
    </div>
    <div>
      <label>Price:</label>
      <input v-model="form.price" type="number" step="0.01" required />
    </div>
    <div>
      <label>Image:</label>
      <input @change="handleFileChange" type="file" accept="image/*" />
    </div>
    <div>
      <label>
        <input type="checkbox" v-model="form.is_available" />
        Available
      </label>
    </div>
    <button type="submit">{{ isEdit ? 'Update' : 'Create' }} Cake</button>
    <div v-if="error" class="error-popup" @click="error = ''">
      <div class="error-popup-content">
        <span class="close-btn" @click.stop="error = ''">&times;</span>
        <span>{{ error }}</span>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  name: "CakeForm",
  props: {
    cake: Object, // for edit mode
    isEdit: Boolean,
    token: String // JWT token
  },
  data() {
    return {
      form: {
        name: this.cake?.name || "",
        description: this.cake?.description || "",
        price: this.cake?.price || "",
        image: null,
        is_available: this.cake?.is_available ?? true
      },
      error: ""
    };
  },
  methods: {
    handleFileChange(e) {
      this.form.image = e.target.files[0];
    },
    async handleSubmit() {
      this.error = "";
      const formData = new FormData();
      formData.append("name", this.form.name);
      formData.append("description", this.form.description);
      formData.append("price", this.form.price);
      if (this.form.image) formData.append("image", this.form.image);
      formData.append("is_available", this.form.is_available);

      try {
        const url = this.isEdit
          ? `/api/v1/cakes/${this.cake.id}/`
          : "/api/v1/cakes/";
        const method = this.isEdit ? "PUT" : "POST";
        const res = await fetch(url, {
          method,
          headers: {
            Authorization: `Bearer ${this.token}`
          },
          body: formData
        });

        const contentType = res.headers.get("content-type");
        if (!res.ok) {
          if (contentType && contentType.includes("application/json")) {
            const err = await res.json();
            throw new Error(err.detail || JSON.stringify(err) || "Error saving cake");
          } else {
            const errText = await res.text();
            throw new Error(errText || "Unknown error");
          }
        }

        this.$emit("success");
      } catch (err) {
        this.error = err.message;
      }
    }
  }
};
</script>

<style scoped>
.cake-form {
  background: #23232b;
  border-radius: 25px;
  padding: 40px;
  border: 1px solid #24242e;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
  max-width: 500px;
  margin: 2rem auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.cake-form label {
  font-weight: 600;
  color: #f7931e;
  margin-bottom: 0.5rem;
}
.cake-form input,
.cake-form textarea {
  width: 100%;
  padding: 0.7rem;
  border: 1px solid #24242e;
  border-radius: 8px;
  background: #18181b;
  color: #fff;
  font-size: 1rem;
  margin-bottom: 0.5rem;
  transition: border 0.2s;
}
.cake-form input:focus,
.cake-form textarea:focus {
  border: 1.5px solid #ff6b35;
}
.cake-form button {
  background: linear-gradient(135deg, #ff6b35, #f7931e);
  color: #fff;
  border: none;
  padding: 0.9rem;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 600;
  font-size: 1.1rem;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 8px 24px rgba(255, 107, 53, 0.08);
}
.cake-form button:hover {
  background: linear-gradient(135deg, #f7931e, #ff006e);
}
.cake-form .error {
  color: #ff006e;
  margin-top: 0.5rem;
  font-weight: 500;
}
.error-popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.error-popup-content {
  background: #23232b;
  color: #ff006e;
  padding: 2rem 2.5rem;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.25);
  font-size: 1.1rem;
  position: relative;
  min-width: 280px;
  max-width: 90vw;
  text-align: center;
}
.close-btn {
  position: absolute;
  top: 10px;
  right: 18px;
  font-size: 1.5rem;
  color: #fff;
  cursor: pointer;
  font-weight: bold;
}
</style> 