from django.contrib import admin
from .models import Author, Books, Publisher, User

# Register your models here.
admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Publisher)
admin.site.register(User)
