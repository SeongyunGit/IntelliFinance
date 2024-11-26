<template>
  <div>
        <!-- 댓글 목록 헤더 -->
        <h4 class="text-2xl font-bold text-gray-800 mb-6 pb-2 border-b border-gray-200">
      댓글 목록 ({{ bank.fin_prdt_nm }})
    </h4>

    <!-- 댓글 리스트 -->
    <div
      v-for="(comment, index) in paginatedComments"
      :key="comment.id"
      class="mb-6 bg-white rounded-xl shadow-sm hover:shadow-md transition-all duration-300 overflow-hidden border border-gray-100"
    >
      <div class="relative p-6">
        <!-- 댓글 번호와 작성일 -->
        <div class="flex items-center gap-3 mb-4">
          <div class="bg-gradient-to-r from-blue-500 to-blue-600 rounded-full w-10 h-10 flex items-center justify-center">
            <span class="text-white font-medium">
              {{ filteredComments.length - ((currentPage - 1) * commentsPerPage + index) }}
            </span>
          </div>
          <div class="flex flex-col">
            <span class="text-gray-500 text-sm">{{ formatDate(comment.created_at) }}</span>
          </div>
        </div>

        <!-- 별점 -->
        <div class="inline-flex items-center gap-2 px-3 py-1.5 bg-gray-50 rounded-lg mb-4">
          <span class="text-gray-600 text-sm font-medium">평점:</span>
          <div class="flex">
            <span
              v-for="n in 5"
              :key="n"
              class="text-xl"
              :class="{
                'text-yellow-400': comment.star >= n,
                'text-gray-200': comment.star < n,
              }"
            >
              ★
            </span>
          </div>
        </div>

        <!-- 댓글 내용 -->
        <p class="text-gray-700 leading-relaxed bg-gray-50 p-4 rounded-xl">
          {{ comment.comment }}
        </p>

        <!-- 삭제 버튼 -->
        <button
          v-if="comment.user === store.mPK"
          @click="store.commentsDelete(comment.id)"
          class="absolute top-4 right-4 px-3 py-1.5 text-sm font-medium text-red-500 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors duration-200"
        >
          삭제
        </button>
      </div>
    </div>

    <!-- 페이지네이션 -->
    <div v-if="totalPages > 1" class="flex justify-center items-center gap-2 mt-8">
      <!-- 이전 페이지 그룹 -->
      <button
        v-if="paginationStart > 1"
        @click="prevPageGroup"
        class="px-3 py-2 rounded-lg border border-gray-200 hover:bg-gray-50 text-gray-600"
      >
        &laquo;
      </button>

      <!-- 페이지 번호 -->
      <button
        v-for="page in displayedPages"
        :key="page"
        @click="currentPage = page"
        class="px-4 py-2 rounded-lg transition-colors duration-200"
        :class="{
          'bg-blue-500 text-white': currentPage === page,
          'hover:bg-gray-50 text-gray-600 border border-gray-200': currentPage !== page
        }"
      >
        {{ page }}
      </button>

      <!-- 다음 페이지 그룹 -->
      <button
        v-if="paginationEnd < totalPages"
        @click="nextPageGroup"
        class="px-3 py-2 rounded-lg border border-gray-200 hover:bg-gray-50 text-gray-600"
      >
        &raquo;
      </button>
    </div>

    <!-- 댓글 작성 폼 -->
    <div v-if="store.mPK" class="mt-10 bg-white rounded-xl shadow-lg border border-gray-100">
      <div class="p-6 border-b border-gray-100">
        <div class="flex justify-between items-center">
          <span class="text-xl font-bold text-gray-800">댓글 작성</span>
          <div class="flex gap-3">
            <!-- 내 댓글 보기 토글 버튼 추가 -->
            <button
              @click="showMyCommentsOnly = !showMyCommentsOnly"
              class="inline-flex items-center gap-2 px-4 py-2.5 border rounded-lg transition-colors duration-200"
              :class="{
                'bg-gray-100 text-gray-700 border-gray-200': !showMyCommentsOnly,
                'bg-blue-50 text-blue-600 border-blue-200': showMyCommentsOnly
              }"
            >
              <span>내 댓글만 보기</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4"
                :class="{ 'text-blue-500': showMyCommentsOnly }"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                />
              </svg>
            </button>
            
            <!-- 기존 저장 버튼 -->
            <button
              @click="saveComment"
              class="inline-flex items-center gap-2 px-6 py-2.5 bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-lg transition-colors duration-200 focus:ring-2 focus:ring-blue-300 focus:ring-offset-2"
            >
              <span>저장</span>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div class="p-6 space-y-6">
        <!-- 별점 선택 -->
        <div class="flex items-center gap-4 p-4 bg-gray-50 rounded-xl">
          <span class="font-medium text-gray-700">별점 선택</span>
          <div class="flex gap-1">
            <button
              v-for="n in 5"
              :key="n"
              @click="setRating(n)"
              class="text-2xl hover:scale-110 transition-transform duration-200"
              :class="{
                'text-yellow-400': rating >= n,
                'text-gray-200': rating < n,
              }"
            >
              ★
            </button>
          </div>
        </div>

        <!-- 댓글 입력 -->
        <textarea
          v-model="comment"
          class="w-full h-32 p-4 bg-gray-50 border border-gray-200 rounded-xl resize-none focus:ring-2 focus:ring-blue-300 focus:border-transparent transition-all duration-200 placeholder-gray-400"
          placeholder="댓글을 입력해주세요..."
        ></textarea>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useCounterStore } from "@/stores/counter";

