from django.contrib import admin
from . import models


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    search_fields = [
        'word',
        'translation',
    ]
    list_display = [
        'word',
        'translation',
        'id',
    ]
