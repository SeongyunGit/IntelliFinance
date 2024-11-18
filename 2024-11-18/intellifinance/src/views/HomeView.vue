<template>
  <div>
    <h1>Home</h1>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})


</script>

<style lang="scss" scoped>

</style>