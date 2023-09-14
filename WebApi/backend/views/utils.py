from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.http.response import FileResponse
from backend.DAL.models.ansible import *

class AdminRequired(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        user = self.request.user
        return user.is_staff # Verify

    def handle_no_permission(self):
        return HttpResponseForbidden('ACCESS FORBIDDEN! ONLY ADMINISTRATORS CAN ACCESS THIS PAGE.')



def media_access(request, path):    
    access_granted = False
    user = request.user
    get_obj = None
    print(path)

    if user.is_authenticated:
        if user.is_staff:
            # If you are an Administrator, access to the route is guaranteed
            access_granted = True
            try:
                get_obj = PlaybookCustom.objects.get(playbook_file=f"backend/integrations/communs/custom/{path}")
                get_obj = get_obj.playbook_file
            except:
                try:
                    get_obj = HostCustom.objects.get(host_file=f"backend/integrations/communs/custom/{path}")
                    get_obj = get_obj.host_file
                except:
                    return HttpResponseForbidden('Object not found, check the path you are using')

    if access_granted:
        response = FileResponse(get_obj)
        return response
    else:
        return HttpResponseForbidden('ACCESS FORBIDDEN! ONLY ADMINISTRATORS CAN ACCESS THIS PAGE.')