<template>
  <div class="bg-gradient-to-b from-indigo-600 to-indigo-500 pb-12">
    <!-- Carousel 섹션 추가 -->
    <div class="max-w-6xl mx-auto px-4 pt-8 pb-12">
      <div class="relative">
        <!-- Carousel 컨테이너 -->
        <div class="overflow-hidden rounded-2xl">
          <div class="flex transition-transform duration-500 ease-in-out" 
               :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
            <!-- Carousel 아이템들 -->
            <div v-for="(slide, index) in slides" :key="index" class="w-full flex-shrink-0">
              <div class="relative h-[400px]">
                <img :src="slide.image" :alt="slide.title" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
                  <div class="text-center text-white px-6">
                    <h2 class="text-4xl font-bold mb-4">{{ slide.title }}</h2>
                    <p class="text-xl">{{ slide.description }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 네비게이션 버튼 -->
        <button @click="prevSlide" class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-white/80 p-2 rounded-full">
          <span class="text-2xl">←</span>
        </button>
        <button @click="nextSlide" class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-white/80 p-2 rounded-full">
          <span class="text-2xl">→</span>
        </button>
        
        <!-- 인디케이터 -->
        <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
          <button v-for="(_, index) in slides" 
                  :key="index"
                  @click="currentSlide = index"
                  :class="{'bg-white': currentSlide === index, 'bg-white/50': currentSlide !== index}"
                  class="w-3 h-3 rounded-full">
          </button>
        </div>
      </div>
    </div>
</div>


  <div class="bg-gradient-to-b from-indigo-600 to-indigo-500 pb-12">
    <!-- 메인 섹션 -->
    <div class="bg-gradient-to-b from-indigo-600 to-indigo-500 pb-12">
      <div class="max-w-6xl mx-auto px-4 pt-8">
        <h3 class="font_roboto text-4xl font-bold montserrat text-white text-center mb-12">💡 맞춤형 금융상품 찾기 💡</h3>
        
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
    <div class="flex h-[195vh]">
      <!-- 설문 컴포넌트 -->
      <div class="w-full sm:w-1/2 flex-1">
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
      <div class="w-full sm:w-1/2 flex-1">
        <!-- 리스트 높이 및 스크롤 설정 -->
        <div class="h-full bg-gray-50 rounded-lg p-8 border overflow-y-scroll">
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
import { ref, computed, onMounted } from 'vue'
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

import smart from '@/assets/smart.jpg'
import fit from '@/assets/fit.jpg'
import invest from '@/assets/invest.jpg'
const currentSlide = ref(0);
const slides = ref([
  {
    image: smart,  // 실제 이미지 경로로 수정 필요
    title: '똑똑한 자산관리의 시작',
    description: '당신의 미래를 위한 최적의 금융 솔루션'
  },
  {
    image: fit,  // 실제 이미지 경로로 수정 필요
    title: '맞춤형 금융상품 추천',
    description: '빅데이터 기반 개인 맞춤 금융상품'
  },
  {
    image: invest,  // 실제 이미지 경로로 수정 필요
    title: '안전한 투자의 시작',
    description: '검증된 금융상품으로 안전하게'
  }
]);

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % slides.value.length;
};

const prevSlide = () => {
  currentSlide.value = currentSlide.value === 0 
    ? slides.value.length - 1 
    : currentSlide.value - 1;
};

// 자동 슬라이드 (선택사항)
onMounted(() => {
  setInterval(nextSlide, 5000); // 5초마다 다음 슬라이드로
});

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

.overflow-y-auto {
  /* 스크롤바 너비 */
  scrollbar-width: thin;
  
  /* 웹킷 브라우저용 스크롤바 스타일링 */
  &::-webkit-scrollbar {
    width: 6px;
  }
  
  &::-webkit-scrollbar-track {
    background: #f1f1f1;
  }
  
  &::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 3px;
  }
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
