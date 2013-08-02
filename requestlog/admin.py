from django.contrib import admin
from django.db import models
from django.forms import TextInput

from .models import RequestLog

class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip', 'path', 'user_agent',)
    search_fields = ('timestamp', 'ip', 'path', 'user_agent',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'128'})},
    }

admin.site.register(RequestLog, RequestLogAdmin)
