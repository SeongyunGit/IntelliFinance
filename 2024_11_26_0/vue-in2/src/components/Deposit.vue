<template>
    <div class="container mx-auto min-h-screen bg-gradient-to-b from-indigo-600 to-indigo-500 p-8">
      <h3 class="text-3xl font-bold text-center text-white mb-8">예금</h3>
      <div class="grid grid-cols-3 gap-4 p-4">
        <DepositItem
        v-for="bank in store.integrationProducts" class="bg-white rounded-lg shadow-md p-6"
        :key="bank.id"
        :bank="bank"
      />  
      </div>
  
</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import DepositItem from './DepositItem.vue';  
const store = useCounterStore()
</script>
<style>

</style>