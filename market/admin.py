from django.contrib import admin
from .models import Category, Guarantee, Color, Article, NewUser

admin.site.register(NewUser)
admin.site.register(Category)
admin.site.register(Guarantee)
admin.site.register(Color)
admin.site.register(Article)
