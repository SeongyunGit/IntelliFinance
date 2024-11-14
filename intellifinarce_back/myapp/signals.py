from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SurveyResponse, SurveyResult

@receiver(post_save, sender=SurveyResponse)
def update_survey_result(sender, instance, **kwargs):
    question = instance.question
    result, created = SurveyResult.objects.get_or_create(question=question)
    
    # 집계 데이터 업데이트
    result.total_responses += 1
    response_data = instance.response_data

    # 예시로 multiple_choice일 경우 각 옵션의 응답 수를 집계
    if question.question_type == 'multiple_choice':
        choice = response_data.get('choice')
        if choice in result.aggregated_data:
            result.aggregated_data[choice] += 1
        else:
            result.aggregated_data[choice] = 1
    
    result.save()

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

@receiver(post_save, sender=SurveyResponse)
def update_survey_result(sender, instance, **kwargs):
    question = instance.question
    result, created = SurveyResult.objects.get_or_create(question=question)
    
    # 집계 데이터 업데이트
    result.total_responses += 1
    response_data = instance.response_data

    # multiple_choice일 경우 집계
    if question.question_type == 'multiple_choice':
        choice = response_data.get('choice')
        if choice in result.aggregated_data:
            result.aggregated_data[choice] += 1
        else:
            result.aggregated_data[choice] = 1

    result.save()

    # 웹소켓을 통해 실시간 업데이트 전송
    async_to_sync(channel_layer.group_send)(
        f"survey_result_{question.id}", {
            'type': 'send_survey_result',
        }
    )