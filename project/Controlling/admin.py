from django.contrib import admin
from .models import Book , Borrowing  , Client , User

# Register your models here.

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Borrowing)