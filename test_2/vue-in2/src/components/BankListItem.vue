<template>
  <div>
    <h5>{{ bank.kor_co_nm }}</h5>
    <p>{{ bank.dcls_chrg_man }}</p>
    <p>{{ bank.homp_url }}</p>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  bank: Object
})
</script>
