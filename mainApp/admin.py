
from django.utils.html import format_html
from django.contrib import admin
from mainApp.models import  account
from mainApp.skillsModel import  skills
from mainApp.educationModel import education
from mainApp.HonorsAndAwardsModel import honorsAndAwards
from mainApp.imagesModel import imagesModel
from .competations import competations
class skillsAdmin(admin.ModelAdmin):
    list_display = ['skill','category','user']
    list_filter = ['category','user']
    list_editable = ['category']
    search_fields = ['category','skill']
    list_per_page = 10
pass


class educationAdmin(admin.ModelAdmin):
    list_display = ['degree','major', 'university', 'startDate', 'endDate', 'user', 'note']
    list_filter = ['degree', 'user']
    list_editable = [ 'major', 'university', 'startDate', 'endDate', 'note']
    search_fields = ['degree', 'major', 'university']
    list_per_page = 10

class honorsAndAwardsAdmin(admin.ModelAdmin):
    list_display = ['title','rank','date','user','description']
    list_filter = ['date','user']
    list_editable = ['rank','date','description']
    search_fields = ['title','rank']
    list_per_page = 10
    pass
class imagesModelAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['Title','user','image_tag']
    list_filter = ['user','Title']
    list_editable = []

    search_fields = ['Title']
    list_per_page = 10
    pass
# Register your models here.
admin.site.register(account)
admin.site.register(skills,skillsAdmin)
admin.site.register(education,educationAdmin)
admin.site.register(honorsAndAwards,honorsAndAwardsAdmin)
admin.site.register(imagesModel,imagesModelAdmin)
admin.site.register(competations)