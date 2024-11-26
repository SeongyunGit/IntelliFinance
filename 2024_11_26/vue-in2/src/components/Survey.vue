<template>
  
  <div class="bg-gradient-to-b from-indigo-600 to-indigo-500 pb-12">
    <!-- 메인 섹션 -->
    <div class="bg-gradient-to-b from-indigo-600 to-indigo-500 pb-12">
      <div class="max-w-6xl mx-auto px-4 pt-8">
        <h3 class="font_roboto text-6xl font-bold montserrat text-white text-center mb-12">맞춤형 금융상품 찾기</h3>
        
        <!-- 금융상품 카테고리 그리드 -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div 
            v-for="(item, index) in categories" 
            :key="index"
            @click="fetchData(item.id)"
            :class="{'bg-white/90': selected === item.id, 'bg-white/75 hover:bg-white/90': selected !== item.id}"
            class="rounded-2xl p-6 cursor-pointer transition-all duration-300 transform hover:scale-105"
          >
            <div class="flex flex-col items-center space-y-3">
              <div class="w-12 h-12 flex items-center justify-center rounded-full"
                   :class="selected === item.id ? 'bg-indigo-100' : 'bg-indigo-50'">
                <span class="text-2xl">{{ item.icon }}</span>
              </div>
              <span class="font-extrabold font_roboto text-3xl text-gray-800">{{ item.name }}</span>
              <span class="font-bold font_roboto text-gray-600">{{ item.description }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container mx-auto">
      <div v-if="!selected" class="container-center text-center py-4 px-6 bg-indigo-50 rounded-lg shadow-md mx-2">
      <img src="@/assets/picture.webp" alt="Finance Illustration" class="finance-image mx-auto mb-6 rounded-lg" />
      <h3 class="font_roboto text-4xl font-semibold text-gray-700">당신의 맞춤형 금융상품을 찾으세요!</h3>
      <p class="font-bold font_roboto text-lg text-gray-500 mt-4">다양한 금융상품 중에서 나에게 맞는 상품을 선택하고, 맞춤형 설문을 통해 최적의 상품을 찾아보세요.</p>
      </div>
    </div>


    <!-- 설문 & 리스트 섹션 -->
    <div class="max-w-6xl mx-auto px-4 -mt-8 h-full">
  <div v-if="selected" class="bg-white rounded-3xl shadow-lg p-8 mb-12 h-full">
    <!-- 설문 & 리스트 두 개가 나란히 보이도록 설정 -->
    <div class="flex h-full ">
      <!-- 설문 컴포넌트 -->
      <div class="w-full sm:w-1/2 flex-1 h-full">
        <div class="h-full bg-gradient-to-r from-indigo-100 to-blue-50 p-8">
          <TransitionGroup name="fade" mode="out-in">
            <DepositSurvey v-if="selected === 1" :surveyData="store.surveyData.deposit" />
            <SavingSurvey v-if="selected === 2" :surveyData="store.surveyData.saving" />
            <MortgageLoanSurvey v-if="selected === 3" :surveyData="store.surveyData.mortgageLoan" />
            <RentHouseLoanSurvey v-if="selected === 4" :surveyData="store.surveyData.rentHouseLoan" />
          </TransitionGroup>
        </div>
      </div>

      <!-- 리스트 컴포넌트 -->
      <div class="w-full sm:w-1/2 flex-1 h-full">
        <!-- 리스트 높이 및 스크롤 설정 -->
        <div class="h-full overflow-y bg-gray-50 rounded-lg p-4 border">
          <TransitionGroup name="fade" mode="out-in">
            <DepositList v-if="selected === 1" :surveyData="store.surveyData.deposit" />
            <SavingList v-if="selected === 2" :surveyData="store.surveyData.saving" />
            <MortgageLoanList v-if="selected === 3" :surveyData="store.surveyData.mortgageLoan" />
            <RentHouseLoanList v-if="selected === 4" :surveyData="store.surveyData.rentHouseLoan" />
          </TransitionGroup>
        </div>
      </div>
    </div>
  </div>
</div>
</div>


</template>



<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref, computed } from 'vue'
import DepositSurvey from './DepositSurvey.vue';
import SavingSurvey from './SavingSurvey.vue';
import DepositList from './DepositList.vue';
import SavingList from './SavingList.vue';

import MortgageLoanSurvey from '@/components/MortgageLoanSurvey.vue';
import MortgageLoanList from '@/components/MortgageLoanList.vue';
import RentHouseLoanSurvey from '@/components/RentHouseLoanSurvey.vue';
import RentHouseLoanList from '@/components/RentHouseLoanList.vue';

// Store 사용
const store = useCounterStore()

const selected = ref(null)

const categories = [
  {
    id: 1,
    name: '예금',
    description: '안전하게 자산을 늘리세요',
    icon: '💰'
  },
  {
    id: 2,
    name: '적금',
    description: '꾸준한 저축의 시작',
    icon: '🏦'
  },
  {
    id: 3,
    name: '주택담보대출',
    description: '내 집 마련의 첫걸음',
    icon: '🏠'
  },
  {
    id: 4,
    name: '전세자금대출',
    description: '편안한 주거 생활을 위해',
    icon: '🔑'
  }
]

const fetchData = (id) => {
  selected.value = id
}


// const deposit = store.surveyData.deposit


</script>

<style scoped>
.fade-scale-enter-active,
.fade-scale-leave-active,
.fade-slide-up-enter-active,
.fade-slide-up-leave-active,
.fade-slide-down-enter-active,
.fade-slide-down-leave-active {
  transition: all 0.3s ease;
}

.fade-scale-enter-from,
.fade-scale-leave-to {
  opacity: 0;
  transform: scale(0.95);
}

.fade-slide-up-enter-from,
.fade-slide-up-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

.fade-slide-down-enter-from,
.fade-slide-down-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.finance-image {
  max-width: 300px; /* 이미지 너비를 300px로 제한 */
  height: auto; /* 이미지 비율 유지 */
}

.list-container {
  height: 100%;
  max-height: 100%;
  overflow-y: auto;
}
.container {
  width: 1140px;
}


/* 폰트 추가 */

.font_gugi {
    font-family: 'Gugi', sans-serif;
}
.font_roboto {
  font-family: 'Roboto', sans-serif;
}
.font_lora {
  font-family: 'Lora', serif;
}
.font_poppins {
  font-family: 'Poppins', sans-serif;
}
.font_montserrat {
  font-family: 'Montserrat', sans-serif;
}
.font_merriweather {
  font-family: 'Merriweather', serif;
}
.font_open_sans {
  font-family: 'Open Sans', sans-serif;
}
.font_playfair {
  font-family: 'Playfair Display', serif;
}
.font_raleway {
  font-family: 'Raleway', sans-serif;
}
.font_dancing_script {
  font-family: 'Dancing Script', cursive;
}
.font_nunito {
  font-family: 'Nunito', sans-serif;
}
</style>
