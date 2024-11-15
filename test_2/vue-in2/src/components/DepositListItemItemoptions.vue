<template>
  <ul>
    <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
            옵션
          </button>
        </h2>
        <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
          <div v-for="option in store.integrationProductOptions">
            <div v-if="option.fin_prdt_cd === bank.fin_prdt_cd">
              <li>
                <p>{{ option.intr_rate_type_nm }}</p>
                <p>기간 : {{ option.save_trm }}</p>
                <p>기본금리 : {{ option.intr_rate }}</p>
                <p>우대금리 : {{ option.intr_rate2 }}</p>
                <hr>
              </li>
            </div>
          </div>
        </div>
      </div>
    </div>
  </ul>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
defineProps({
  bank: Object
})
</script>
<style  scoped>

</style>