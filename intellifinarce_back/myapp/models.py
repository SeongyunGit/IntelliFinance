from django.db import models

# 공통 정보 (금융상품 기본 정보)
class FinancialProduct(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('D', '예금'),
        ('S', '적금'),
        ('L', '대출'),
    ]
    
    fin_co_no = models.CharField(max_length=7)  # 금융기관 코드
    fin_prdt_cd = models.CharField(max_length=7)  # 금융상품 코드
    kor_co_nm = models.CharField(max_length=255)  # 금융기관 이름
    fin_prdt_nm = models.CharField(max_length=255)  # 금융상품 이름
    prdt_type = models.CharField(max_length=1, choices=PRODUCT_TYPE_CHOICES)  # 예금, 적금, 대출 구분
    join_way = models.CharField(max_length=255)  # 가입 방법
    mtrt_int = models.TextField()  # 만기 후 이자
    spcl_cnd = models.TextField()  # 특별 조건
    join_deny = models.BooleanField(default=False)  # 가입 제한 여부
    join_member = models.CharField(max_length=255)  # 가입 가능 대상
    etc_note = models.TextField()  # 기타 사항
    max_limit = models.IntegerField(null=True, blank=True)  # 최고 한도 (적용되지 않는 경우 null)
    dcls_strt_day = models.DateField()  # 공시 시작일
    dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일
    fin_co_subm_day = models.DateTimeField()  # 금융기관 제출일
    
    def __str__(self):
        return f"{self.kor_co_nm} - {self.fin_prdt_nm}"
        
# 설문 응답을 위한 추가적인 테이블
class SurveyResponse(models.Model):
    financial_product = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE)  # 금융상품과 연결
    user_name = models.CharField(max_length=255)  # 사용자 이름
    user_age = models.IntegerField()  # 사용자 나이
    user_income = models.IntegerField()  # 사용자 연소득
    satisfaction_level = models.IntegerField()  # 만족도 (1~5 점수)
    remarks = models.TextField()  # 의견 또는 기타 사항
    response_date = models.DateTimeField(auto_now_add=True)  # 설문 응답일
    
    def __str__(self):
        return f"{self.user_name} - {self.financial_product.fin_prdt_nm} - {self.satisfaction_level}"
    
class Survey(models.Model):
    survey_type = models.CharField(max_length=100)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, related_name='responses', on_delete=models.CASCADE)
    response_data = models.JSONField()  # 응답을 JSON 형태로 저장
    created_at = models.DateTimeField(auto_now_add=True)