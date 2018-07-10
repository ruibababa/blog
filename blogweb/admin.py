from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, PostAdmin)



