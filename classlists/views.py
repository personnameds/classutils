from django.shortcuts import render

from django.views.generic import ListView
from classlists.models import Klass, Student
		
class ClassesListListView(ListView):
    template_name='classes_list.html'
    context_object_name='classes_list'
    model=Klass
    
class StudentListListView(ListView):
    template_name='student_list.html'
    context_object_name='student_list'
    model=Student
    
    def get_queryset(self):
        return Student.objects.filter(klass__name=self.kwargs['klass']).order_by('name')
    
    def get_context_data(self, **kwargs):
        ctx=super(StudentListListView, self).get_context_data(**kwargs)
        ctx['klass']=self.kwargs['klass']
        return ctx