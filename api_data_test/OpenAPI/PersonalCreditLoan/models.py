from django.db import models

class LoanProduct(models.Model):
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 공시 월
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융 회사 번호
    fin_prdt_cd = models.CharField(max_length=100, null=True, blank=True)  # 상품 코드
    crdt_prdt_type = models.CharField(max_length=1, null=True, blank=True)  # 신용 대출 종류 (예: 1: 일반신용대출)
    kor_co_nm = models.CharField(max_length=100, null=True, blank=True)  # 금융 기관명
    fin_prdt_nm = models.CharField(max_length=200, null=True, blank=True)  # 대출 상품명
    join_way = models.CharField(max_length=255, null=True, blank=True)  # 가입 방법
    cb_name = models.CharField(max_length=255, null=True, blank=True)  # 신용 평가 기관 (예: NICE, KCB)
    crdt_prdt_type_nm = models.CharField(max_length=100, null=True, blank=True)  # 신용대출 종류명
    dcls_strt_day = models.DateField(null=True, blank=True)  # 공시 시작일
    dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일
    fin_co_subm_day = models.DateTimeField(null=True, blank=True)  # 금융 회사 제출일

    def __str__(self):
        return self.fin_prdt_nm


class LoanProductOption(models.Model):
    loan_product = models.ForeignKey(LoanProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    crdt_lend_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 금리 유형 (예: A: 대출금리)
    crdt_lend_rate_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 금리 유형명
    crdt_grad_1 = models.FloatField(null=True, blank=True)  # 신용등급 1에 대한 금리
    crdt_grad_4 = models.FloatField(null=True, blank=True)  # 신용등급 4에 대한 금리
    crdt_grad_5 = models.FloatField(null=True, blank=True)  # 신용등급 5에 대한 금리
    crdt_grad_6 = models.FloatField(null=True, blank=True)  # 신용등급 6에 대한 금리
    crdt_grad_10 = models.FloatField(null=True, blank=True)  # 신용등급 10에 대한 금리
    crdt_grad_11 = models.FloatField(null=True, blank=True)  # 신용등급 11에 대한 금리
    crdt_grad_12 = models.FloatField(null=True, blank=True)  # 신용등급 12에 대한 금리
    crdt_grad_13 = models.FloatField(null=True, blank=True)  # 신용등급 13에 대한 금리
    crdt_grad_avg = models.FloatField(null=True, blank=True)  # 평균 금리

    def __str__(self):
        return f"{self.loan_product.fin_prdt_nm} - {self.crdt_lend_rate_type_nm} 옵션"
