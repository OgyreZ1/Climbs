from django.urls import path
from .views import *

app_name = 'climbs'
urlpatterns = [
    path('all/', ChallengesListView.as_view()),
    path('challenge/detail/<int:pk>/', ChallengeDetailView.as_view()),
    path('challenge/create/', ChallengeCreateView.as_view()),
    path('step/create/', StepCreateView.as_view())
]