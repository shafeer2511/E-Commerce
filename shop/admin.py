from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description','created_at','status')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'vendor', 'quantity', 'original_price', 'selling_price', 'status', 'trending', 'created_at')
    search_fields = ('name', 'vendor')  # Adds a search bar for these fields
    list_filter = ('status', 'trending', 'category')  # Adds filters in the admin sidebar
    ordering = ('-created_at',)  # Orders products by the newest created first

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)