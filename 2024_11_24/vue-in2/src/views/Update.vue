<template>
  <div>
    <h1>Bank update</h1>
    <p>데이터 업데이트(삭제후 다시 저장)</p>
    
    <!-- 각각의 버튼에 클릭 이벤트 추가 -->
    <button @click="deleteData">삭제</button>
    <br>
    <button @click="getDeposit">입금 데이터 요청</button>
    <br>
    <button @click="getSaving">예금 데이터 요청</button>
    <br>
    <button @click="getMortgageLoan">주택 담보 대출 데이터 요청</button>
    <br>
    <button @click="getRentHouseLoan">전세 대출 데이터 요청</button>
    <br>
    <button @click="getCompany2">다른 회사 데이터 요청</button>

    <!-- 테스트용버튼 -->
    <br>
    <button @click="commentsCreate(2)">댓글 작성 요청</button>
    <br>
    <button @click="commentsDelete(3)">댓글 삭제 요청</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

// 각 버튼에 해당하는 함수들
const deleteData = () => {
  store.delete_data() // 삭제 함수
}

const getDeposit = () => {
  store.getdeposit()  // 입금 데이터 요청
}

const getSaving = () => {
  store.getsaving()   // 예금 데이터 요청
}

const getMortgageLoan = () => {
  store.getmortgageLoan() // 주택 담보 대출 데이터 요청
}

const getRentHouseLoan = () => {
  store.getrentHouseLoan() // 전세 대출 데이터 요청
}

const getCompany2 = () => {
  store.getcompany2() // 다른 회사 데이터 요청
}


// 임시 테스트용 함수
const commentsCreate = (product_pk) => {
  store.commentsCreate(product_pk)
}
const commentsDelete = (comment_pk) => {
  store.commentsDelete(comment_pk)
}
</script>

<style scoped>
</style>
