from django.contrib import admin
from .models import *

# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display = ['id','DATE','ca1','ca2','ca3','ca4', 'caption']
    search_fields = ['id']

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'sum1', 'sum2', 'sum3', 'sum4']
    search_fields = ['id']

admin.site.register(mainTB, TableAdmin)
admin.site.register(resultTB, ResultAdmin)