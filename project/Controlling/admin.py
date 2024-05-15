from django.contrib import admin
from .models import Book , Borrowing  , User , Client  , Admin

# Register your models here.

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Borrowing)
admin.site.register(Admin)