// Props로 전달된 은행 데이터
const props = defineProps({
  bank: Object,
});

// 상태 관리
const comment = ref("");
const rating = ref(0);
const currentPage = ref(1);
const commentsPerPage = 5; // 페이지당 댓글 개수
const pagesPerGroup = 5; // 페이지 버튼 그룹 크기

const store = useCounterStore();

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`;
}

// 별점 설정
const setRating = (value) => {
  rating.value = value;
};

// 댓글 저장 함수
const saveComment = () => {
  const data = {
    comment: comment.value,
    star: rating.value,
  };

  if (!data.comment || !data.star) {
    alert("댓글과 별점을 모두 입력해주세요.");
    return;
  }

  console.log("댓글 저장 데이터:", props.bank.id, data);
  store.commentsCreate(props.bank.id, data);

  comment.value = "";
  rating.value = 0;
};

// // 댓글 목록 계산
// const filteredComments = computed(() =>
//   store.coments.comments
//     .filter((item) => item.bank_product === props.bank.id)
//     .sort((a, b) => new Date(b.created_at) - new Date(a.created_at)) // 최신순 정렬
// );

const totalPages = computed(() =>
  Math.ceil(filteredComments.value.length / commentsPerPage)
);

const paginatedComments = computed(() => {
  const start = (currentPage.value - 1) * commentsPerPage;
  const end = start + commentsPerPage;
  return filteredComments.value.slice(start, end);
});

// 페이지네이션 그룹
const paginationStart = computed(() =>
  Math.floor((currentPage.value - 1) / pagesPerGroup) * pagesPerGroup + 1
);
const paginationEnd = computed(() =>
  Math.min(paginationStart.value + pagesPerGroup - 1, totalPages.value)
);

const displayedPages = computed(() => {
  const pages = [];
  for (let i = paginationStart.value; i <= paginationEnd.value; i++) {
    pages.push(i);
  }
  return pages;
});

// 페이지 그룹 이동
const prevPageGroup = () => {
  currentPage.value = paginationStart.value - pagesPerGroup;
};

const nextPageGroup = () => {
  currentPage.value = paginationEnd.value + 1;
};

const showMyCommentsOnly = ref(false); // 새로운 상태 추가

// 댓글 목록 계산 수정
const filteredComments = computed(() =>
  store.coments.comments
    .filter((item) => {
      const bankMatch = item.bank_product === props.bank.id;
      return showMyCommentsOnly.value
        ? bankMatch && item.user === store.mPK
        : bankMatch;
    })
    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
);
</script>

<style scoped>
/* 필요에 따라 추가 스타일 작성 */
</style>
