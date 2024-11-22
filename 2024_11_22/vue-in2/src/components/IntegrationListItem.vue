<template>
  <div>
    <h2 class="text-lg font-bold text-gray-800 mb-4">{{ bank.fin_prdt_nm }}</h2>
        <p class="text-sm text-gray-500 mb-4">{{ bank.kor_co_nm }}</p>
        <div class="border-t pt-4">
          <div class="text-sm text-gray-600 space-y-2">
          <p><span class="font-medium">만기 후 1개월 이내:</span> {{ bank.mtrt_int }}</p>
          <p><span class="font-medium">1개월 초과 6개월 이내:</span> {{ bank.loan_inci_expn }}</p>
          <p><span class="font-medium">6개월 초과:</span> {{ bank.type_a }}</p>
        </div>
        </div>
        <div class="mt-4 text-center">
          <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            {{ bank.id }}
          </button>
        </div>

    <!-- <hr>
    <h5>{{ bank.fin_prdt_nm }}</h5>
    <p>{{ bank.kor_co_nm }}</p>
    <p>{{ bank.mtrt_int }}</p>
    <p>{{ bank.loan_inci_expn }}</p>
    <p>{{ bank.type_a }}</p>
    <p>{{ bank.id }}</p> -->
  </div>
</template>

<script setup>
defineProps({
  bank: Object
})
</script>
