<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const logOut = function () {
  store.logOut()
}
</script>

<template>
  <header>
    <div>
      <h1>테스트 Appvue</h1>
      <nav>
        <RouterLink to="/">Home</RouterLink> |
        <RouterLink to="/company">Bank</RouterLink> |
        <RouterLink to="/update">update</RouterLink> |
        <RouterLink to="/signup">signup</RouterLink> |
        <RouterLink to="/login">login</RouterLink> |
        <form @submit.prevent="logOut">
          <input type="submit" value="Logout">
        </form>
      </nav>
      <nav>
        <RouterLink to="/deposit">deposit</RouterLink> |
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
