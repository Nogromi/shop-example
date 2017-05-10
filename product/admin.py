from django.contrib import admin
from django.contrib.admin import AdminSite
from  .models import Product, Comment





# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','description', 'price', 'created' ,'updated',  ]
    list_filter = ['price', 'created']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class CommentAdmin(admin.ModelAdmin):
    search_fields =  ['name','body']
admin.site.register(Comment, CommentAdmin)



class MyAdminSite(AdminSite):
    site_url = '127.0.0.1:8000/products/'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Product, ProductAdmin)

admin_site.register(Comment, CommentAdmin)
