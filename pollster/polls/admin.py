from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                ('Date Information', {'fields': ['publish_date'], 'classes':
                ['collapse']}),]
    inLines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
