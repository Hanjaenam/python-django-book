from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test_form_def', views.form_test_def, name="form_test_def"),
    path('test_form_class', views.form_test_class.as_view(), name="form_test_class"),
    path('class_view', views.My_view.as_view()),  # class View
    path('class_view_template', views.My_view_template.as_view()), # class Template
    # path('class_view_template2', views.MyViewTemplate.as_view(template_name='about.html')) 가능 p.203 참고할 것.

]
