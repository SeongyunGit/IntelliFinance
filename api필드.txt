from django.db import models

#############################################################################################################################################

# 은행리스트(company)
class companyList(models.Model):
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 예: "202410"
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융회사 번호
    kor_co_nm = models.CharField(max_length=100, null=True, blank=True)  # 금융기관명
    dcls_chrg_man = models.TextField(null=True, blank=True)  # 담당자 정보
    homp_url = models.URLField(null=True, blank=True)  # 홈페이지 URL
    cal_tel = models.CharField(max_length=20, null=True, blank=True)  # 고객센터 전화번호

    def __str__(self):
        return self.kor_co_nm

# 은행리스트(company) 옵션
class companyListOption(models.Model):
    deposit_product = models.ForeignKey(companyList, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 예: "202410"
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융회사 번호
    area_cd = models.CharField(max_length=2, null=True, blank=True)  # 지역 코드
    area_nm = models.CharField(max_length=20, null=True, blank=True)  # 지역명
    exis_yn = models.CharField(max_length=1, null=True, blank=True)  # 존재 여부 (Y/N)

    def __str__(self):
        return f"{self.area_nm} ({self.exis_yn})"

#############################################################################################################################################

# 정기예금(Deposit)
class DepositProduct(models.Model):
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 예: "202410"
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융회사 번호
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True)  # 금융상품 코드
    kor_co_nm = models.CharField(max_length=100, null=True, blank=True)  # 금융기관명
    fin_prdt_nm = models.CharField(max_length=200, null=True, blank=True)  # 상품명
    join_way = models.CharField(max_length=255, null=True, blank=True)  # 가입 방법
    mtrt_int = models.TextField(null=True, blank=True)  # 만기 후 이자
    spcl_cnd = models.TextField(null=True, blank=True)  # 특별 조건
    join_deny = models.CharField(max_length=1, null=True, blank=True)  # 가입 제한
    join_member = models.CharField(max_length=100, null=True, blank=True)  # 가입 대상
    etc_note = models.TextField(null=True, blank=True)  # 기타 참고사항
    max_limit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # 최대 한도
    dcls_strt_day = models.DateField(null=True, blank=True)  # 공시 시작일
    dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일
    fin_co_subm_day = models.DateTimeField(null=True, blank=True)  # 금융기관 제출일

    def __str__(self):
        return self.fin_prdt_nm

# 정기예금(Deposit) 옵션
class DepositProductOption(models.Model):
    deposit_product = models.ForeignKey(DepositProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 예: "202410"
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True)
    intr_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 이자율 유형 (S: 단리 등)
    intr_rate_type_nm = models.CharField(max_length=10, null=True, blank=True)  # 이자율 유형 이름 (예: "단리")
    save_trm = models.CharField(max_length=2, null=True, blank=True)  # 예: "1", "3", "6", "12"
    # intr_rate와 intr_rate2에 NULL 허용
    intr_rate = models.FloatField(null=True, blank=True)  # NULL을 허용하도록 변경
    intr_rate2 = models.FloatField(null=True, blank=True)  # NULL을 허용하도록 변경

    def __str__(self):
        return f"{self.fin_prdt_cd} - {self.save_trm}개월"

#############################################################################################################################################

# 적금(saving)
class SavingProduct(models.Model):
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 예: "202410"
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융회사 번호
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True)  # 금융상품 코드
    kor_co_nm = models.CharField(max_length=100, null=True, blank=True)  # 금융기관명
    fin_prdt_nm = models.CharField(max_length=200, null=True, blank=True)  # 상품명
    join_way = models.CharField(max_length=255, null=True, blank=True)  # 가입 방법
    mtrt_int = models.TextField(null=True, blank=True)  # 만기 후 이자
    spcl_cnd = models.TextField(null=True, blank=True)  # 특별 조건
    join_deny = models.CharField(max_length=1, null=True, blank=True)  # 가입 제한
    join_member = models.CharField(max_length=100, null=True, blank=True)  # 가입 대상
    etc_note = models.TextField(null=True, blank=True)  # 기타 참고사항
    max_limit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # 최대 한도
    dcls_strt_day = models.DateField(null=True, blank=True)  # 공시 시작일
    dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일
    fin_co_subm_day = models.DateTimeField(null=True, blank=True)  # 금융기관 제출일

    def __str__(self):
        return self.fin_prdt_nm

