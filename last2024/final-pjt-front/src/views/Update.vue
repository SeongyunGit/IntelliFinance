<template>
  <div class="update-container">
    <div class="header">
      <h1>Bank update</h1>
      <p>데이터 업데이트</p>
    </div>

    <div class="button-container">
      <div class="button-group">
        <h2>예금 관련</h2>
        <button @click="getDeposit">입금 데이터 요청</button>
        <button @click="getSaving">예금 데이터 요청</button>
      </div>

      <div class="button-group">
        <h2>대출 관련</h2>
        <button @click="getMortgageLoan">주택 담보 대출 데이터 요청</button>
        <button @click="getRentHouseLoan">전세 대출 데이터 요청</button>
      </div>

      <div class="button-group">
        <h2>기타 정보</h2>
        <button @click="getCompany2">다른 회사 데이터 요청</button>
        <button @click="getexchange2">환율 데이터 요청</button>
      </div>
    </div>
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

const getexchange2 = () => {
  store.getexchange2() // 환율 데이터 요청
}
</script>

<style scoped>
.update-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.header {
  text-align: center;
  margin-bottom: 3rem;
}

.header h1 {
  color: white;
  margin-bottom: 0.5rem;
}

.header p {
  color: white;
}

.button-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.button-group {
  background-color: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.button-group h2 {
  font-size: 1.2rem;
  color: #2c3e50;
  margin-bottom: 1rem;
  text-align: center;
}

button {
  width: 100%;
  padding: 0.8rem;
  margin: 0.5rem 0;
  border: none;
  border-radius: 4px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
}

@media (max-width: 768px) {
  .button-container {
    grid-template-columns: 1fr;
  }
}
</style>

