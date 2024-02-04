from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('quote/<int:quote_id>', views.quote, name='quote'),
    path('tag/', views.tag, name='tag'),
    path('add_author/', views.add_author, name='add_author'),
    path('delete/<int:quote_id>', views.delete_quote, name='delete'),
]