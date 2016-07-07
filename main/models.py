from django.db import models
# сделать загрузку вариантов предметов из моделей предметов
class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название предмета')
    #index = models.AutoField(unique=True)

class Document(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Документ', primary_key=True)
    subject = models.ForeignKey(Subject, verbose_name='Предмет')
    description = models.TextField()
    file = models.FileField(upload_to='docs')
