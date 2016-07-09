from django.db import models
# сделать загрузку вариантов предметов из моделей предметов
class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название предмета')
    code_name = models.SlugField(max_length=20, unique=True, verbose_name='URL префикс (только латинские быквы и символы - и _')

class Document(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Документ', primary_key=True)
    subject = models.ForeignKey(Subject, verbose_name='Предмет')
    kurs = models.PositiveSmallIntegerField(verbose_name= 'Курс')
    author = models.CharField(max_length=20, verbose_name='Автор')
    description = models.TextField()
    file = models.FileField(upload_to='docs')
