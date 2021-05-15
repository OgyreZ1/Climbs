from rest_framework import serializers
from .models import *


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, required=False)

    class Meta:
        model = Challenge
        fields = '__all__'


