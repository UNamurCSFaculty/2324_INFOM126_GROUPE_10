from django.urls import path

from . import views

urlpatterns = [
path('', views.index, name='index'),
path('ajouter_message/', views.add_message, name='add_message'),
path('modifier_message/<int:message_id>/', views.update_message, name='modifier_message'),
path('supprimer_message/<int:message_id>/', views.delete_message, name='supprimer_message')
    
]