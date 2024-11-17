import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Company from '@/views/Company.vue'
import Update from '@/views/Update.vue'
import Deposit from '@/views/Deposit.vue'
// import DepositListItemItemoptions from '@/components/DepositListItemItemoptions.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
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
  ],
})

export default router
