from rest_framework import serializers
from .models import Daily, Evaluation


class DailySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'date',
            'univ',
            'study',
            'other',
            'first_meet',
            'wanna_do',
            'summary',
            'evaluation',
        )
        model = Daily


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta2:
        fields = (
            'id',
            'evaluation',
        )
        model2 = Evaluation
