from django.urls import path
from . import views

urlpatterns = [
    path('api/geology/', views.USGeologyListCreate.as_view()),
]
