from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Books)
admin.site.register(BookOrders)
admin.site.register(BookContent)
admin.site.register(ISBN)
