import django
from django.contrib import admin

# Register your models here.
from shop.models import product,Contact,Orders,OrderUpdate,myuser
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(myuser)
