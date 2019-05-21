from django.urls import include, path

from . import views
from .views import UserListView, UserProfileView

urlpatterns = [
    path('user/', UserListView.as_view(), name="user-all"),
    path('hello/', UserProfileView.as_view(), name='hello'),
    path('signup/', views.SignUp.as_view(), name='signup')
]