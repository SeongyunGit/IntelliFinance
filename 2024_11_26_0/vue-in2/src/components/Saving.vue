<template>
    <div class="container mx-auto min-h-screen bg-gradient-to-b from-indigo-600 to-indigo-500 p-8">
      <h3 class="text-3xl font-bold text-center text-white mb-8">적금</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>
      <div class="grid grid-cols-3 gap-4 p-4">
        <SavingItem 
        v-for="bank in store.integrationProducts" class="bg-white rounded-lg shadow-md p-6"
        :key="bank.id"
        :bank="bank"
      />  
      </div>
  
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter'
import SavingItem from './SavingItem.vue';
  
  const store = useCounterStore()
  </script>
  