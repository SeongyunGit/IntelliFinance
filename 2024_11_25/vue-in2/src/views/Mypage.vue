<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-4xl">
      <!-- 헤더 -->
      <h1 class="text-4xl font-semibold text-center text-gray-800 mb-8">My Page</h1>

      <!-- 사용자 정보 -->
      <div class="space-y-6">
        <div class="flex justify-between text-lg">
          <span class="font-medium text-gray-700">Name</span>
          <span class="text-gray-500">{{ store.Uname }}</span>
        </div>
        <div class="flex justify-between text-lg">
          <span class="font-medium text-gray-700">Email</span>
          <span class="text-gray-500">{{ store.Uemail }}</span>
        </div>
      </div>
      

      <!-- deposit, saving, mortgageLoan, rentHouseLoan 각각 처리 -->
      <div v-for="(list, index) in lists" :key="index" class="mt-8">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">{{ list.korea }}</h2>
        
        <!-- 환율 막대 그래프 -->
        <div class="mb-12">
          <p v-if="list.name === 'deposit'">기본금리</p>
          <LineChart v-if="list.name === 'deposit'" :data="chartData_deposit1" />
          <p v-if="list.name === 'deposit'">우대금리</p>
          <LineChart v-if="list.name === 'deposit'" :data="chartData_deposit2" />
          <p v-if="list.name === 'saving'">기본금리</p>
          <LineChart v-if="list.name === 'saving'" :data="chartData_saving1" />
          <p v-if="list.name === 'saving'">우대금리</p>
          <LineChart v-if="list.name === 'saving'" :data="chartData_saving2" />
          <LineChart v-if="list.name === 'mortgageLoan'" :data="chartData_mortgageLoan" />
          <LineChart v-if="list.name === 'rentHouseLoan'" :data="chartData_rentHouseLoan" />
        </div>

        <!-- 카드 슬라이드 -->
        <div class="relative overflow-hidden">
          <!-- 좌측 버튼 -->
          <button
            @click="scrollLeft(index)"
            class="absolute left-0 top-1/2 transform -translate-y-1/2 z-10 bg-gray-800 text-white p-2 rounded-full hover:bg-gray-600 focus:outline-none"
            :disabled="currentIndices[index] <= 0"
          >
            &#60;
          </button>

          <!-- 카드들 -->
          
          <div :ref="list.ref" class="flex transition-transform duration-300">
            <div
              v-for="(item, idx) in visibleItems(list.name)"
              :key="idx"
            >
            <div v-if="store.is_liked.liked_articles && store.is_liked.liked_articles.find(bank => bank.id == item.id)" class="bg-white p-6 rounded-lg shadow-md w-64 mx-2">
            <div v-if="item.type_a==list.name">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">{{ item.prdt_name }}</h2>
              <p class="text-gray-500">{{ item.mtrt_int }}</p>
              <p class="text-gray-500">상품 유형: {{ item.type_a }}</p>
            </div>
            <button
              class="mt-2 px-4 py-2 bg-red-100 hover:bg-red-200 rounded-lg text-red-600"
              @click.stop="store.toggleLike(item.id)"
            >
              <div v-if="store.is_liked.liked_articles && store.is_liked.liked_articles.find(bank => bank.id == item.id)">
                {{ "❤️ 좋아요 취소" }}  
              </div>
              <div v-else>
                {{ "🤍 좋아요" }}
              </div> 
            </button>
            </div>
          </div>
        </div>
          
          <!-- 우측 버튼 -->
          <button
            @click="scrollRight(index)"
            class="absolute right-0 top-1/2 transform -translate-y-1/2 z-10 bg-gray-800 text-white p-2 rounded-full hover:bg-gray-600 focus:outline-none" >
            &#62;
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js'

// Chart.js 모듈 등록 (PointElement 추가)
ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

const store = useCounterStore()
onMounted(() => {
  store.visibleItems()
})

// 리스트들의 설정
const lists = [
  { korea:'예금',name: 'deposit', data: store.likeList.filter(type=>type.type_a==='deposit'), ref: 'depositRef' },
  { korea:'적금',name: 'saving', data: store.likeList.filter(type=>type.type_a==='saving'), ref: 'savingRef' },
  { korea:'전세 자금 대출',name: 'mortgageLoan', data: store.likeList.filter(type=>type.type_a==='mortgageLoan'), ref: 'mortgageLoanRef' },
  { korea:'주택 담보 대출',name: 'rentHouseLoan', data: store.likeList.filter(type=>type.type_a==='rentHouseLoan'), ref: 'rentHouseLoanRef' }
];


// 각 리스트에 대한 현재 인덱스 상태
const currentIndices = ref([0, 0, 0, 0]);

// 각 리스트에 대해 보여줄 카드들 계산
const visibleItems = (listName) => {
  const index = lists.findIndex(list => list.name === listName);
  // console.log()
  return lists[index].data.slice(currentIndices.value[index], currentIndices.value[index] + 4);
};


