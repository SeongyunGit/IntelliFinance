<template>
  <div>
    <!-- 댓글 출력 -->
    <h4 class="text-lg font-semibold mt-6">댓글 목록</h4>

    <!-- 댓글 리스트 -->
    <div
      v-for="comment in paginatedComments"
      :key="comment.id"
      class="p-4 border border-gray-200 rounded-md bg-gray-50 flex justify-between items-center"
    >
      <!-- 댓글 내용 -->
      <div>
        <!-- 별점 출력 -->
        <div class="flex space-x-1">
          <span
            v-for="n in 5"
            :key="n"
            class="text-2xl"
            :class="{
              'text-yellow-400': comment.star >= n,
              'text-gray-300': comment.star < n,
            }"
          >
            ★
          </span>
        </div>

        <!-- 댓글 텍스트 -->
        <p class="text-gray-800 mt-2">{{ comment.comment }}</p>
        <span class="text-gray-800 text-sm mt-2 text-gray-500">{{ comment.created_at }}</span>
      </div>

      <!-- 삭제 버튼 -->
      <button
        v-if="comment.user === store.mPK"
        @click="store.commentsDelete(comment.id)"
        class="text-red-500 font-bold"
      >
        ❌
      </button>
    </div>

    <!-- 페이지네이션 -->
    <div class="flex justify-center mt-4 space-x-2">
      <!-- 이전 버튼 -->
      <button
        v-if="paginationStart > 1"
        @click="prevPageGroup"
        class="px-4 py-2 bg-gray-200 rounded-md hover:bg-gray-300 text-gray-600"
      >
        이전
      </button>

      <!-- 페이지 번호 버튼 -->
      <button
        v-for="page in displayedPages"
        :key="page"
        @click="currentPage = page"
        :class="{
          'bg-blue-500 text-white': currentPage === page,
          'bg-gray-200 text-gray-600': currentPage !== page,
        }"
        class="px-4 py-2 rounded-md hover:bg-blue-600"
      >
        {{ page }}
      </button>

      <!-- 다음 버튼 -->
      <button
        v-if="paginationEnd < totalPages"
        @click="nextPageGroup"
        class="px-4 py-2 bg-gray-200 rounded-md hover:bg-gray-300 text-gray-600"
      >
        다음
      </button>
    </div>

    <!-- 댓글 작성 -->
    <div v-if="store.mPK" class="p-6 bg-white shadow rounded-md">
      <span class="text-xl font-bold mb-4">댓글 작성</span>
      <!-- 저장 버튼 -->
      <button
        @click="saveComment"
        class="mt-4 bg-blue-500 text-white py-1 px-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300"
      >
        저장
      </button>

      <!-- 별점 입력 -->
      <div class="flex items-center space-x-2 mt-2">
        <span class="font-semibold">별점:</span>
        <div class="flex">
          <button
            v-for="n in 5"
            :key="n"
            @click="setRating(n)"
            class="text-2xl"
            :class="{
              'text-yellow-400': rating >= n,
              'text-gray-300': rating < n,
            }"
          >
            ★
          </button>
        </div>
      </div>

      <!-- 댓글 입력 -->
      <textarea
        v-model="comment"
        class="w-full h-20 p-2 border border-gray-300 rounded-md resize-none focus:ring focus:ring-blue-300"
        placeholder="댓글을 입력하세요"
      ></textarea>
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
const pagesPerGroup = 10; // 페이지 버튼 그룹 크기

const store = useCounterStore();

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

// 댓글 목록 계산
const filteredComments = computed(() =>
  store.coments.comments
    .filter((item) => item.bank_product === props.bank.id)
    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at)) // 최신순 정렬
);

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
</script>

<style scoped>
/* 필요에 따라 추가 스타일 작성 */
</style>
