from django.contrib import admin

from home.models import Book,Author,Genre
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)
@admin.register(Book)
class bookadmi(admin.ModelAdmin):
   search_fields=('id','name')
   list_filters=('name','purchase_date')
@admin.register(Author)
class authoradmi(admin.ModelAdmin):
     search_fields=('id','name')
     list_filters=('name','purchase_date')
@admin.register(Genre)
class genreadmi(admin.ModelAdmin):
    pass