from django.db import models

# 환율 테이블
class CurrencyExchange(models.Model):
    result = models.IntegerField()  # 조회 결과 (1: 성공, 2: DATA코드 오류, 3: 인증코드 오류, 4: 일일제한횟수 마감)
    cur_unit = models.TextField()  # 통화 코드
    cur_nm = models.TextField()  # 국가/통화명
    ttb = models.TextField(null=True, blank=True)  # 전신환(송금) 받으실 때 (TTB)
    tts = models.TextField(null=True, blank=True)  # 전신환(송금) 보내실 때 (TTS)
    deal_bas_r = models.TextField()  # 매매 기준율
    bkpr = models.TextField()  # 장부 가격
    yy_efee_r = models.TextField(default='0')  # 연환가료율
    ten_dd_efee_r = models.TextField(default='0')  # 10일 환가료율
    kftc_deal_bas_r = models.TextField()  # 서울 외국환 중개 매매 기준율
    kftc_bkpr = models.TextField()  # 서울 외국환 중개 장부 가격
    updated_at = models.DateTimeField(auto_now=True)  # 업데이트 날짜 (자동 갱신)

    def __str__(self):
        return self.cur_nm