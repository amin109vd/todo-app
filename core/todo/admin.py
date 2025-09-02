from django.contrib import admin
from . models import Task

@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ('title','complete')
    list_filter = ('complete',)
    ordering = ('created_date',)
    search_fields = ('title',)
        

