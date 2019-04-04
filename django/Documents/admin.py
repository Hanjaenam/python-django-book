from django.contrib import admin
from polls.models import Question, Choice
# admin.StackedInline/TabularInline, fields, fieldsets, inlines, list_display

class ChoiceInline(admin.StackedInline): # admin.TabularInline
  model = Choice
  extra = 2

class QuestionAdmin(admin.ModelAdmin):
  # fields = ['question_text', 'pub_date'] # 필드 순서 변경

  # 각 필드를 분리해서 보여주기
  fieldsets = [
    ('Question Statement', {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}) # classes 필드 접기
  ]
  inlines = [ChoiceInline]  # Question추가할 경우 같이 Choice를 추가할 수 있도록
  list_display = ('question_text', 'pub_date') # question 리스트에서 날짜도 보여주게끔
  list_filter = ['pub_date'] # 필터 사이드바 추가
  search_fields = ['question_text'] # 검색 박스 추가
# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
