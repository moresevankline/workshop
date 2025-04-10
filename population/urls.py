from django.urls import path
from . import views

urlpatterns = [
    path("prediction/", views.predicted_population(), name="predict_population"),
]
