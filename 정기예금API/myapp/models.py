from django.db import models

class DepositProduct(models.Model):
    dcls_month = models.CharField(max_length=6)  # 예: "202410"
    fin_co_no = models.CharField(max_length=7)  # 금융회사 번호
    fin_prdt_cd = models.CharField(max_length=20)  # 금융상품 코드
    kor_co_nm = models.CharField(max_length=100)  # 금융기관명
    fin_prdt_nm = models.CharField(max_length=200)  # 상품명
    join_way = models.CharField(max_length=255)  # 가입 방법
    mtrt_int = models.TextField()  # 만기 후 이자
    spcl_cnd = models.TextField()  # 특별 조건
    join_deny = models.CharField(max_length=1)  # 가입 제한
    join_member = models.CharField(max_length=100)  # 가입 대상
    etc_note = models.TextField()  # 기타 참고사항
    max_limit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # 최대 한도
    dcls_strt_day = models.DateField()  # 공시 시작일
    dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일
    fin_co_subm_day = models.DateTimeField()  # 금융기관 제출일

    def __str__(self):
        return self.fin_prdt_nm


class DepositProductOption(models.Model):
    deposit_product = models.ForeignKey(DepositProduct, related_name="options", on_delete=models.CASCADE)
    dcls_month = models.CharField(max_length=6)  # 예: "202410"
    fin_co_no = models.CharField(max_length=7)
    fin_prdt_cd = models.CharField(max_length=20)
    intr_rate_type = models.CharField(max_length=1)  # 이자율 유형 (S: 단리 등)
    intr_rate_type_nm = models.CharField(max_length=10)  # 이자율 유형 이름 (예: "단리")
    save_trm = models.CharField(max_length=2)  # 예: "1", "3", "6", "12"
    # intr_rate와 intr_rate2에 NULL 허용
    intr_rate = models.FloatField(null=True, blank=True)  # NULL을 허용하도록 변경
    intr_rate2 = models.FloatField(null=True, blank=True) # NULL을 허용하도록 변경

    def __str__(self):
        return f"{self.fin_prdt_cd} - {self.save_trm}개월"


