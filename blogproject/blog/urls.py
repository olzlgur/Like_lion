

from .views import *
from django.urls import path


urlpatterns = [
    path('', home, name="home"),
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]
