<template>
  <div>
    <hr>
    <h3>설문</h3>
    {{ selected }}
    <div>
      <!-- 금융 기관명 (체크박스, 복수 선택 가능) -->
      <ul class="select-list">
        <li @click="fetchData(1)">
          <span :class="{active: selected == 1}">예금</span>
        </li>
        <li @click="fetchData(2)">
          <span :class="{ active: selected == 2 }">적금</span>
        </li>
        <li @click="fetchData(3)">
          <span :class="{ active: selected == 3 }">대출</span>
        </li>
      </ul>
      <div>
        <DepositSurvey v-if="selected == 1" :surveyData="store.surveyData.deposit" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref, watch } from 'vue'
import DepositSurvey from './DepositSurvey.vue';

// Store 사용
const store = useCounterStore()

const selected = ref(0)
const fetchData = (sel) => {
  selected.value = sel
}
// const deposit = store.surveyData.deposit
</script>

<style scoped>
</style>
