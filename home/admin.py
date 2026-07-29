from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User




@admin.register(User)
class CustomUserAdmin(UserAdmin):
   
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type', 'is_staff')

    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email')}), # <--- این بخش بسیار مهم است
        ('اطلاعات امنیتی', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('اطلاعات اضافی', {'fields': ('phone_number', 'address', 'user_type', 'profile_picture')}),
    )

    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'user_type'),
        }),
    )