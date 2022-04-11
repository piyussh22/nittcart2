from django.contrib import admin

# Register your models here.
from .models import Product, Contact
from .models import Registerform,Addpost1

admin.site.register(Product)
admin.site.register(Contact)

admin.site.register(Registerform)
admin.site.register(Addpost1)
