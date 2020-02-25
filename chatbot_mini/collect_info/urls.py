from django.urls import path
 
from . import views
 
urlpatterns = [
    path('', views.collect_info, name='collect_info'),
	path('ajax/load-models/', views.load_models, name='ajax_load_models'),
	path('submit/', views.submit, name='submit'),
]
