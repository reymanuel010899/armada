"""socialapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
app_name = 'inicio_app'


urlpatterns = [
    path('', views.homeview, name='inicio' ),
    path('perfil/<username>/', views.perfil, name='profile'),
    path('solicitudes/', views.friend_views, name="friend"),
    path('perfil-setting/', views.perfil_setting_views, name="perfil-setting"),
    path('perfil-photos/<username>/', views.fotos_views, name="perfil-photos"),
    path('perfil-about/<username>/', views.about_views, name="perfil-about"),
    path('buscar-contenido/', views.buscar_contenido_views, name="buscar-contenido"),
    path('agreagr-like-status/<pk>/', views.agergar_like_status, name="agregar-like"),
    path('enviar-solicitud/<username>/', views.enviar_solicitud, name="enviar-solicitud"),
    path('agregar-amigos/<username>/', views.añadir_a_amigos, name="agregar-amigos"),
    path('friend-añadidos/', views.amigos_añadidos, name="friend-añadidos"),
    path('chat-usuario/<username>/', views.chats_usuarios, name="chat-usuario"),
    path("ultimo-chat/", views.ultimos_chats, name="ultimo-chat"),
    path('listar-notificaciones/', views.listar_notificaciones, name="listar-notificaciones"),
    path("Settings/", views.Settings_views, name="Settings"),
    path("feed/<pk>/", views.feed_views, name="feed"),
    path("compartir-post/<pk>/", views.compartir_post, name="compartir-post"),
    path('sugerencia-amigo/', views.sugerencias_amigos_views, name="sugerencia-amigo"),
    path('comentar-post-profile/<pk>/',  views.comentar_post, name="comentar-post-profile" ),
    path('eliminar-documentos/<pk>/', views.eliminar_documentos, name="eliminar-documentos"),
    path('elimicar-post/<pk>/', views.eliminar_post, name="elimicar-post")
    # path('cambiar-perfil/', views.cambiar_perfil, name="cambiar-perfil")
    #path('cambiar-contraseña/', views.cambiar_contraseña, name="cambiar-contraseña"),
    

]
