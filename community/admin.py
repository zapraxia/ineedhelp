from django.contrib import admin

from .models import University, Program, Profile, Correspondence

admin.site.register(University)
admin.site.register(Program)
admin.site.register(Profile)


@admin.register(Correspondence)
class CorrespondenceAdmin(admin.ModelAdmin):
    list_display = ['subject', 'name', 'email', 'created_on']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
