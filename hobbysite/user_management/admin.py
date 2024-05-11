from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]
    add_fieldsets = (
            (None, {'fields': ('display_name','email', 'password',)}),
        )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)