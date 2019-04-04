from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher
# Create your views here.

#---- TemplateView
class BooksModelView(TemplateView):
  template_name = 'books/index.html'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['model_list'] = ['Book', 'Author', 'Publisher']
    return context

class BookList(ListView):
  # template_name = books/book_list.html 로 자동 저장된다.
  # context -> object_list 로 자동 저장된다 ( template 에서 object_list 를 사용하면 된다. )
  model = Book
class AuthorList(ListView):
  model = Author
class PublisherList(ListView):
  model = Publisher

class BookDetail(DetailView):
  model = Book
class AuthorDetail(DetailView):
  model = Author
class PublisherDetail(DetailView):
  model = Publisher