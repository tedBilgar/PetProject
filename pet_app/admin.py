from django.contrib import admin
from .models import Cat
from .models import Owner
from .models import Toy
from .models import CatToyRelation

admin.site.register(Cat)
admin.site.register(Owner)
admin.site.register(Toy)
admin.site.register(CatToyRelation)
