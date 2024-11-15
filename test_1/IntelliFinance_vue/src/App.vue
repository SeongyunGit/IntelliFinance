<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div>
      <h1>테스트 Appvue</h1>
      <nav>
        <RouterLink to="/">Home</RouterLink> |
        <RouterLink to="/company">Bank</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
