import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Company from '@/views/Company.vue'
import SaveDate from '@/views/SaveDate.vue'
import DeleteDate from '@/views/DeleteDate.vue'
import Deposit from '@/views/Deposit.vue'

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
      path: '/save',
      name: 'save',
      component: SaveDate,
    },
    {
      path: '/delete',
      name: 'delete',
      component: DeleteDate,
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: Deposit,
    },
  ],
})

export default router
