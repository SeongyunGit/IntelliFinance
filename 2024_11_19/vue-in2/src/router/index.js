import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Company from '@/views/Company.vue'
import Update from '@/views/Update.vue'
import Deposit from '@/views/Deposit.vue'
// import DepositListItemItemoptions from '@/components/DepositListItemItemoptions.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import { useCounterStore } from '@/stores/counter'

import Announcement from '@/views/Announcement.vue'
import ForgotPassword from '@/views/ForgotPassword.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView,
    },
    {
      path: '/company',
      name: 'company',
      component: Company,
    },
    {
      path: '/update',
      name: 'update',
      component: Update,
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: Deposit,
      // children: [
      //   { path: 'options', name: 'deposit_options', component: DepositListItemItemoptions },
      // ],
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/announcement',
      name: 'Announcement',
      component: Announcement,
    },
    {
      path: '/login/forgot-password',
      name: 'ForgotPassword',
      component: ForgotPassword,
    }
  ],
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  // 만약 이동하는 목적지가 메인 페이지이면서
  // 현재 로그인 상태가 아니라면 로그인 페이지로 보냄
  // if (to.name === 'HomeView' && !store.isLogin) {
  //   window.alert('로그인이 필요합니다.')
  //   return { name: 'LogInView' }
  // }

  // 만약 로그인 사용자가 회원가입 또는 로그인 페이지로 이동하려고 하면
  // 메인 페이지로 보냄
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 되어있습니다.')
    return { name: 'HomeView' }
  }
})

export default router