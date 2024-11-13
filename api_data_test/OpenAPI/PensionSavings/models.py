from django.db import models

class DepositProduct(models.Model):
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 예: "202010"
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융회사 번호
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True)  # 금융상품 코드
    kor_co_nm = models.CharField(max_length=100, null=True, blank=True)  # 금융기관명
    fin_prdt_nm = models.CharField(max_length=200, null=True, blank=True)  # 상품명
    join_way = models.CharField(max_length=255, null=True, blank=True)  # 가입 방법
    prdt_type = models.CharField(max_length=3, null=True, blank=True)  # 상품 종류 코드
    prdt_type_nm = models.CharField(max_length=100, null=True, blank=True)  # 상품 종류 이름
    avg_prft_rate = models.FloatField(null=True, blank=True)  # 평균 수익률
    btrm_prft_rate_1 = models.FloatField(null=True, blank=True)  # 1년 실적 수익률
    btrm_prft_rate_2 = models.FloatField(null=True, blank=True)  # 2년 실적 수익률
    btrm_prft_rate_3 = models.FloatField(null=True, blank=True)  # 3년 실적 수익률
    sale_co = models.TextField(null=True, blank=True)  # 판매 회사
    sale_strt_day = models.DateField(null=True, blank=True)  # 판매 시작일
    dcls_strt_day = models.DateField(null=True, blank=True)  # 공시 시작일
    dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일
    fin_co_subm_day = models.DateTimeField(null=True, blank=True)  # 금융기관 제출일

    def __str__(self):
        return self.fin_prdt_nm


class DepositProductOption(models.Model):
    deposit_product = models.ForeignKey(DepositProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 예: "202010"
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융회사 번호
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True)  # 금융상품 코드
    pnsn_recp_trm = models.CharField(max_length=1, null=True, blank=True)  # 연금 수령 기간
    pnsn_recp_trm_nm = models.CharField(max_length=50, null=True, blank=True)  # 연금 수령 기간 이름
    pnsn_entr_age = models.IntegerField(null=True, blank=True)  # 연금 가입 나이
    pnsn_entr_age_nm = models.CharField(max_length=10, null=True, blank=True)  # 연금 가입 나이 이름
    mon_paym_atm = models.CharField(max_length=10, null=True, blank=True)  # 월 납입 금액
    mon_paym_atm_nm = models.CharField(max_length=50, null=True, blank=True)  # 월 납입 금액 이름
    paym_prd = models.CharField(max_length=2, null=True, blank=True)  # 납입 기간 (예: 10년)
    paym_prd_nm = models.CharField(max_length=50, null=True, blank=True)  # 납입 기간 이름
    pnsn_strt_age = models.IntegerField(null=True, blank=True)  # 연금 수령 나이
    pnsn_strt_age_nm = models.CharField(max_length=10, null=True, blank=True)  # 연금 수령 나이 이름
    pnsn_recp_amt = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # 연금 수령 금액

    def __str__(self):
        return f"{self.fin_prdt_cd} - {self.pnsn_recp_trm_nm} 옵션"
