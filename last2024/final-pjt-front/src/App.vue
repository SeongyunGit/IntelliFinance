<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue';
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

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getCompany()
})

</script>

<template>
  <!-- 고정된 버튼 -->
  <button class="footer-fixed" @click="toggleChatbot">
    <span class="chat-icon">💬</span>
</button>
  <!-- 블러 처리된 메인 화면 -->
  <div :class="{ 'blurred': isChatbotVisible }">
    <header class="bg-gradient-to-b from-indigo-600 to-indigo-500">
      <nav class="bg-white border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between items-center h-16">
            <!-- 로고 -->
            <div class="flex-shrink-0">
              <a href="/" class="text-2xl font-bold text-indigo-600">
                <RouterLink to="/">INTELLIFINANCE</RouterLink>
              </a>
            </div>

            <!-- 메뉴 -->
            <div class="hidden md:flex space-x-4">
              <RouterLink to="/depositview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
                예금
              </RouterLink>
              <RouterLink to="/savingview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
                적금
              </RouterLink>
              <RouterLink to="/mortgageview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
                전세 자금 대출
              </RouterLink>
              <RouterLink to="/renthouseview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
                주택 담보 대출
              </RouterLink>
              <RouterLink to="/company" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
                은행
              </RouterLink>
              <RouterLink to="/exchange" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
                환율
              </RouterLink>
              <RouterLink to="/mapview" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
                지도
              </RouterLink>
              <RouterLink to="/announcement" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
                공지사항
              </RouterLink>
            </div>
            <div class="hidden md:flex items-center space-x-4" v-if="!store.isLogin">
        <a href="/login" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
          <RouterLink to="/login">login</RouterLink>
        </a>
        <a href="/signup" class="bg-indigo-600 text-white px-4 py-2 rounded-md font-bold font_poppins hover:bg-indigo-700">
          <RouterLink to="/signup">Signup</RouterLink>
        </a>
      </div>
      <div class="hidden md:flex items-center space-x-4" v-else>
        <a href="/mypage"  class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md font-bold font_poppins">
          <RouterLink to="/mypage">mypage</RouterLink>
        </a>
        <form @submit.prevent="logOut">
          <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md font-bold font_poppins hover:bg-indigo-700">
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
  <div v-if="isChatbotVisible" class="chatbot-overlay fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="chatbot-container bg-white rounded-xl shadow-xl w-full max-w-md mx-4 overflow-hidden">
      
      <!-- 헤더 -->
      <div class="chat-box-header bg-indigo-600 px-4 py-3 flex justify-between items-center">
        <h3 class="text-white font-semibold">AI 챗봇</h3>
        <button @click="toggleChatbot" class="text-white hover:bg-indigo-700 rounded-full p-1">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- 메시지 영역 -->
      <div class="messages h-96 px-4 py-3 overflow-y-auto bg-gray-50 space-y-4">
        
        <!-- 사용자 메시지 -->
        <div v-if="store.userMessage" class="message user-message flex justify-end">
          <div class="max-w-[70%]">
            <div class="bg-indigo-600 text-white px-4 py-2 rounded-2xl rounded-tr-sm">
              <p class="text-sm">{{ store.userMessage }}</p>
            </div>
          </div>
        </div>

        <!-- 봇 메시지 -->
        <div v-if="store.botReply" class="message bot-message flex justify-start">
          <div class="max-w-[70%]">
            <div class="bg-white border text-gray-700 px-4 py-2 rounded-2xl rounded-tl-sm shadow-sm">
              <p class="text-sm">{{ store.botReply }}</p>
            </div>
          </div>
        </div>

        <!-- 로딩 표시 -->
        <div v-if="store.isLoading" class="loading flex justify-start mt-4">
          <div class="bg-white border px-4 py-2 rounded-2xl rounded-tl-sm shadow-sm">
            <div class="flex space-x-2">
              <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
              <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
              <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.4s"></div>
            </div>
          </div>
        </div>

      </div>

      <!-- 메시지 입력 -->
      <div class="message-input px-4 py-3 bg-white border-t">
        <div class="flex space-x-2">
          <input 
            v-model="store.userMessage"
            type="text" 
            placeholder="Type a message..."
            class="flex-1 px-4 py-2 border rounded-full focus:outline-none focus:border-indigo-600 text-sm"
            :disabled="store.isLoading"
            @keyup.enter="store.sendMessage()"
          />
          <button 
            @click="store.sendMessage()" 
            :disabled="store.isLoading || !store.userMessage.trim()"
            class="bg-indigo-600 text-white px-4 py-2 rounded-full hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
</div>
</template>

<style>
/* 고정된 버튼 */
.footer-fixed {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  background-color: #0078D4; /* 챗봇 버튼의 기본 색상 */
  color: white;
  border: none;
  border-radius: 50%;
  font-size: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
}

.footer-fixed:hover {
  background-color: #005A9E; /* 호버 시 버튼 색상 변경 */
  transform: translateY(-4px); /* 호버 시 살짝 떠오르는 효과 */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* 그림자 크기 증가 */
}

.chat-icon {
  font-size: 30px; /* 아이콘의 크기 조정 */
  color: #0078D4; /* 아이콘을 파란색으로 설정 */
  transition: transform 0.3s ease;
}

.footer-fixed:hover .chat-icon {
  transform: scale(1.2); /* 호버 시 아이콘 크기 증가 */
  color: #005A9E; /* 호버 시 아이콘 색상 변화 */
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
