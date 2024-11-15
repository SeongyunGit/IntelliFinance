import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const companyList = ref([])
  const companyListOption = ref([])
  const integrationProducts = ref([])
  const integrationProductOptions = ref([])

  const API_URL = 'http://127.0.0.1:8000'
  
  const getCompany = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/get_combined_company_data/`,
    })
      .then((response) => {
        // console.log(response.data)
        companyList.value = response.data.companyList
        companyListOption.value = response.data.companyListOption
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getIntegration = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/get_combined_integration_data/`,
    })
      .then((response) => {
        // console.log(response.data)
        integrationProducts.value = response.data.integrationProducts
        integrationProductOptions.value = response.data.integrationProductOptions
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getdeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/deposit/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getsaving = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/saving/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getmortgageLoan = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/mortgageLoan/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getrentHouseLoan = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/rentHouseLoan/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const delete_data = function () {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/delete_product_data/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  
  return { companyList, companyListOption, 
    integrationProducts, integrationProductOptions, 
    API_URL, 
    getCompany, getIntegration,
    getdeposit, getsaving, getmortgageLoan, getrentHouseLoan, 
    delete_data
   }
}, { persist: true })
