from django.urls import path

from . import views

#app_name = 'addArticle'

urlpatterns = [
               path('adda', views.add, name="add"),
               path('edit/<str:title>/', views.edit, name="edit"),
               path('save/', views.save, name='save_text')]