from django.urls import path

from relatorios import views

urlpatterns = [

    path('', views.index, name='index'),
    
    path('solved_tickets', views.solved_tickets, name='solved_tickets'),
    path('get_all_tickets', views.get_all_tickets, name='get_all_tickets')

    
]