// 오른쪽으로 스크롤
const scrollRight = (index) => {
  if (currentIndices.value[index] + 4 < lists[index].data.length) {
    currentIndices.value[index]++;
  }
};

// 왼쪽으로 스크롤
const scrollLeft = (index) => {
  if (currentIndices.value[index] > 0) {
    currentIndices.value[index]--;
  }
};

///////////////////////////////////////////////////////////////////
const chartData_deposit_namelist = ref([])
const chartData_deposit1 = ref({
  // 상품 이름
  labels: ['1개월', '3개월', '6개월', '12개월', '24개월', '36개월'], // 기간
  datasets: [],
});

// chartData_deposit_namelist의 변경을 감지하여 datasets 업데이트
const updateChartData1 = () => {
  // datasets를 초기화 (기존 데이터를 지우고 새로 추가)
  chartData_deposit1.value.datasets = [];

  // chartData_deposit_namelist의 길이만큼 datasets 항목을 생성
  chartData_deposit_namelist.value.forEach((item, index) => {
    chartData_deposit1.value.datasets.push({
      label: item.prdt_name,  // label에 상품 이름을 넣음
      data: item.intr_rate,  // 해당 데이터는 나중에 추가
      backgroundColor: `rgba(${(index*161)%256}, ${(index*99)%256}, ${(index*131)%256}, 0.2)`,  // 색상 예시
      borderColor: `rgba(${(index*161)%256}, ${(index*99)%256}, ${(index*131)%256}, 1)`,  // 선 색상 예시
      borderWidth: 1,
      fill: false,  // 선 그래프 설정
    });
  });
};

const chartData_deposit2 = ref({
  // 상품 이름
  labels: ['1개월', '3개월', '6개월', '12개월', '24개월', '36개월'], // 상품 이름
  datasets: [],
});

// chartData_deposit_namelist 변경을 감지하여 datasets 업데이트
const updateChartData2 = () => {
  // datasets를 초기화 (기존 데이터를 지우고 새로 추가)
  chartData_deposit2.value.datasets = [];

  // chartData_deposit_namelist 길이만큼 datasets 항목을 생성
  chartData_deposit_namelist.value.forEach((item, index) => {
    chartData_deposit2.value.datasets.push({
      label: item.prdt_name,  // label에 상품 이름을 넣음
      data: item.intr_rate2,  // 해당 데이터는 나중에 추가
      backgroundColor: `rgba(${(index*161)%256}, ${(index*99)%256}, ${(index*131)%256}, 0.2)`,  // 색상 예시
      borderColor: `rgba(${(index*161)%256}, ${(index*99)%256}, ${(index*131)%256}, 1)`,  // 선 색상 예시
      borderWidth: 1,
      fill: false,  // 선 그래프 설정
    });
  });
};

const chartData_saving1_namelist = ref([])
const chartData_saving1 = ref({
  // 상품 이름
  labels: ['1개월', '3개월', '6개월', '12개월', '24개월', '36개월'], // 상품 이름
  datasets: [],
});

// chartData_saving1_namelist 변경을 감지하여 datasets 업데이트
const updateChartData3 = () => {
  // datasets를 초기화 (기존 데이터를 지우고 새로 추가)
  chartData_saving1.value.datasets = [];

  // chartData_saving1_namelist 길이만큼 datasets 항목을 생성
  chartData_saving1_namelist.value.forEach((item, index) => {
    chartData_saving1.value.datasets.push({
      label: item.prdt_name,  // label에 상품 이름을 넣음
      data: item.intr_rate,  // 해당 데이터는 나중에 추가
      backgroundColor: `rgba(${(index*161)%256}, ${(index*99)%256}, ${(index*131)%256}, 0.2)`,  // 색상 예시
      borderColor: `rgba(${(index*161)%256}, ${(index*99)%256}, ${(index*131)%256}, 1)`,  // 선 색상 예시
      borderWidth: 1,
      fill: false,  // 선 그래프 설정
    });
  });
};

const chartData_saving2 = ref({
  // 상품 이름
  labels: ['1개월', '3개월', '6개월', '12개월', '24개월', '36개월'], // 상품 이름
  datasets: [],
});

// chartData_saving1_namelist 변경을 감지하여 datasets 업데이트
const updateChartData4 = () => {
  // datasets를 초기화 (기존 데이터를 지우고 새로 추가)
  chartData_saving2.value.datasets = [];

  // chartData_saving1_namelist 길이만큼 datasets 항목을 생성
  chartData_saving1_namelist.value.forEach((item, index) => {
    chartData_saving2.value.datasets.push({
      label: item.prdt_name,  // label에 상품 이름을 넣음
      data: item.intr_rate2,  // 해당 데이터는 나중에 추가
      backgroundColor: `rgba(${(index*161)%256}, ${(index*99)%256}, ${(index*131)%256}, 0.2)`,  // 색상 예시
      borderColor: `rgba(${(index*161)%256}, ${(index*99)%256}, ${(index*131)%256}, 1)`,  // 선 색상 예시
      borderWidth: 1,
      fill: false,  // 선 그래프 설정
    });
  });
};

