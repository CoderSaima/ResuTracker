from django.urls import path
from resu_app import views

urlpatterns = [
    path('jflksfl', views.resu_views, name='resu_view'),
    path('', views.resu_model_view, name='resu_model_view')
]
