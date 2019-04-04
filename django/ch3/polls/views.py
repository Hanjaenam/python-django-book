from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.models import Choice, Question
from .form import test_form    # Form
from django.views.generic import View           # class View class
from django.views.generic import TemplateView   # Template View class
from django.views.generic.edit import FormView  # Form View class
import logging # log
# Create your views here.

# setting.py파일에서 설정된 로거를 취득한다.
logger = logging.getLogger('mylogger')
def my_view(request, arg1, arg):
  # 필요한 로직
  if bad_mojo:
    # ERROR 레벨의 로그 레코드를 생성함
    logger.error('Something went wrong!')


def index(request):
  latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice"
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

# -------------------------------- Form ------------------------------------- #
def form_test_def(request):
  if request.method == 'POST':
    form = test_form(request.POST)
    if form.is_valid():
      # new_name = form.cleaned_data['name']
      # 유효성 검사 후 통과된 데이터들이 cleaned_data 에 들어온다.
      return HttpResponseRedirect('/success/')
  else:
    form = test_form(initial={'label_id_or_input_name': 'initial!'})
  return render(request, 'form.html', {'form':form})

class form_test_class(View):
  form_class = test_form
  initial = {'label_id_or_input_name': 'initial!'}
  template_name = 'form.html'
  def get(self, request, *args, **kwargs):
    # 자동으로 get method 를 감지하는 듯
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form': form})
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      return HttpResponseRedirect('/success/') # /success -> localhost:8000/success, success -> localhost:8000/polls/success
    return HttpResponseRedirect('/failure/') # 유효하지 않은 데이터를 가진 POST

class form_test_class_2(FormView):
  form_class = test_form
  template_name = 'form.html'
  success_url = '/success/'
  def form_valid(self, form):
    return super(form_test_class_2, self).form_valid(form)
# -------------------------------- Form ------------------------------------- #

# basic class View
class My_view(View):
  def get(self, request):
    return HttpResponse('result')

# template view class
class My_view_template(TemplateView):
  template_name = "about.html"