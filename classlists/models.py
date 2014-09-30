from django.db import models

class Klass(models.Model):
    name=models.CharField(max_length=5, unique=True)
    size=models.IntegerField(max_length=2)
    
    class Meta:
        verbose_name='Class'
        verbose_name_plural='Classes'
    
    def __unicode__(self):
        return '%s' %self.name
    
class Student(models.Model):
    name=models.CharField(max_length=20)
    klass=models.ForeignKey('Klass', verbose_name='Class')