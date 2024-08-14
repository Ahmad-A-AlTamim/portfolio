from django.contrib import admin
from .models import  account
from .skillsModel import  skills
from .educationModel import education
admin.site.register(account)
admin.site.register(education)
class skillsAdmin(admin.ModelAdmin):
    list_display = ['skill','category','user']
    list_filter = ['category','user']
    list_editable = ['category']
    search_fields = ['category','skill']
    list_per_page = 10

# class educationAdmin(admin.ModelAdmin):
#     list_display = ['major','university','startDate','endDate','user','note']
#     list_filter = ['degree','user']
#     list_editable = ['degree','major','university','startDate','endDate','note']
#     search_fields = ['degree','major','university']
#     list_per_page = 10

# Register your models here.
admin.site.register(skills,skillsAdmin)
# admin.site.register(education)