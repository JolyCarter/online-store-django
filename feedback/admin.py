from django.contrib import admin

from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'message')


admin.site.register(Feedback, FeedbackAdmin)
