from django.urls import path, include
from .views.home import HomeView
from .views.ansible import *
from .views.log import LogView
from .views.user import *
from .views.credential import *
from .views.api import *
from .views.doc import *
from .views.utils import media_access

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('doc', DocView.as_view(), name='doc'),
    path('ansible/', AnsibleView.as_view(), name='ansible'),
    path('ansible/default/', AnsibleDefaultView.as_view(), name='ansibleDefault'),
    path('ansible/custom/', AnsibleCustomView.as_view(), name='ansibleCustom'),
    path('ansible/custom/playbook/new', PlaybookCustomView.as_view(), name='playbookCustom'),
    path('ansible/custom/host/new', HostCustomView.as_view(), name='hostCustom'),

    path('ansible/custom/playbook/list/', PlaybookCustomListView.as_view(), name='playbookCustomList'),
    path('ansible/custom/playbook/<int:pk>/edit/', PlaybookCustomEditView.as_view(), name='playbookCustomEdit'),
    path('ansible/custom/playbook/<int:pk>/delete/', PlaybookCustomDeleteView.as_view(), name='playbookCustomDelete'),

    path('ansible/custom/playbook/commandline/', CommandLineView.as_view(), name='commandLine'),
    path('ansible/custom/playbook/commandline/<int:pk>/edit/', CommandLineEditView.as_view(), name='commandLineEdit'),
    path('ansible/custom/playbook/commandline/<int:pk>/delete', CommandLineDeleteView.as_view(), name='commandLineDelete'),


    path('ansible/custom/host/list/', HostCustomListView.as_view(), name='hostCustomList'),
    path('ansible/custom/host/<int:pk>/edit/', HostCustomEditView.as_view(), name='hostCustomEdit'),
    path('ansible/custom/host/<int:pk>/delete/', HostCustomDeleteView.as_view(), name='hostCustomDelete'),


    path('ansible/credential/', CredentialPageView.as_view(), name='credentialList'),
    path('ansible/credential/<int:pk>/edit/', UpdateCredentialView.as_view(), name='credentialEdit'),
    path('ansible/credential/<int:pk>/delete/', DeleteCredentialView.as_view(), name='credentialDelete'),
    path('log/', LogView.as_view(), name='log'),
    path('user/list/', UserPageView.as_view(), name='userList'),
    path('user/<int:pk>/edit/', UpdateUserView.as_view(), name='userEdit'),
    path('user/<int:pk>/delete/', DeleteUserView.as_view(), name='userDelete'),

    #Api Area
    path('api/', ApiPageView.as_view(), name='apiKey'),
    path('api/v1/', ApiResponseView.as_view(), name='apiResponse'),
    path('api/v2/', ApiCustomResponseView.as_view(), name='apiCustomResponse'),
    path('api/v2/host', ApiHostDefault.as_view(), name='ApiHostDefault'),
    path('api/v3/playbook', ApiGetPlaybook.as_view(), name='apiGetPlaybook'),
    path('api/v3/command', ApiGetCommandLine.as_view(), name='apiGetCommand'),
    path('api/v3/host', ApiGetHost.as_view(), name='apiGetHost'),
    path('api/key/<int:pk>/delete/', ApiDeleteView.as_view(), name='keyDelete'),
    
    #Security Area
    path('backend/integrations/communs/custom/<str:path>', media_access, name='media'),
]