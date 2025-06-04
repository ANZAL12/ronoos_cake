<template>
  <div class="aboutus-container">
    <div class="aboutus-header">
      <img src="/logo.png" alt="Ronoos Cake Logo" class="aboutus-logo" />
      <h1 class="aboutus-title">About <span>Ronoos Cake</span></h1>
    </div>
    <div class="aboutus-content">
      <p>
        Welcome to Ronoos Cake! We are passionate bakers dedicated to creating delicious, beautiful cakes for every occasion. Our journey began in 2015, and since then, we've served thousands of happy customers with our unique flavors and creative designs.
      </p>
      <p>
        Our mission is to make every celebration sweeter. Whether it's a birthday, wedding, anniversary, or just a craving for something special, Ronoos Cake is here to make your moments memorable.
      </p>
      <h2 class="aboutus-section-title">Meet Our Team</h2>
      <div class="aboutus-team">
        <div class="team-member" v-for="member in team" :key="member.name">
          <img :src="member.photo" :alt="member.name" class="team-photo" />
          <div class="team-name">{{ member.name }}</div>
          <div class="team-role">{{ member.role }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const team = [
  {
    name: 'Anzal Ronoos',
    role: 'Master Baker & Founder',
    photo: 'https://randomuser.me/api/portraits/men/32.jpg',
  },
  {
    name: 'Sara Lee',
    role: 'Cake Designer',
    photo: 'https://randomuser.me/api/portraits/women/44.jpg',
  },
  {
    name: 'John Smith',
    role: 'Pastry Chef',
    photo: 'https://randomuser.me/api/portraits/men/65.jpg',
  },
]
</script>

<style scoped>
.aboutus-container {
  background: #fff;
  min-height: 100vh;
  padding: 0 0 3rem 0;
}
.aboutus-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2.5rem 0 1.5rem 0;
}
.aboutus-logo {
  width: 80px;
  height: 80px;
  object-fit: contain;
  margin-bottom: 1rem;
}
.aboutus-title {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(90deg, #f37022, #ff8c42, #ff6b35);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-fill-color: transparent;
  margin-bottom: 0.5rem;
}
.aboutus-title span {
  color: #f37022;
}
.aboutus-content {
  max-width: 700px;
  margin: 0 auto;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.07);
  padding: 2rem 2.5rem;
  font-size: 1.15rem;
  color: #23232b;
}
.aboutus-section-title {
  margin-top: 2.5rem;
  font-size: 1.4rem;
  font-weight: 700;
  color: #f37022;
  margin-bottom: 1.2rem;
}
.aboutus-team {
  display: flex;
  gap: 2.5rem;
  flex-wrap: wrap;
  justify-content: center;
}
.team-member {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff7f0;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(243,112,34,0.07);
  padding: 1.2rem 1.5rem;
  min-width: 180px;
  margin-bottom: 1.5rem;
}
.team-photo {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 0.7rem;
}
.team-name {
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 0.2rem;
}
.team-role {
  color: #f37022;
  font-size: 0.98rem;
}
</style> 