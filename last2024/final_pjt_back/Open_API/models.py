from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
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

# 상품 종합 테이블
class IntegrationProduct(models.Model):
    # 공통 필드
    dcls_month = models.TextField(null=True, blank=True)  # 공시 월 (예: "202410")
    fin_co_no = models.TextField(null=True, blank=True)  # 금융 회사 번호
    fin_prdt_cd = models.TextField(null=True, blank=True)  # 상품 코드 (금융상품 코드, 대출 상품 코드 등)
    kor_co_nm = models.TextField(null=True, blank=True)  # 금융 기관명
    fin_prdt_nm = models.TextField(null=True, blank=True)  # 상품명 (금융상품명, 대출 상품명 등)
    join_way = models.TextField(null=True, blank=True)  # 가입 방법
    dcls_strt_day = models.TextField(null=True, blank=True)  # 공시 시작일
    dcls_end_day = models.TextField(null=True, blank=True)  # 공시 종료일
    fin_co_subm_day = models.TextField(null=True, blank=True)  # 금융 기관 제출일
    
    # (예금, 적금) 추가 필드
    mtrt_int = models.TextField(null=True, blank=True)  # 만기 후 이자
    spcl_cnd = models.TextField(null=True, blank=True)  # 특별 조건
    join_deny = models.TextField(null=True, blank=True)  # 가입 제한 (Y/N 등)
    join_member = models.TextField(null=True, blank=True)  # 가입 대상
    etc_note = models.TextField(null=True, blank=True)  # 기타 참고사항
    max_limit = models.TextField(null=True, blank=True)  # 최대 한도
    
    # (주택담보대출, 전세자금대출) 추가필드
    loan_inci_expn = models.TextField(null=True, blank=True)  # 대출 인지세 및 기타 비용
    erly_rpay_fee = models.TextField(null=True, blank=True)  # 조기 상환 수수료
    dly_rate = models.TextField(null=True, blank=True)  # 연체 금리
    loan_lmt = models.TextField(null=True, blank=True)  # 대출 한도
    
    # api 필드가 아닌 공통 추가필드
    type_a = models.TextField(null=True, blank=True) # 데이터 타입(예: 예금, 적금, 주택담보대출, 전세자금대출)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_product')
    
    
# 상품옵션 종합 테이블
class IntegrationProductOption(models.Model):
    # 금융 상품 외래키 (예: 예금, 적금, 대출 상품 등)
    deposit_product = models.ForeignKey(IntegrationProduct, related_name="options", on_delete=models.CASCADE, null=True, blank=True)
    
    # 공통 필드 (예금, 적금, 대출(주택,전세))
    dcls_month = models.CharField(max_length=6, null=True, blank=True)  # 공시 월 (예: "202410")
    fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융 회사 번호
    fin_prdt_cd = models.CharField(max_length=20, null=True, blank=True)  # 상품 코드
    
    # (예금, 적금) 추가 필드 
    intr_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 이자율 유형 (S: 단리 등)
    intr_rate_type_nm = models.CharField(max_length=10, null=True, blank=True)  # 이자율 유형 이름 (예: "단리")
    save_trm = models.CharField(max_length=4, null=True, blank=True)  # 예: "1", "3", "6", "12" (기간)
    intr_rate = models.FloatField(null=True, blank=True)  # 기본 금리
    intr_rate2 = models.FloatField(null=True, blank=True)  # 우대 금리 (NULL 허용)

    # (적금) 추가 필드
    rsrv_type = models.CharField(max_length=1, null=True, blank=True)  # 적립식 종류 (정액적립식/자유적립식)
    rsrv_type_nm = models.CharField(max_length=20, null=True, blank=True)  # 적립식 종류 이름

    # (주택담보대출, 전세자금대출) 추가 필드
    rpay_type = models.CharField(max_length=1, null=True, blank=True)  # 상환 방식 (예: D -> 분할상환)
    rpay_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 상환 방식 명
    lend_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 금리 유형 (예: F -> 고정금리)
    lend_rate_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 금리 유형 명
    lend_rate_min = models.FloatField(null=True, blank=True)  # 최소 금리
    lend_rate_max = models.FloatField(null=True, blank=True)  # 최대 금리
    lend_rate_avg = models.FloatField(null=True, blank=True)  # 평균 금리
    
    # (주택 담보) 추가 필드
    mrtg_type = models.CharField(max_length=2, null=True, blank=True)  # 담보 유형 (예: 아파트, 주택 등)
    mrtg_type_nm = models.CharField(max_length=50, null=True, blank=True)  # 담보 유형 명 (예: 아파트)

#############################################################################################################################################
##좋아요 테이블
# class Like(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")  # 좋아요를 누른 사용자
#     bank_product = models.ForeignKey(IntegrationProduct, on_delete=models.CASCADE, related_name="liked_by")  # 좋아요 대상 상품
#     created_at = models.DateTimeField(auto_now_add=True)  # 좋아요 생성 시간

#     class Meta:
#         unique_together = ('user', 'bank_product')

#댓글 테이블
class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")  # 좋아요를 누른 사용자
    bank_product = models.ForeignKey(IntegrationProduct, on_delete=models.CASCADE, related_name="bank_product")  # 좋아요 대상 상품
    star = models.TextField(null=True, blank=True) # 별점
    comment = models.TextField(null=True, blank=True) # 댓글
    created_at = models.DateTimeField(auto_now_add=True)  # 댓글 생성 시간

    # class Meta:
    #     unique_together = ('user', 'bank_product')