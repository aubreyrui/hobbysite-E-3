from django.contrib import admin

from .models import Job, Commission

class JobAdmin(admin.ModelAdmin):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission


admin.site.register(Job, JobAdmin)
admin.site.register(Commission, CommissionAdmin)