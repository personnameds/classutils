from django.contrib import admin
from classlists.models import Klass, Student

class KlassAdmin(admin.ModelAdmin):
    list_display=('name','size',)

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','klass',)

admin.site.register(Klass, KlassAdmin)
admin.site.register(Student, StudentAdmin)
