<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="username" id="username" v-model.trim="username"><br>

      <label for="email">email : </label>
      <input type="email" id="email" v-model.trim="email"><br>

      <label for="password">password : </label>
      <input type="password" id="password" v-model.trim="password"><br>

      <label for="password2">password confirmation : </label>
      <input type="password" id="password2" v-model.trim="password2">

      <label for="birth_date">생일: </label>
      <input type="date" id="birth_date" v-model.trim="birth_date">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const email = ref(null)
const password = ref(null)
const password2 = ref(null)
const birth_date = ref(null)

const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    email: email.value,
    password: password.value,
    password2: password2.value,
    birth_date: birth_date.value,
  }
  console.log(payload)
  
  store.signUp(payload)
}

</script>

<style>

</style>
