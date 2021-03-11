from django.contrib import admin
from issue_tracker.models import Task, Type, Status


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'type', 'created_at', 'updated_at']
    list_filter = ['status', 'type']
    search_fields = ['summary', 'description', 'status', 'type']
    fields = ['id', 'summary', 'description', 'status', 'type']
    readonly_fields = ['created_at', 'updated_at', 'id']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name_of_status']
    fields = ['name_of_status']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name_of_type']
    fields = ['name_of_type']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
