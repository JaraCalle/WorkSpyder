from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Mostrar todos los campos disponibles del usuario en la lista del admin
    list_display = ['id', 'email']

    # Configuración para ver y editar todos los campos en el admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('avatar',)}),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Fechas Importantes', {'fields': ('last_login',)}),
    )

    # Campos al crear un nuevo usuario desde el admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'avatar', 'is_active', 'is_staff'),
        }),
    )

    # Configuraciones adicionales
    search_fields = ('email',)  # Corregido: tupla con una coma final
    ordering = ('email',)
