from django.contrib import admin

from .models import Job, JobApplication, Commission

class JobAdmin(admin.ModelAdmin):
    model = Job


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication


class CommissionAdmin(admin.ModelAdmin):
    model = Commission


admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Commission, CommissionAdmin)