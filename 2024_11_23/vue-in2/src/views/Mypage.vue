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
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">{{ list.name }}</h2>
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
              class="bg-white p-6 rounded-lg shadow-md w-64 mx-2"
            >
            <div v-if="item.type_a==list.name">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">{{ item.name }}</h2>
              <p class="text-gray-500">{{ item.mtrt_int }}</p>
              <p class="text-gray-500">상품 유형: {{ item.type_a }}</p>
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
import { ref, computed, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
onMounted(() => {
  store.visibleItems()
})

// 각 리스트 데이터 정의
// const deposit = [
//   { title: "deposit1", coment: "내용1" },
//   { title: "deposit2", coment: "내용2" },
//   { title: "deposit3", coment: "내용3" },
//   { title: "deposit4", coment: "내용4" },
//   { title: "deposit5", coment: "내용5" },
//   { title: "deposit6", coment: "내용6" },
// ];

// const saving = [
//   { title: "saving1", coment: "내용1" },
//   { title: "saving2", coment: "내용2" },
//   { title: "saving3", coment: "내용3" },
//   { title: "saving4", coment: "내용4" },
//   { title: "saving5", coment: "내용5" },
//   { title: "saving6", coment: "내용6" },
// ];

// const mortgageLoan = [
//   { title: "mortgageLoan1", coment: "내용1" },
//   { title: "mortgageLoan2", coment: "내용2" },
//   { title: "mortgageLoan3", coment: "내용3" },
//   { title: "mortgageLoan4", coment: "내용4" },
//   { title: "mortgageLoan5", coment: "내용5" },
//   { title: "mortgageLoan6", coment: "내용6" },
// ];

// const rentHouseLoan = [
//   { title: "rentHouseLoan1", coment: "내용1" },
//   { title: "rentHouseLoan2", coment: "내용2" },
//   { title: "rentHouseLoan3", coment: "내용3" },
//   { title: "rentHouseLoan4", coment: "내용4" },
//   { title: "rentHouseLoan5", coment: "내용5" },
//   { title: "rentHouseLoan6", coment: "내용6" },
// ];

// 리스트들의 설정
const lists = [
  { name: 'deposit', data: store.likeList.filter(type=>type.type_a==='deposit'), ref: 'depositRef' },
  { name: 'saving', data: store.likeList.filter(type=>type.type_a==='saving'), ref: 'savingRef' },
  { name: 'mortgageLoan', data: store.likeList.filter(type=>type.type_a==='mortgageLoan'), ref: 'mortgageLoanRef' },
  { name: 'rentHouseLoan', data: store.likeList.filter(type=>type.type_a==='rentHouseLoan'), ref: 'rentHouseLoanRef' }
];


// 각 리스트에 대한 현재 인덱스 상태
const currentIndices = ref([0, 0, 0, 0]);

// 각 리스트에 대해 보여줄 카드들 계산
const visibleItems = (listName) => {
  const index = lists.findIndex(list => list.name === listName);
  console.log()
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
</script>

<style scoped>
/* 추가 스타일은 이곳에 작성 */
</style>
