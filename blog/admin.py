from django.contrib import admin
from .models import*

#@admin.register(Article)
#class ArticleAdmin(admin.ModelAdmin):
  #pass
admin.site.register(Article)