from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='catalogos'),
    path('listarCarreras/', views.listarCarreras, name='listarCarreras'),
    path('crearCarreras/', views.crearCarreras, name='crearCarreras'),
    path('editarCarreras/<int:pk>/', views.editarCarreras, name='editarCarreras'),
    path('eliminarCarreras/<int:pk>',views.eliminarCarreras, name='eliminarCareras'),
]
