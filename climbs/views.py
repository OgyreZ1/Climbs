from rest_framework import generics
from .serializers import *
from .models import Challenge


class ChallengeCreateView(generics.CreateAPIView):
    serializer_class = ChallengeSerializer


class ChallengesListView(generics.ListAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()


class ChallengeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge


class StepCreateView(generics.CreateAPIView):
    serializer_class = StepSerializer


class StepsListView(generics.ListAPIView):
    serializer_class = StepSerializer
    queryset = Step.objects.all()


class StepDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StepSerializer
    queryset = Challenge
