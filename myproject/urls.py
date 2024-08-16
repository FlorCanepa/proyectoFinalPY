from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('search/', views.search, name='search'),
    path('register/', views.registro, name='register'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('books/', views.libro_listado, name='libro_listado'),
    path('books/<int:libro_id>/edit/', views.editar_libro, name='editar_libro'),
    path('books/<int:libro_id>/delete/', views.borrar_libro, name='borrar_libro'),
    path('accounts/', include('django.contrib.auth.urls'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
