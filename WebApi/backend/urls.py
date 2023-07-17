from django.urls import path, include
from .views.home import HomeView
from .views.ansible import AnsibleView
from .views.log import LogView
from .views.user import *
from .views.credential import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ansible/', AnsibleView.as_view(), name='ansible'),
    path('ansible/credential/', CredentialPageView.as_view(), name='credentialList'),
    path('ansible/credential/<int:pk>/edit/', UpdateCredentialView.as_view(), name='credentialEdit'),
    path('ansible/credential/<int:pk>/delete/', DeleteCredentialView.as_view(), name='credentialDelete'),
    path('log/', LogView.as_view(), name='log'),
    path('user/list/', UserPageView.as_view(), name='userList'),
    path('user/create/', CreateUserView.as_view(), name='userCreate'),
    path('user/<int:pk>/edit/', UpdateUserView.as_view(), name='userEdit'),
    path('user/<int:pk>/delete/', DeleteUserView.as_view(), name='userDelete'),
]