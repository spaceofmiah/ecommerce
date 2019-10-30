from django.urls import path
from clothing import views

app_name = "clothing"
urlpatterns = [
    path('', views.index_page, name='index'),
]
