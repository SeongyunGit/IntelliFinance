from rest_framework import serializers
from .models import SurveyResult

class SurveyResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResult
        fields = ['question', 'total_responses', 'aggregated_data']