const chartData_mortgageLoan = ref({
  // 상품 이름
  labels: [], // 상품 이름

  datasets: [
    // 최소, 최대, 평균 데이터
    {
      label: '최소',  // 최소 금리
      data: [],  // 최소 금리 데이터
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1,
      fill: false,  // 선 그래프에 맞게 수정
    },
    {
      label: '최대',  // 최대 금리
      data: [],  // 최대 금리 데이터
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
      fill: false,  // 선 그래프에 맞게 수정
    },
    // {
    //   label: '평균',  // 평균 금리
    //   data: [],  // 평균 금리 데이터
    //   backgroundColor: 'rgba(75, 192, 192, 0.2)',
    //   borderColor: 'rgba(75, 192, 192, 1)',
    //   borderWidth: 1,
    //   fill: false,  // 선 그래프에 맞게 수정
    // },
  ],
});

const chartData_rentHouseLoan = ref({
  // 상품 이름
  labels: [], // 상품 이름

  datasets: [
    // 최소, 최대, 평균 데이터
    {
      label: '최소',  // 최소 금리
      data: [],  // 최소 금리 데이터
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1,
      fill: false,  // 선 그래프에 맞게 수정
    },
    {
      label: '최대',  // 최대 금리
      data: [],  // 최대 금리 데이터
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
      fill: false,  // 선 그래프에 맞게 수정
    },
    // {
    //   label: '평균',  // 평균 금리
    //   data: [],  // 평균 금리 데이터
    //   backgroundColor: 'rgba(75, 192, 192, 0.2)',
    //   borderColor: 'rgba(75, 192, 192, 1)',
    //   borderWidth: 1,
    //   fill: false,  // 선 그래프에 맞게 수정
    // },
  ],
});

watch(
  () => store.likeList,
  (newData) => {
    if (newData && newData.length) {
      // deposit 기본금리, 우대금리
      chartData_deposit_namelist.value = newData
        .filter(item => item.type_a === 'deposit') // 'deposit'인 항목만 필터링
        .map(item => ({
          prdt_name: item.prdt_name,  // 상품 이름
          intr_rate: item.intr_rate,
          intr_rate2: item.intr_rate2,
        }))
      updateChartData1()
      updateChartData2()

      // saving 기본금리, 우대금리
      chartData_saving1_namelist.value = newData
        .filter(item => item.type_a === 'saving') // 'saving'인 항목만 필터링
        .map(item => ({
          prdt_name: item.prdt_name,  // 상품 이름
          intr_rate: item.intr_rate,
          intr_rate2: item.intr_rate2,
        }))
      updateChartData3()
      updateChartData4()

      // mortgageLoan 기본금리
      chartData_mortgageLoan.value.labels = newData
        .filter(item => item.type_a === 'mortgageLoan') // 'mortgageLoan'인 항목만 필터링
        .map(item => `${item.prdt_name}`)           // 필터링된 항목에 대해 map 수행
      chartData_mortgageLoan.value.datasets[0].data = newData
        .filter(item => item.type_a === 'mortgageLoan')
        .map(item => item.lend_rate_min[0])
      chartData_mortgageLoan.value.datasets[1].data = newData
        .filter(item => item.type_a === 'mortgageLoan')
        .map(item => item.lend_rate_max[0])
      // chartData_mortgageLoan.value.datasets[2].data = newData
      //   .filter(item => item.type_a === 'mortgageLoan')
      //   .map(item => item.lend_rate_avg[0])

      // rentHouseLoan 기본금리
      chartData_rentHouseLoan.value.labels = newData
        .filter(item => item.type_a === 'rentHouseLoan') // 'rentHouseLoan'인 항목만 필터링
        .map(item => `${item.prdt_name}`)           // 필터링된 항목에 대해 map 수행
      chartData_rentHouseLoan.value.datasets[0].data = newData
        .filter(item => item.type_a === 'rentHouseLoan')
        .map(item => item.lend_rate_min[0])
      chartData_rentHouseLoan.value.datasets[1].data = newData
        .filter(item => item.type_a === 'rentHouseLoan')
        .map(item => item.lend_rate_max[0])
      // chartData_rentHouseLoan.value.datasets[2].data = newData
      //   .filter(item => item.type_a === 'rentHouseLoan')
      //   .map(item => item.lend_rate_avg[0])
    }
  },
  { immediate: true }
)
</script>

<script>
// Chart.js 막대 그래프 컴포넌트
export default {
  components: {
    LineChart: Line,
  },
}
</script>

<style scoped>
/* 추가 스타일은 이곳에 작성 */
</style>
