from django.urls import path
 
from . import views
 
urlpatterns = [
    path('', views.collect_info, name='collect_info'),
	path('submit/', views.submit, name='submit'),
]
