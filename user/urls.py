from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("registration/", views.UserRegisterView.as_view(), name="user-registration"),
    path(
        "login/",
        views.UserView.as_view(),
        name="user-details",
    ),
]
