<template>
  <div>
    <hr>
    <h5>{{ bank.fin_prdt_nm }}</h5>
    <p>{{ bank.kor_co_nm }}</p>
    <p>{{ bank.mtrt_int }}</p>
    <p>{{ bank.loan_inci_expn }}</p>
    <p>{{ bank.type_a }}</p>
    <p>{{ bank.id }}</p>
  </div>
</template>

<script setup>
defineProps({
  bank: Object
})
</script>
