from django.contrib import admin
from .models import adminpanel,adminfruits,admingreens,admintubers,adminveg

# Register your models here.
admin.site.register(adminpanel)
admin.site.register(adminfruits)
admin.site.register(adminveg)
admin.site.register(admintubers)
admin.site.register(admingreens)