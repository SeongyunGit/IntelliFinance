<template>
  <div>
    <hr>
    <h5>{{ bank.kor_co_nm }}</h5>
    <p>{{ bank.dcls_chrg_man }}</p>
    <p>{{ bank.homp_url }}</p>
  </div>
</template>

<script setup>
defineProps({
  bank: Object
})
</script>
