from django.urls import path
from . import views


urlpatterns = [

    path('all', views.AllViews.as_view()),

]
