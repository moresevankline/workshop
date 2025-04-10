from django.urls import path
from . import views

urlpatterns = [
    path("countries/", views.CountriesView().as_view(), name="countries"),
    path("country/<str:country>/", views.CountryView().as_view(), name="country"),
]
