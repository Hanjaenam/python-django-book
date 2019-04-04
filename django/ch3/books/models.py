from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=100)
  # 테이블 간 관계를 타나내는 필드는ForeignKey, ManyToManyField, OneToOneField 3가지가 존재한다.
  authors = models.ManyToManyField('Author') # N : N
  # N : 1 Book에서는 외래키를 단 하나만 지정할 수 있으므로 한 명의 작가가 여러 개의 Book을 가질 수 있다는 것.
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE) 
  pulication_date = models.DateField()
  def __str__(self):
    return self.title

class Author(models.Model):
  name = models.CharField(max_length=50)
  salutation = models.CharField(max_length=100)
  email = models.EmailField()
  def __str__(self):
    return self.name

class Publisher(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  website = models.URLField()
  def __str__(self):
    return self.name