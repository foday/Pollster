from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin"

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
