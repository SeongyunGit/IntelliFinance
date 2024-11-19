<template>
  <div>
    <h3>Integration List</h3>
    <IntegrationListItem 
      v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank"
    />
  </div>
</template>

<script setup>
import IntegrationListItem from '@/components/IntegrationListItem.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>
