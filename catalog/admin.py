from django.contrib import admin
from catalog.models import Genre,Book,BookInstance,Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
#@admin.register(BookInstance)
#class BookInstanceAdmin(admin.ModelAdmin):
#   list_display = ('book', 'status', 'borrower', 'due_back', 'id')
#  list_filter = ('status', 'due_back')
    
