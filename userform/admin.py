from django.contrib import admin
from .models import Registration

# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone')
admin.site.register(Registration,RegistrationAdmin)    
