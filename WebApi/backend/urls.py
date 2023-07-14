from django.urls import path, include
from .views.home import HomeView
from .views.ansible import AnsibleView
from .views.log import LogView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ansible/', AnsibleView.as_view(), name='ansible'),
    path('log/', LogView.as_view(), name='log'),
]