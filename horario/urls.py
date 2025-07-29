from django.urls import path
from . import views

app_name = 'horario'

urlpatterns = [
    path('', views.horario_view, name='horario'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('agregar/', views.agregar_clase, name='agregar_clase'),
    path('editar/<int:pk>/', views.editar_clase, name='editar_clase'),
    path('eliminar/<int:pk>/', views.eliminar_clase, name='eliminar_clase'),
    path('api/clases/', views.api_clases, name='api_clases'),
] 