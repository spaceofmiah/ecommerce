from django.urls import path
from clothing import views

app_name = "clothing"
urlpatterns = [
    path('', views.index_page, name='index'),
    path('all-cloth/', views.cloth_list, name='cloth_list')
]
