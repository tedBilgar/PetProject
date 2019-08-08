from django.contrib import admin
from .models import Cat
from .models import Owner

admin.site.register(Cat)
admin.site.register(Owner)
