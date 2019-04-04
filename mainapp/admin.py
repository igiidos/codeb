from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import IndexMarkUp


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('markup_text',)


admin.site.register(IndexMarkUp, PostAdmin)