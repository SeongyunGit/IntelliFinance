<template>
  <div>
    <div class="min-h-screen bg-gray-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div class="bg-white shadow-lg rounded-lg p-8">
      <div class="text-center">
        <h2 class="text-2xl font-bold text-gray-900">Welcome!</h2>
        <p class="mt-2 text-sm text-gray-600">Sign in to your account</p>
      </div>
      <form class="mt-8 space-y-6" action="#" method="POST" @submit.prevent="logIn">
        <!-- Email Input -->
        <div>
          
          <label for="username" class="block text-sm font-medium text-gray-700">Email address</label>
          <div class="mt-1">
            <input type="email" id="username" v-model.trim="username" required
              class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-400 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" 
              placeholder="you@example.com">
          </div>
        </div>

        <!-- Password Input -->
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
          <div class="mt-1">
            <input type="password" id="password" v-model.trim="password" required
              class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-400 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" 
              placeholder="••••••••">
          </div>
        </div>

        <!-- Forgot Password -->
        <div class="flex items-center justify-between">
          <div class="text-sm">
            <a href="/forgot-password" class="font-medium text-indigo-600 hover:text-indigo-500">
              <RouterLink to="/login/forgot-password">Forgot your password?</RouterLink>
            </a>
          </div>
        </div>

        <!-- Submit Button -->
        <div>
          <button type="submit" value="logIn"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Sign In
          </button>
        </div>
      </form>
    </div>

    <!-- Sign Up Redirect -->
    <p class="mt-6 text-center text-sm text-gray-600">
      Don't have an account? 
      <a href="/signup" class="font-medium text-indigo-600 hover:text-indigo-500">Sign up</a>
    </p>
  </div>
</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router';


const username = ref(null)
const password = ref(null)

const store = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  

  store.logIn(payload)
}

</script>

<style>

</style>
