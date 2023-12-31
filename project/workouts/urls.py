from django.urls import path
from .views import *

urlpatterns = [
    path('create-workout/', CreateWorkoutView.as_view(), name='create-workout'),
    path('my-workouts/', MyWorkoutsView.as_view(), name='get-my-workouts'),
    path('<int:workout_id>/exercises/', WorkoutExercisesView.as_view(), name='get-workout-exercises'),
    path('<int:workout_id>/modify/', WorkoutUpdateDeleteView.as_view(), name='modify-delete-workout'),
    path('exercises/<int:exercise_id>/sets/', SetsAPIView.as_view(), name='create-get-sets'),
    path('sets/<int:set_id>/', SetDeleteAPIView.as_view(), name='delete-set'),
    path('summary/', WorkoutSummaryAPIView.as_view(), name='workout-summary'),
    path('progress/', ExerciseProgressionAPIView.as_view(), name='progress-exercises'),

    # Admin functions
    path('workouts-list/', WorkoutListAPIView.as_view(), name='workouts-list'),
    path('exercises-list/', ExerciseListAPIView.as_view(), name='exercises-list'),
    path('sets-list/', SetListAPIView.as_view(), name='sets-list'),
]

