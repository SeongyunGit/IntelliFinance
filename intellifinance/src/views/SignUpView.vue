<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="username" id="username" v-model.trim="username"><br>

      <label for="password1">password : </label>
      <input type="password" id="password1" v-model.trim="password1"><br>

      <label for="password2">password confirmation : </label>
      <input type="password" id="password2" v-model.trim="password2">

      <label for="member_birth">생일: </label>
      <input type="date" id="member_birth" v-model.trim="member_birth">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const member_birth = ref(null)

const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    member_birth: member_birth.value,
  }
  console.log(payload)
  
  store.signUp(payload)
}

</script>

<style>

</style>
