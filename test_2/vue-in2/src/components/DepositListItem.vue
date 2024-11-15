<template>
  <div>
    <h5>{{ bank.fin_prdt_nm }}</h5>
    <p>{{ bank.kor_co_nm }}</p>
    <p>{{ bank.mtrt_int }}</p>
    <p>{{ bank.type_a }}</p>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  bank: Object
})
</script>