# 적금(saving) 옵션
class SavingProductOption(models.Model):
    installment_product = models.ForeignKey(SavingProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 예: "202410"
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True)
    intr_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 이자율 유형 (S: 단리 등)
    intr_rate_type_nm = models.CharField(max_length=10, null=True, blank=True)  # 이자율 유형 이름 (예: "단리")
    rsrv_type = models.CharField(max_length=1, null=True, blank=True)  # 적립식 종류 (정액적립식/자유적립식)
    rsrv_type_nm = models.CharField(max_length=20, null=True, blank=True)  # 적립식 종류 이름
    save_trm = models.CharField(max_length=2, null=True, blank=True)  # 예: "12", "24", "36" (개월)
    intr_rate = models.FloatField(null=True, blank=True)  # 기본 금리
    intr_rate2 = models.FloatField(null=True, blank=True)  # 우대 금리

    def __str__(self):
        return f"{self.fin_prdt_cd} - {self.save_trm}개월"

#############################################################################################################################################

# 연금저축(annuitySaving)
class annuitySavingProduct(models.Model):
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

# 연금저축(annuitySaving) 옵션
class annuitySavingProductOption(models.Model):
    deposit_product = models.ForeignKey(annuitySavingProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
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

#############################################################################################################################################

# 주택담보(MortgageLoan)
class mortgageLoanProduct(models.Model):
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

# 주택담보(MortgageLoan) 옵션
class mortgageLoanProductOption(models.Model):
    loan_product = models.ForeignKey(mortgageLoanProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    mrtg_type = models.CharField(max_length=2, null=True, blank=True)  # 담보 유형 (예: 아파트, 주택 등)
    mrtg_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 담보 유형 명 (예: 아파트)
    rpay_type = models.CharField(max_length=1, null=True, blank=True)  # 상환 방식 (예: D -> 분할상환)
    rpay_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 상환 방식 명
    lend_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 금리 유형 (예: F -> 고정금리)
    lend_rate_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 금리 유형 명
    lend_rate_min = models.FloatField(null=True, blank=True)  # 최소 금리
    lend_rate_max = models.FloatField(null=True, blank=True)  # 최대 금리
    lend_rate_avg = models.FloatField(null=True, blank=True)  # 평균 금리

    def __str__(self):
        return f"{self.loan_product.fin_prdt_nm} - {self.mrtg_type_nm} 옵션"
#############################################################################################################################################

# 전세자금대출(JeonseLoan)
class rentHouseLoanProduct(models.Model):
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

# 전세자금대출(JeonseLoan) 옵션
class rentHouseLoanProductOption(models.Model):
    loan_product = models.ForeignKey(rentHouseLoanProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    rpay_type = models.CharField(max_length=1, null=True, blank=True)  # 상환 방식 (예: S -> 만기일시상환)
    rpay_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 상환 방식 명
    lend_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 금리 유형 (예: F -> 고정금리)
    lend_rate_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 금리 유형 명
    lend_rate_min = models.FloatField(null=True, blank=True)  # 최소 금리
    lend_rate_max = models.FloatField(null=True, blank=True)  # 최대 금리
    lend_rate_avg = models.FloatField(null=True, blank=True)  # 평균 금리

    def __str__(self):
        return f"{self.loan_product.fin_prdt_nm} - {self.rpay_type_nm} 옵션"

#############################################################################################################################################

# 개인신용대출(PersonalCreditLoan)
class creditLoanProduct(models.Model):
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

# 개인신용대출(PersonalCreditLoan) 옵션
class creditLoanProductOption(models.Model):
    loan_product = models.ForeignKey(creditLoanProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
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

#############################################################################################################################################
