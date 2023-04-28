from django.contrib import admin
from .models import (SolisitudMOdel, AmigoModels, ChatModels, PostModel, LikeModels, ComentarModels , ConpartirModels,
                     NotificacionesModels,ComentarioLike,
                 PostaspirantesModels   )

class UsermodelAdmin(admin.ModelAdmin):
    list_display = ('user','añadidos','created')
    search_fields = ('user__username',)

# Register your models here.
admin.site.register(SolisitudMOdel)
admin.site.register(AmigoModels, UsermodelAdmin)
admin.site.register(PostModel)
admin.site.register(LikeModels)
admin.site.register(ComentarModels)
admin.site.register(ConpartirModels)
admin.site.register(NotificacionesModels)
admin.site.register(ChatModels)
admin.site.register(ComentarioLike)
admin.site.register(PostaspirantesModels)