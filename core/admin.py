from django.contrib import admin
from .models import Worker


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'name', 'team', 'level')

    def name(self, obj):
        return obj.user.first_name
    name.short_description = 'Name'

    def user_name(self, obj):
        return obj.user.username

    user_name.short_description = 'Username'

admin.site.register(Worker, WorkerAdmin)