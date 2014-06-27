from django.contrib import admin
from models import Achievement, Workshop, Worker, Option, Question

# Register your models here.


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'name', 'team', 'level')

    def name(self, obj):
        return obj.user.first_name
    name.short_description = 'Name'
    def user_name(self, obj):
        return obj.user.username
    user_name.short_description = 'Username'


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description',)


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'commiter',)

    def commiter(self, obj):
        return obj.commiter.user.username

admin.site.register(Achievement)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Question, QuestionAdmin)