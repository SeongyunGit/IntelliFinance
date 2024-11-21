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
    <nav class="bg-white border-b border-gray-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between items-center h-16">
      <!-- Logo -->
      <div class="flex-shrink-0">
        <!-- <img src="./assets/logo.PNG" alt="Home Banner" class="w-full h-96 object-cover"> -->
        <a href="/" class="text-2xl font-bold text-indigo-600">
          <RouterLink to="/">Home</RouterLink>
        </a>
      </div>

      <!-- Full Menu -->
      <div class="hidden md:flex space-x-4">
        <RouterLink to="/deposit" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          Integration
        </RouterLink>
        <RouterLink to="/company" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          Bank
        </RouterLink>
        <RouterLink to="/announcement" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          announcement
        </RouterLink>
        <RouterLink to="/update" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          update
        </RouterLink>
      </div>

      <!-- Call-to-Action Button -->
      <div class="hidden md:flex items-center space-x-4" v-if="!store.isLogin">
        <a href="/login" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          <RouterLink to="/login">login</RouterLink>
        </a>
        <a href="/signup" class="bg-indigo-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-indigo-700">
          <RouterLink to="/signup">Signup</RouterLink>
        </a>
      </div>
      <div class="hidden md:flex items-center space-x-4" v-else>
        <a href="/mypage"  class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          <RouterLink to="/mypage">mypage</RouterLink>
        </a>
        <form @submit.prevent="logOut">
          <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-indigo-700">
            Logout
          </button>
        </form>
      </div>
    </div>
  </div>
  </nav>
  </header>
  <RouterView />
</template>

<style scoped>
</style>
