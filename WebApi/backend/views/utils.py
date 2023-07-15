from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AdminRequired(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        user = self.request.user
        return user.is_staff # Verificando

    def handle_no_permission(self):
        return HttpResponseForbidden('ACCESS FORBIDDEN! ONLY ADMINISTRATORS CAN ACCESS THIS PAGE.')