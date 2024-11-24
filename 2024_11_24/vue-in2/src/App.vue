<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const logOut = function () {
  store.logOut()
}
import { ref } from 'vue';

const isChatbotVisible = ref(false);

// 챗봇 열기/닫기 토글 함수
const toggleChatbot = () => {
  isChatbotVisible.value = !isChatbotVisible.value;
};

</script>

<template>
  <!-- 고정된 버튼 -->
  <button class="footer-fixed" @click="toggleChatbot">
    💬 Chat
  </button>

  <!-- 블러 처리된 메인 화면 -->
  <div :class="{ 'blurred': isChatbotVisible }">
    <header>
      <nav class="bg-white border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between items-center h-16">
            <!-- 로고 -->
            <div class="flex-shrink-0">
              <a href="/" class="text-2xl font-bold text-indigo-600">
                <RouterLink to="/">Home</RouterLink>
              </a>
            </div>

            <!-- 메뉴 -->
            <div class="hidden md:flex space-x-4">
              <RouterLink to="/depositview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
                예금
              </RouterLink>
              <RouterLink to="/savingview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
                적금
              </RouterLink>
              <RouterLink to="/mortgageview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
                전세 자금 대출
              </RouterLink>
              <RouterLink to="/renthouseview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
                주택 담보 대출
              </RouterLink>
              <RouterLink to="/company" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
                Bank
              </RouterLink>
              <RouterLink to="/mapview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
                지도
              </RouterLink>
              <RouterLink to="/announcement" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
                공지사항
              </RouterLink>
            </div>
            <div class="hidden md:flex items-center space-x-4" v-if="!store.isLogin">
        <a href="/login" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          <RouterLink to="/login">login</RouterLink>
        </a>
        <a href="/signup" class="bg-indigo-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-indigo-700">
          <RouterLink to="/signup">Signup</RouterLink>
        </a>
      </div>
      <div class="hidden md:flex items-center space-x-4" v-else>
        <a href="/mypage"  class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          <RouterLink to="/mypage">mypage</RouterLink>
        </a>
        <form @submit.prevent="logOut">
          <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-indigo-700">
            Logout
          </button>
        </form>
      </div>
          </div>
        </div>
      </nav>
      <RouterView />
    </header>
  </div>

  <!-- 챗봇 화면 -->
  <div v-if="isChatbotVisible" class="chatbot-overlay">
    <div class="chatbot-container">
      <div class="chat-box">
      <div class="messages">
        <!-- 사용자 메시지 -->
        <div v-if="store.userMessage" class="message user-message">
          <p>{{ store.userMessage }}</p>
        </div>
        <!-- 챗봇의 응답 -->
        <div v-if="store.botReply" class="message bot-message">
          <p>{{ store.botReply }}</p>
        </div>
      </div>
      <!-- 메시지 입력 -->
      <input 
        v-model="store.userMessage"
        type="text" 
        placeholder="Type a message..."
        :disabled="store.isLoading"
      />
      <button @click="store.sendMessage()" :disabled="store.isLoading || !store.userMessage.trim()">Send</button>
    </div>

    <!-- 로딩 표시 -->
    <div v-if="store.isLoading" class="loading">Loading...</div>
      <button @click="toggleChatbot">닫기</button>
    </div>
  </div>
</template>

<style>
/* 고정된 버튼 */
.footer-fixed {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 50%;
  font-size: 16px;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* 블러 처리 */
.blurred {
  filter: blur(5px); /* 블러 효과 */
  pointer-events: none; /* 상호작용 방지 */
}

/* 챗봇 오버레이 */
.chatbot-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 반투명 배경 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

/* 챗봇 컨테이너 */
.chatbot-container {
  width: 400px;
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  text-align: center;
}
.chat-box {
  display: flex;
  flex-direction: column;
}

.messages {
  max-height: 400px;
  overflow-y: auto;
}

.message {
  margin: 10px 0;
  padding: 10px;
  border-radius: 5px;
}

.user-message {
  background-color: #e0f7fa;
  align-self: flex-start;
}

.bot-message {
  background-color: #f1f8e9;
  align-self: flex-end;
}

input[type="text"] {
  padding: 10px;
  margin: 10px 0;
  width: 100%;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.loading {
  text-align: center;
  font-size: 16px;
  color: #007bff;
}
</style>
