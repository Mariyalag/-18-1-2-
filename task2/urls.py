from django.urls import path
from .views import ClassView, function_view

urlpatterns = [
    path('', function_view),
    path('classt/', ClassView.as_view()),
]
