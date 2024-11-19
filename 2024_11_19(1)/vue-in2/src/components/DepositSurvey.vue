<template>
  <div>
    <hr>
    <h3>Deposit Survey</h3>
    <div>
      <!-- 금융 기관명 (dropdown, 은행 선택) -->
      <p>1. 은행이름:
        <select v-model="surveyData.kor_co_nm">
          <option value="국민">국민</option>
          <option value="우리">우리</option>
          <option value="신한">신한</option>
          <!-- 추가적인 은행을 여기에 추가 가능 -->
        </select>
      </p>

      <!-- 이자율 유형 (radio, 단리 / 복리 선택) -->
      <p>2. 이자율유형:
        <label><input v-model="surveyData.intr_rate_type_nm" type="radio" value="null" /> 전체</label>
        <label><input v-model="surveyData.intr_rate_type_nm" type="radio" value="단리" /> 단리</label>
        <label><input v-model="surveyData.intr_rate_type_nm" type="radio" value="복리" /> 복리</label>
      </p>

      <!-- 저축 예정 기간 (radio, 1, 3, 6, 12개월 선택) -->
      <p>3. 저축 예정 기간:
        <label><input v-model="surveyData.save_trm" type="radio" value="null" /> 전체</label>
        <label><input v-model="surveyData.save_trm" type="radio" value="1" /> 1개월</label>
        <label><input v-model="surveyData.save_trm" type="radio" value="3" /> 3개월</label>
        <label><input v-model="surveyData.save_trm" type="radio" value="6" /> 6개월</label>
        <label><input v-model="surveyData.save_trm" type="radio" value="12" /> 12개월</label>
      </p>

      <!-- intr_rate: 기본 금리 -->
      <p>4. 기본금리: <input v-model="surveyData.intr_rate" type="number" placeholder="Enter interest rate" /></p>

      <!-- intr_rate2: 우대 금리 -->
      <p>5. 우대금리: <input v-model="surveyData.intr_rate2" type="number" placeholder="Enter preferential interest rate" /></p>
    </div>
    <hr>
    <!-- '저장' 버튼 -->
    <button @click="submitSurvey">저장</button>
    <p>{{ surveyData }}</p>
    <hr>
    <div v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank">
      <DepositListItem v-if="bank.type_a === 'deposit'" :bank="bank"/>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import DepositListItem from '@/components/DepositListItem.vue'
import { useCounterStore } from '@/stores/counter'

// Store 사용
const store = useCounterStore()

const props = defineProps({
  surveyData: Object
});

// 서베이 데이터를 저장하는 함수
const submitSurvey = () => {
  // 데이터를 저장하기 위한 객체
  const newSurveyData = {
    'kor_co_nm': props.surveyData['kor_co_nm'] || null,
    'intr_rate_type_nm': props.surveyData['intr_rate_type_nm'] || null,  // 단일 값으로 수정
    'save_trm': props.surveyData['save_trm'] || null,  // 단일 값으로 수정
    'intr_rate': props.surveyData['intr_rate'] || null,
    'intr_rate2': props.surveyData['intr_rate2'] || null
  }
  // 데이터가 이미 존재하면 업데이트
  console.log('수정', newSurveyData)
  store.updateSurveyData(props.surveyData.id, newSurveyData) 
}
</script>

<style scoped>
</style>
