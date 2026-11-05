from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    ('User Role', {'fields': ('role',)}),
    )

    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('User Role', {'fields': ('role',)}),
    )
    

admin.site.register(User, CustomUserAdmin)

# Register your models here.
