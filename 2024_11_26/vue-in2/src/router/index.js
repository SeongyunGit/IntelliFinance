import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Company from '@/views/Company.vue'
import Update from '@/views/Update.vue'
// import DepositListItemItemoptions from '@/components/DepositListItemItemoptions.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import { useCounterStore } from '@/stores/counter'

import Announcement from '@/views/Announcement.vue'
import ForgotPassword from '@/views/ForgotPassword.vue'
import Mypage from '@/views/Mypage.vue'
import DepositView from '@/views/DepositView.vue'
import SavingView from '@/views/SavingView.vue'
import MortgageView from '@/views/MortgageView.vue'
import RentHouseView from '@/views/RentHouseView.vue'
import MapView from '@/views/MapView.vue'
import Exchange from '@/views/Exchange.vue'

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
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: Mypage,
    },
    {
      path: '/depositview',
      name: 'depositview',
      component: DepositView,
    },
    {
      path: '/savingview',
      name: 'savingview',
      component: SavingView,
    },
    {
      path: '/mortgageview',
      name: 'mortgageview',
      component: MortgageView,
    },
    {
      path: '/renthouseview',
      name: 'renthouseview',
      component: RentHouseView,
    },
    {
      path: '/mapview',
      name: 'mapview',
      component: MapView,
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: Exchange,
    },
  ],
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  // 만약 이동하는 목적지가 메인 페이지이면서
  // 현재 로그인 상태가 아니라면 로그인 페이지로 보냄
//   if (to.name === 'HomeView' && !store.isLogin) {
//     window.alert('로그인이 필요합니다.')
//     return { name: 'LogInView' }
//  }

  // 만약 로그인 사용자가 회원가입 또는 로그인 페이지로 이동하려고 하면
  // 메인 페이지로 보냄
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 되어있습니다.')
    return { name: 'HomeView' }
  }
})

export default router
