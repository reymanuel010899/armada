from django.contrib import admin
from .models import User, InformacionPersonal, UserActivity

class UsermodelAdmin(admin.ModelAdmin):
    list_display = ('username','gmail','genero','ubicacion', 'id')
    search_fields = ('username','id')

class informacionAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'user__id')
    list_display = ('user', 'cedula', 'telefono','direcion','pais')

admin.site.register(User, UsermodelAdmin)
admin.site.register(InformacionPersonal,informacionAdmin)
admin.site.register(UserActivity)