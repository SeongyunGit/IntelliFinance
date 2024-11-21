<template>
  <div>
    <hr>
    <h3>Deposit Survey</h3>
    <div>
      <!-- 금융 기관명 (체크박스, 복수 선택 가능) -->
      <p>1. 은행이름:
      <!-- '전체' 체크박스 -->
      <label><input type="checkbox" v-model="isAllSelected.kor_co_nm" @change="toggleAll('kor_co_nm')" /> 전체</label>
      <label><input type="checkbox" value="국민" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 국민</label>
      <label><input type="checkbox" value="우리" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 우리</label>
      <label><input type="checkbox" value="신한" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 신한</label>
      <label><input type="checkbox" value="농협" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 농협</label>
      <label><input type="checkbox" value="카카오" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" /> 카카오</label>
      </p>

      <!-- 이자율 유형 (체크박스) -->
      <p>2. 이자율유형:
      <label><input type="checkbox" v-model="isAllSelected.intr_rate_type_nm" @change="toggleAll('intr_rate_type_nm')" /> 전체</label>
      <label><input type="checkbox" value="단리" v-model="surveyData.intr_rate_type_nm" @change="checkAllCondition('intr_rate_type_nm')" /> 단리</label>
      <label><input type="checkbox" value="복리" v-model="surveyData.intr_rate_type_nm" @change="checkAllCondition('intr_rate_type_nm')" /> 복리</label>
      </p>
      <!-- 저축 예정 기간 (체크박스) -->
      <p>3. 저축 예정 기간:
      <label><input type="checkbox" v-model="isAllSelected.save_trm" @change="toggleAll('save_trm')" /> 전체</label>
      <label><input type="checkbox" value="1" v-model="surveyData.save_trm" @change="checkAllCondition('save_trm')" /> 1개월</label>
      <label><input type="checkbox" value="3" v-model="surveyData.save_trm" @change="checkAllCondition('save_trm')" /> 3개월</label>
      <label><input type="checkbox" value="6" v-model="surveyData.save_trm" @change="checkAllCondition('save_trm')" /> 6개월</label>
      <label><input type="checkbox" value="12" v-model="surveyData.save_trm" @change="checkAllCondition('save_trm')" /> 12개월</label>
      </p>
      <!-- intr_rate: 기본 금리 -->
      <p>4. 기본금리: <input v-model="surveyData.intr_rate" type="number" placeholder="Enter interest rate" /></p>

      <!-- intr_rate2: 우대 금리 -->
      <p>5. 우대금리: <input v-model="surveyData.intr_rate2" type="number" placeholder="Enter preferential interest rate" /></p>
    </div>
    <hr>
    <!-- '저장' 버튼 -->
    <button @click="submitSurvey">저장</button>
    <!-- <p>{{ surveyData }}</p> -->
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
  intr_rate_type_nm: false,
  save_trm: false,
  kor_co_nm: false
})

// `전체` 체크박스를 선택하거나 해제할 때 호출되는 함수
const toggleAll = (field) => {
  if (isAllSelected.value[field]) {
    // '전체'가 체크되면 모든 항목을 선택
    if (field === 'intr_rate_type_nm') {
      props.surveyData[field] = ['단리', '복리']
    } else if (field === 'save_trm') {
      props.surveyData[field] = ['1', '3', '6', '12']
    } else if (field === 'kor_co_nm') {
      props.surveyData[field] = ['국민', '우리', '신한', '농협', '카카오']
    }
  } else {
    // '전체'가 해제되면 모든 항목을 해제
    props.surveyData[field] = []
  }
}

// 각 항목의 체크 상태를 반영하여 '전체' 체크박스를 업데이트
const checkAllCondition = (field) => {
  if (field === 'intr_rate_type_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 2 // '단리', '복리'가 모두 체크되면 '전체' 체크
  } else if (field === 'save_trm') {
    isAllSelected.value[field] = props.surveyData[field].length === 4 // 1, 3, 6, 12개월이 모두 체크되면 '전체' 체크
  } else if (field === 'kor_co_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 5 // 모든 은행이 체크되면 '전체' 체크
  }
}

// 서베이 데이터를 저장하는 함수
const submitSurvey = () => {
  // 데이터를 저장하기 위한 객체
  const newSurveyData = {
    'kor_co_nm': props.surveyData['kor_co_nm'] || [],
    'intr_rate_type_nm': props.surveyData['intr_rate_type_nm'] || [],
    'save_trm': props.surveyData['save_trm'] || [],
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
