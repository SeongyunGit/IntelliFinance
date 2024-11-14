import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import SurveyResponse  # 모델을 가져옵니다.

class SurveyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'survey_results'
        self.room_group_name = f"survey_{self.room_name}"

        # WebSocket 연결이 수립되면, 특정 room group에 가입
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # WebSocket 연결이 종료되면, room group에서 나감
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # WebSocket으로부터 메시지를 수신했을 때
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        response_data = text_data_json['response_data']

        # 응답 데이터 저장 (SurveyResponse 모델에 저장)
        SurveyResponse.objects.create(response_data=response_data)

        # 응답이 추가되었으므로, 결과를 다시 계산해서 전송
        results = self.get_survey_results()  # 결과 계산 함수

        # 결과를 room group에 전송
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_survey_results',
                'results': results
            }
        )

    # room group으로부터 메시지를 받으면 클라이언트로 전송
    async def send_survey_results(self, event):
        results = event['results']
        await self.send(text_data=json.dumps({
            'results': results
        }))

    def get_survey_results(self):
        # 설문 결과 계산 로직 작성 (예: 각 선택지에 대한 응답 비율 계산)
        return {
            'question_1': {'매우 만족': 50, '만족': 30, '보통': 20},
            'question_2': {'매우 높다': 60, '높다': 25, '보통': 15}
        }