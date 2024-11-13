from django.db import models

class LoanProduct(models.Model):
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 공시 월
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융 회사 번호
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True)  # 상품 코드
    kor_co_nm = models.CharField(max_length=100, null=True, blank=True)  # 금융 기관명
    fin_prdt_nm = models.CharField(max_length=200, null=True, blank=True)  # 대출 상품명
    join_way = models.CharField(max_length=255, null=True, blank=True)  # 가입 방법
    loan_inci_expn = models.TextField(null=True, blank=True)  # 대출 인지세 및 기타 비용
    erly_rpay_fee = models.TextField(null=True, blank=True)  # 조기 상환 수수료
    dly_rate = models.TextField(null=True, blank=True)  # 연체 금리
    loan_lmt = models.TextField(null=True, blank=True)  # 대출 한도
    dcls_strt_day = models.DateField(null=True, blank=True)  # 공시 시작일
    dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일
    fin_co_subm_day = models.DateTimeField(null=True, blank=True)  # 금융 회사 제출일

    def __str__(self):
        return self.fin_prdt_nm

class LoanProductOption(models.Model):
    loan_product = models.ForeignKey(LoanProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    rpay_type = models.CharField(max_length=1, null=True, blank=True)  # 상환 방식 (예: S -> 만기일시상환)
    rpay_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 상환 방식 명
    lend_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 금리 유형 (예: F -> 고정금리)
    lend_rate_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 금리 유형 명
    lend_rate_min = models.FloatField(null=True, blank=True)  # 최소 금리
    lend_rate_max = models.FloatField(null=True, blank=True)  # 최대 금리
    lend_rate_avg = models.FloatField(null=True, blank=True)  # 평균 금리

    def __str__(self):
        return f"{self.loan_product.fin_prdt_nm} - {self.rpay_type_nm} 옵션"
