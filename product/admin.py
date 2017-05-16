from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Product, Comment, Profile


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price', 'created', 'updated', ]
    list_filter = ['price', 'created']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']


admin.site.register(Comment, CommentAdmin)


#
# admin_site = MyAdminSite(name='myadmin')
# admin_site.register(Product, ProductAdmin)
#
# admin_site.register(Comment, CommentAdmin)
# admin_site.register(Profile)
