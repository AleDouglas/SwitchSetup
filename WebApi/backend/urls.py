from django.urls import path, include
from .views.home import HomeView
from .views.ansible import AnsibleView
from .views.log import LogView
from .views.user import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ansible/', AnsibleView.as_view(), name='ansible'),
    path('log/', LogView.as_view(), name='log'),
    path('user/list/', UserPageView.as_view(), name='userList'),
    path('user/create/', CreateUserView.as_view(), name='userCreate'),
    path('user/<int:pk>/edit/', UpdateUserView.as_view(), name='userEdit'),
    path('user/<int:pk>/delete/', DeleteUserView.as_view(), name='userDelete'),
]