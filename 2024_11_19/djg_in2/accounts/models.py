from ast import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Announcement(models.Model):
    announcement_title = models.CharField(max_length=50)
    announcement_content = models.CharField(max_length=255)
    announcement_important = models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.announcement_title


# 설문 종합 필드 모델
class Survey(models.Model):
    # 공통 추가 필드
    user = models.ForeignKey(User, related_name="options", on_delete=models.CASCADE, null=True, blank=True) # 설문 작성 유저
    type_a = models.TextField(null=True, blank=True) # 데이터 타입(예: 예금, 적금, 주택담보대출, 전세자금대출)
    today = models.DateField(auto_now=True, auto_now_add=False) # 설문작성날짜

    # 공통 필드
    # fin_co_no = models.CharField(max_length=7, null=True, blank=True)  # 금융 회사 번호
    kor_co_nm = models.JSONField(null=True, blank=True)  # 금융 기관명

    # (예금, 적금) 추가 필드
    # intr_rate_type = models.CharField(max_length=1, null=True, blank=True)  # 이자율 유형 (S: 단리 등)
    intr_rate_type_nm = models.JSONField(null=True, blank=True)  # 이자율 유형 이름 (예: "단리")
    save_trm = models.JSONField(null=True, blank=True)  # 예: "1", "3", "6", "12" (기간)
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

    def __str__(self):
        return self.name