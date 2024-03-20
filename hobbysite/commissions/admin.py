from django.contrib import admin

from .models import Comment, Commission

class CommentAdmin(admin.ModelAdmin):
    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    model = Commission


admin.site.register(Comment, CommentAdmin)
admin.site.register(Commission, CommissionAdmin)