<template>
  <div>
    <hr>
    <h3>Deposit Survey</h3>
    <div>
      <!-- kor_co_nm: 금융 기관명 -->
      <p>1. 은행이름: <input v-model="surveyData['kor_co_nm']" type="text" placeholder="Enter financial institution name" /></p>

      <!-- mtrt_int: 만기 후 이자 -->
      <p>2. 만기후 이자: <input v-model="surveyData['mtrt_int']" type="text" placeholder="Enter interest after maturity" /></p>

      <!-- intr_rate_type_nm: 이자율 유형 (radio로 하나만 선택) -->
      <p>3. 이자율유형: 
        <label><input v-model="surveyData['intr_rate_type_nm']" type="radio" value="전체" /> 전체</label>
        <label><input v-model="surveyData['intr_rate_type_nm']" type="radio" value="단리" /> 단리</label>
        <label><input v-model="surveyData['intr_rate_type_nm']" type="radio" value="복리" /> 복리</label>
      </p>

      <!-- save_trm: 기간 (radio로 하나만 선택) -->
      <p>4. 기간: 
        <label><input v-model="surveyData['save_trm']" type="radio" value="전체" /> 전체</label>
        <label><input v-model="surveyData['save_trm']" type="radio" value="1" /> 1</label>
        <label><input v-model="surveyData['save_trm']" type="radio" value="3" /> 3</label>
        <label><input v-model="surveyData['save_trm']" type="radio" value="6" /> 6</label>
        <label><input v-model="surveyData['save_trm']" type="radio" value="12" /> 12</label>
      </p>

      <!-- intr_rate: 기본 금리 -->
      <p>5. 기본금리: <input v-model="surveyData['intr_rate']" type="number" placeholder="Enter interest rate" /></p>

      <!-- intr_rate2: 우대 금리 -->
      <p>6. 우대금리: <input v-model="surveyData['intr_rate2']" type="number" placeholder="Enter preferential interest rate" /></p>
    </div>
    <hr>
    <!-- '저장' 버튼 -->
    <button @click="submitSurvey">저장</button>
    <p>{{ surveyData }}</p>
    <hr>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

// Store 사용
const store = useCounterStore()

// 데이터 바인딩을 위한 surveyData
const surveyData = ref({})

// 컴포넌트가 마운트될 때 surveyData를 불러오는 함수
onMounted(() => {
  // survey 데이터를 불러옴
  store.getSurveyData(1)
  // surveyData를 저장소에서 불러온 데이터로 초기화
  surveyData.value = store.surveyData
})

// 서베이 데이터를 저장하는 함수
const submitSurvey = () => {
  // 데이터를 저장하기 위한 객체
  const newSurveyData = {
    'kor_co_nm': surveyData.value['kor_co_nm'] || null,
    'mtrt_int': surveyData.value['mtrt_int'] || null,
    'intr_rate_type_nm': surveyData.value['intr_rate_type_nm'] || null,  // 단일 값으로 수정
    'save_trm': surveyData.value['save_trm'] || null,  // 단일 값으로 수정
    'intr_rate': surveyData.value['intr_rate'] || null,
    'intr_rate2': surveyData.value['intr_rate2'] || null
  }
  // 데이터가 이미 존재하는지 확인
  if (store.ox) {
    // 데이터가 이미 존재하면 업데이트
    console.log('수정', surveyData.value)
    store.updateSurveyData(store.surveyData.id, newSurveyData)  // 예시로 ID를 전달
  } else {
    // 데이터가 없으면 새로 추가
    console.log('생성')
    store.saveSurveyData(newSurveyData)
    store.ox = 1
  }
}
</script>



<style scoped>
</style>
