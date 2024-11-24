<template>
  <div class="max-w-4xl mx-auto p-8 bg-white rounded-xl shadow-lg">
    <!-- 환율 계산기 -->
    <div class="mb-12">
      <h2 class="text-3xl font-semibold text-center mb-6 text-gray-900">환율 계산기</h2>
      <form class="space-y-6">
        <!-- 국가 선택 -->
        <div class="flex items-center justify-between">
          <label for="currency" class="w-1/4 text-lg font-medium text-gray-700">국가 선택:</label>
          <select v-model="selectedCurrency" id="currency" class="w-3/4 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 ease-in-out">
            <option v-for="(currency, index) in store.exchangelist" :key="index" :value="currency.cur_unit">
              {{ currency.cur_nm }} ({{ currency.cur_unit }})
            </option>
          </select>
        </div>

        <!-- 원화 금액 입력 -->
        <div class="flex items-center justify-between">
          <label for="amount" class="w-1/4 text-lg font-medium text-gray-700">입력 금액 (원화):</label>
          <input type="number" v-model="amount" id="amount" placeholder="원화 금액" class="w-3/4 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 ease-in-out" />
        </div>

        <!-- 변환된 금액 (외국 통화) -->
        <div class="flex items-center justify-between">
          <label for="convertedAmount" class="w-1/4 text-lg font-medium text-gray-700">변환된 금액:</label>
          <input type="number" :value="convertedAmount" disabled id="convertedAmount" class="w-3/4 p-3 bg-gray-100 border border-gray-300 rounded-lg focus:outline-none" />
        </div>

        <!-- 외국 통화 금액 입력 -->
        <div class="flex items-center justify-between">
          <label for="foreignAmount" class="w-1/4 text-lg font-medium text-gray-700">입력 금액 (외국 통화):</label>
          <input type="number" v-model="foreignAmount" id="foreignAmount" placeholder="외국 통화 금액" class="w-3/4 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 ease-in-out" />
        </div>

        <!-- 변환된 원화 금액 -->
        <div class="flex items-center justify-between">
          <label for="convertedWon" class="w-1/4 text-lg font-medium text-gray-700">변환된 원화 금액:</label>
          <input type="number" :value="convertedWon" disabled id="convertedWon" class="w-3/4 p-3 bg-gray-100 border border-gray-300 rounded-lg focus:outline-none" />
        </div>
      </form>
    </div>

    <!-- 환율 막대 그래프 -->
    <div class="mb-12">
      <h2 class="text-2xl font-semibold text-center mb-6 text-gray-900">환율 막대 그래프</h2>
      <BarChart :data="chartData" />
    </div>

    <!-- 환율 표로 표시 -->
    <h1 class="text-2xl font-semibold mb-6 text-center text-gray-900">환율표</h1>
    <table class="min-w-full table-auto border-collapse border border-gray-300 bg-white shadow-md rounded-lg">
      <thead class="bg-gray-200">
        <tr>
          <th class="px-6 py-4 text-left text-lg font-medium text-gray-700">통화 이름</th>
          <th class="px-6 py-4 text-left text-lg font-medium text-gray-700">기준 환율 (BKPR)</th>
          <th class="px-6 py-4 text-left text-lg font-medium text-gray-700">매매 기준율</th>
          <th class="px-6 py-4 text-left text-lg font-medium text-gray-700">매입율 (TTB)</th>
          <th class="px-6 py-4 text-left text-lg font-medium text-gray-700">매도율 (TTS)</th>
          <th class="px-6 py-4 text-left text-lg font-medium text-gray-700">업데이트 날짜</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in store.exchangelist" :key="index" class="hover:bg-gray-100">
          <td class="px-6 py-4 text-gray-700">{{ item.cur_nm }}({{ item.cur_unit }})</td>
          <td class="px-6 py-4 text-gray-700">{{ item.bkpr }}</td>
          <td class="px-6 py-4 text-gray-700">{{ item.deal_bas_r }}</td>
          <td class="px-6 py-4 text-gray-700">{{ item.ttb }}</td>
          <td class="px-6 py-4 text-gray-700">{{ item.tts }}</td>
          <td class="px-6 py-4 text-gray-700">{{ formatDate(item.updated_at) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script setup>
import { onMounted, ref, watch, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

// Chart.js 모듈 등록
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const store = useCounterStore()

// 환율 계산에 필요한 데이터
const selectedCurrency = ref('USD') // 선택된 통화
const amount = ref(1000) // 원화 입력
const foreignAmount = ref(1) // 외국 통화 입력

// 괄호 안의 숫자 추출 함수
const extractCurrencyUnitMultiplier = (currencyUnit) => {
  const match = currencyUnit.match(/\((\d+)\)/)
  return match ? parseInt(match[1]) : 1 // 괄호 안의 숫자를 반환, 없으면 1을 반환
}

// 변환된 금액 계산
const convertedAmount = computed(() => {
  if (amount.value && selectedCurrency.value) {
    const currency = store.exchangelist.find(item => item.cur_unit === selectedCurrency.value)
    let currencyValue = parseFloat(currency.bkpr.replace(/,/g, ''))
    const multiplier = extractCurrencyUnitMultiplier(currency.cur_unit) // 괄호 안의 숫자 추출
    currencyValue = currencyValue / multiplier // BKPR을 괄호 안 숫자로 나누기
    if (currency) {
      return (amount.value / currencyValue).toFixed(2) // 원화 -> 선택된 외국 통화
    }
  }
  return 0
})

const convertedWon = computed(() => {
  if (foreignAmount.value && selectedCurrency.value) {
    const currency = store.exchangelist.find(item => item.cur_unit === selectedCurrency.value)
    let currencyValue = parseFloat(currency.bkpr.replace(/,/g, ''))
    const multiplier = extractCurrencyUnitMultiplier(currency.cur_unit) // 괄호 안의 숫자 추출
    currencyValue = currencyValue / multiplier // BKPR을 괄호 안 숫자로 나누기
    if (currency) {
      return (foreignAmount.value * currencyValue).toFixed(2) // 외국 통화 -> 원화
    }
  }
  return 0
})

const chartData = ref({
  labels: [], // 통화 이름
  datasets: [
    {
      label: 'TTB',
      data: [], // TTB 데이터
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1,
    },
    {
      label: 'TTS',
      data: [], // TTS 데이터
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
    },
    {
      label: '매매기준율 (deal_bas_r)',
      data: [], // deal_bas_r 데이터
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1,
    },
  ],
})

// 날짜 포맷 함수
const formatDate = (dateString) => {
  return dateString.split('T')[0]; // "2024-11-25T00:30:51.281990+09:00" -> "2024-11-25"
};

onMounted(() => {
  // store.getexchange()
})

watch(
  () => store.exchangelist,
  (newData) => {
    if (newData && newData.length) {
      chartData.value.labels = newData.map(item => `${item.cur_nm}(${item.cur_unit})`)
      // 데이터 변환: 쉼표 제거 후 숫자로 변환
      chartData.value.datasets[0].data = newData.map(item => {
        const multiplier = extractCurrencyUnitMultiplier(item.cur_unit)
        return Number(item.ttb.replace(/,/g, '')) / multiplier
      })
      chartData.value.datasets[1].data = newData.map(item => {
        const multiplier = extractCurrencyUnitMultiplier(item.cur_unit)
        return Number(item.tts.replace(/,/g, '')) / multiplier
      })
      chartData.value.datasets[2].data = newData.map(item => {
        const multiplier = extractCurrencyUnitMultiplier(item.cur_unit)
        return Number(item.deal_bas_r.replace(/,/g, '')) / multiplier
      })
    }
  },
  { immediate: true }
)

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      display: true,
    },
    title: {
      display: true,
      text: '환율 막대 그래프',
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      min: 0,
      max: 2000, // 기본 최대값 (필요시 동적 업데이트 가능)
    },
  },
}
</script>

<script>
// Chart.js 막대 그래프 컴포넌트
export default {
  components: {
    BarChart: Bar,
  },
}
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
  font-weight: bold;
}

form {
  margin-bottom: 20px;
}

label {
  margin-right: 10px;
}

input {
  padding: 5px;
  margin: 5px;
  width: 200px;
}
</style>
