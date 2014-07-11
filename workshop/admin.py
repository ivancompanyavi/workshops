from django.contrib import admin
from .models import Question, Option, Workshop, Answer
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description',)


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'commiter',)

    def commiter(self, obj):
        return obj.commiter.user.username

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Answer)