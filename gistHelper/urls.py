from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    path('meal/', views.MealplanList.as_view()),
    # path('meal/<int:pk>/', views.MealplanDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)