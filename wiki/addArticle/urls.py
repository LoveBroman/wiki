from django.urls import path

from . import views

#app_name = 'addArticle'

urlpatterns = [
               path('adda', views.add, name="add"),
               path('edit/<str:title>/', views.edit, name="edit"),
               path('save_add/', views.save_add, name='save_add'),
               path('save_edit/', views.save_edit, name= 'save_edit')]