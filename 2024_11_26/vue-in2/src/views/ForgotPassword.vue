<template>
  <div>
    <div class="min-h-screen bg-gray-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-md w-full space-y-8">
        <div class="bg-white shadow-lg rounded-lg p-8">
          <!-- Header -->
          <div class="text-center">
            <h2 class="text-2xl font-bold text-gray-900">Reset Your Password</h2>
            <p class="mt-2 text-sm text-gray-600">
              Enter your email address to receive a password reset link.
            </p>
          </div>

          <!-- Form -->
          <form class="mt-8 space-y-6" @submit.prevent="requestReset">
            <!-- Email Input -->
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
              <div class="mt-1">
                <input 
                  type="email" 
                  id="email" 
                  v-model.trim="email" 
                  required
                  class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-400 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" 
                  placeholder="you@example.com"
                >
              </div>
            </div>

            <!-- Submit Button -->
            <div>
              <button type="submit"
                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                Send Reset Link
              </button>
            </div>
          </form>
        </div>

        <!-- Redirect to Login -->
        <p class="mt-6 text-center text-sm text-gray-600">
          Remember your password? 
          <RouterLink to="/login" class="font-medium text-indigo-600 hover:text-indigo-500">Sign In</RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      email: ''
    }
  },
  methods: {
    async requestReset() {
      try {
        console.log('Sending request with email:', this.email);  // 디버깅용
        
        const response = await axios.post('http://127.0.0.1:8000/accounts/password/reset/', {
          email: this.email
        });
        
        console.log('Response:', response);  // 디버깅용
        alert('비밀번호 재설정 링크가 이메일로 전송되었습니다.');
        
      } catch (error) {
        console.error('Error:', error);  // 디버깅용
        
        const errorMessage = error.response?.data?.error || '서버 오류가 발생했습니다.';
        alert(errorMessage);
      }
    }
  }
}
</script>