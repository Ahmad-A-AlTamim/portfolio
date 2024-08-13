from django.contrib import admin
from .models import  account
from .skillsModel import  skills
admin.site.register(account)
class skillsAdmin(admin.ModelAdmin):
    list_display = ['skill','category','user']
    list_filter = ['category','user']
    list_editable = ['category']
    search_fields = ['category','skill']
    list_per_page = 10



# Register your models here.
admin.site.register(skills,skillsAdmin)