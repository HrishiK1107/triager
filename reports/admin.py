from django.contrib import admin
from .models import BugReport

@admin.action(description='Mark selected reports as Approved')
def mark_approved(modeladmin, request, queryset):
    updated = queryset.update(status='Approved')
    modeladmin.message_user(request, f"{updated} reports marked as Approved.")

@admin.action(description='Mark selected reports as Rejected')
def mark_rejected(modeladmin, request, queryset):
    updated = queryset.update(status='Rejected')
    modeladmin.message_user(request, f"{updated} reports marked as Rejected.")

@admin.action(description='Mark selected reports as In Progress')
def mark_in_progress(modeladmin, request, queryset):
    updated = queryset.update(status='In Progress')
    modeladmin.message_user(request, f"{updated} reports marked as In Progress.")

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'submitted_by', 'submitted_at', 'status', 'cvss_score', 'reward')
    list_filter = ('status', 'submitted_at')
    actions = [mark_approved, mark_rejected, mark_in_progress]