<template>
  <div>
    <hr>
    <h3>Lending Survey</h3>
    <div>
      <!-- 금융 기관명 (체크박스) -->
      <p>1. 은행이름:
        <label><input type="checkbox" v-model="isAllSelected.kor_co_nm" @change="toggleAll('kor_co_nm')" /> 전체</label>
        <label><input type="checkbox" value="한화생명보험주식회사" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 한화생명보험주식회사</label>
        <label><input type="checkbox" value="삼성생명보험주식회사" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 삼성생명보험주식회사</label>
        <label><input type="checkbox" value="흥국생명보험주식회사" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 흥국생명보험주식회사</label>
        <label><input type="checkbox" value="교보생명보험주식회사" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 교보생명보험주식회사</label>
        <label><input type="checkbox" value="하나생명보험주식회사" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 하나생명보험주식회사</label>
      </p>

      <!-- 상환 방식 -->
      <p>2. 상환방식:
        <label><input type="checkbox" v-model="isAllSelected.rpay_type_nm" @change="toggleAll('rpay_type_nm')" /> 전체</label>
        <label><input type="checkbox" value="분할상환방식" v-model="surveyData.rpay_type_nm" @change="checkAllCondition('rpay_type_nm')" /> 분할상환방식</label>
        <label><input type="checkbox" value="만기일시상환방식" v-model="surveyData.rpay_type_nm" @change="checkAllCondition('rpay_type_nm')" /> 만기일시상환방식</label>
      </p>

      <!-- 금리 유형 -->
      <p>3. 금리유형:
        <label><input type="checkbox" v-model="isAllSelected.lend_rate_type_nm" @change="toggleAll('lend_rate_type_nm')" /> 전체</label>
        <label><input type="checkbox" value="고정금리" v-model="surveyData.lend_rate_type_nm" @change="checkAllCondition('lend_rate_type_nm')" /> 고정금리</label>
        <label><input type="checkbox" value="변동금리" v-model="surveyData.lend_rate_type_nm" @change="checkAllCondition('lend_rate_type_nm')" /> 변동금리</label>
      </p>

      <!-- 금리 입력 -->
      <p>4. 최소 금리: <input v-model="surveyData.lend_rate_min" type="number" placeholder="Enter minimum interest rate" /></p>
      <p>5. 최대 금리: <input v-model="surveyData.lend_rate_max" type="number" placeholder="Enter maximum interest rate" /></p>
      <p>6. 평균 금리: <input v-model="surveyData.lend_rate_avg" type="number" placeholder="Enter average interest rate" /></p>

      <!-- 담보 유형 -->
      <p>7. 담보유형:
        <label><input type="checkbox" v-model="isAllSelected.mrtg_type_nm" @change="toggleAll('mrtg_type_nm')" /> 전체</label>
        <label><input type="checkbox" value="아파트" v-model="surveyData.mrtg_type_nm" @change="checkAllCondition('mrtg_type_nm')" /> 아파트</label>
        <label><input type="checkbox" value="아파트외" v-model="surveyData.mrtg_type_nm" @change="checkAllCondition('mrtg_type_nm')" /> 아파트외</label>
      </p>
    </div>
    <hr>
    <button @click="submitSurvey">저장</button>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'

// Store 사용
const store = useCounterStore()

const props = defineProps({
  surveyData: Object
});

// `전체` 체크박스를 선택했는지 여부를 추적하는 객체
const isAllSelected = ref({
  kor_co_nm: false,
  rpay_type_nm: false,
  lend_rate_type_nm: false,
  mrtg_type_nm: false
})

// `전체` 체크박스를 선택하거나 해제할 때 호출되는 함수
const toggleAll = (field) => {
  if (isAllSelected.value[field]) {
    if (field === 'kor_co_nm') {
      props.surveyData[field] = ['한화생명보험주식회사', '삼성생명보험주식회사', '흥국생명보험주식회사', '교보생명보험주식회사', '하나생명보험주식회사']
    } else if (field === 'rpay_type_nm') {
      props.surveyData[field] = ['분할상환방식', '만기일시상환방식']
    } else if (field === 'lend_rate_type_nm') {
      props.surveyData[field] = ['고정금리', '변동금리']
    } else if (field === 'mrtg_type_nm') {
      props.surveyData[field] = ['아파트', '아파트외']
    }
  } else {
    props.surveyData[field] = []
  }
}

// 각 항목의 체크 상태를 반영하여 '전체' 체크박스를 업데이트
const checkAllCondition = (field) => {
  if (field === 'kor_co_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 5
  } else if (field === 'rpay_type_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 2
  } else if (field === 'lend_rate_type_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 2
  } else if (field === 'mrtg_type_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 2
  }
}

// 서베이 데이터를 저장하는 함수
const submitSurvey = () => {
  // 데이터를 저장하기 위한 객체
  const newSurveyData = {
    'kor_co_nm': props.surveyData['kor_co_nm'] || [],
    'rpay_type_nm': props.surveyData['rpay_type_nm'] || [],
    'lend_rate_type_nm': props.surveyData['lend_rate_type_nm'] || [],
    'lend_rate_min': props.surveyData['lend_rate_min'] || null,
    'lend_rate_max': props.surveyData['lend_rate_max'] || null,
    'lend_rate_avg': props.surveyData['lend_rate_avg'] || null,
    'mrtg_type_nm': props.surveyData['mrtg_type_nm'] || [],
  }
  // 데이터가 이미 존재하면 업데이트
  console.log('수정', newSurveyData)
  store.updateSurveyData(props.surveyData.id, newSurveyData, 'mortgageLoan') 
}
</script>

<style scoped>
</style>
