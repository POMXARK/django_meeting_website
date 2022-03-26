from django.urls import path
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import TestClass, Category1Details,PersonList
app_name = "authenticate"

urlpatterns = [
    path('list/', PersonList.as_view()),
    path('members/', TestClass.as_view()),
    path('clients/<int:id>/match', Category1Details.as_view()),
    path('clients/create', UserViewSet.as_view({'post': 'create'}), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    path("activation/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "activate"}), name="activate"),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("reset-password-confirm/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "reset_password_confirm"}), name="reset_password_confirm"),
]