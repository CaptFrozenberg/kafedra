from django.db import models
# сделать загрузку вариантов предметов из моделей предметов
class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название предмета')
    code_name = models.SlugField(max_length=20, unique=True, verbose_name='URL префикс')
    magistratura = models.BooleanField(verbose_name='Магистратура', default=False)
    kurs = models.PositiveSmallIntegerField(verbose_name='Курс', default=0)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Документ', db_index=True)
    subject = models.ForeignKey(Subject, verbose_name='Предмет')
    kurs = models.PositiveSmallIntegerField(verbose_name= 'Курс')
    author = models.CharField(max_length=20, verbose_name='Автор')
    description = models.TextField()
    file = models.FileField(upload_to='docs')

    def __str__(self):
        return '{0} {1} курс'.format(self.name, str(self.kurs))
