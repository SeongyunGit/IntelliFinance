<template>
  <div>
    <h5>{{ bank.fin_prdt_nm }}</h5>
    <p>{{ bank.kor_co_nm }}</p>
    <p>{{ bank.mtrt_int }}</p>
    <p>{{ bank.type_a }}</p>
    <!-- <RouterLink to="/options">상세옵션</RouterLink> -->
    <hr>
    <DepositListItemItemoptions :bank="bank"/>
    <!-- <RouterView /> -->
    <hr>
  </div>
</template>

<script setup>
// import { RouterLink, RouterView } from 'vue-router'
import DepositListItemItemoptions from '@/components/DepositListItemItemoptions.vue'

defineProps({
  bank: Object
})
</script>
