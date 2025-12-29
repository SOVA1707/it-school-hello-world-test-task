from django.contrib import admin

from test_app import models


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    ...
