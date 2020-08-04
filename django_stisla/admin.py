from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.

class StislaAdmin(AdminSite):

    site_short_title = "DJ"

    def each_context(self, request):
        context = super().each_context(request)
        context["site_short_title"] = self.site_short_title
        return context


site = StislaAdmin()
site.register(Group, GroupAdmin)
site.register(User, UserAdmin)