<template>
  <div>
    <hr>
    <h3>설문</h3>
    {{ selected }}
    <div>
      <!-- 금융 기관명 (체크박스, 복수 선택 가능) -->
      <ul class="select-list">
        <li @click="fetchData(1)">
          <span :class="{ active: selected == 1 }">예금</span>
        </li>
        <li @click="fetchData(2)">
          <span :class="{ active: selected == 2 }">적금</span>
        </li>
        <li @click="fetchData(3)">
          <span :class="{ active: selected == 3 }">주택담보대출</span>
        </li>
        <li @click="fetchData(4)">
          <span :class="{ active: selected == 3 }">전세자금대출</span>
        </li>
      </ul>
      <div>
        <DepositSurvey v-if="selected == 1" :surveyData="store.surveyData.deposit" />
        <DepositList v-if="selected == 1" :surveyData="store.surveyData.deposit" />
        <SavingSurvey v-if="selected == 2" :surveyData="store.surveyData.saving" />
        <SavingList v-if="selected == 2" :surveyData="store.surveyData.saving" />
        <MortgageLoanSurvey v-if="selected == 3" :surveyData="store.surveyData.mortgageLoan" />
        <MortgageLoanList v-if="selected == 3" :surveyData="store.surveyData.mortgageLoan" />
        <RentHouseLoanSurvey v-if="selected == 4" :surveyData="store.surveyData.rentHouseLoan" />
        <RentHouseLoanList v-if="selected == 4" :surveyData="store.surveyData.rentHouseLoan" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref, watch } from 'vue'
import DepositSurvey from '@/components/DepositSurvey.vue';
import DepositList from '@/components/DepositList.vue';
import SavingSurvey from '@/components/SavingSurvey.vue';
import SavingList from '@/components/SavingList.vue';
import MortgageLoanSurvey from '@/components/MortgageLoanSurvey.vue';
import MortgageLoanList from '@/components/MortgageLoanList.vue';
import RentHouseLoanSurvey from '@/components/RentHouseLoanSurvey.vue';
import RentHouseLoanList from '@/components/RentHouseLoanList.vue';

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
