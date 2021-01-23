from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog, name='blog'),
    path('<int:pk>/', detail, name='detail'),
    path('search/', search, name='search'),
]


