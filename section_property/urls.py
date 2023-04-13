from django.urls import path
from . import views

urlpatterns = [
    path('verify_sections/', views.VerifySectionsView.as_view(), name='verify_sections'),
]
