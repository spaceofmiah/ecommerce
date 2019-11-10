from django.urls import path
from clothing import views

app_name = "clothing"
urlpatterns = [
    path(
            '', 
            views.index_page, 
            name='index'
        ),

    path(
            'all-cloth/', 
            views.cloth_list, 
            name='cloth_list'
        ),  

    path(
            'search-cloth/', 
            views.handle_cloth_search, 
            name='handle_cloth_search'
        ),

    path(
            'create-cloth', 
            views.handle_cloth_creation, 
            name='create_cloth'
        ),
    
    path(
            'cart/<int:cloth_id>/', 
            views.handle_add_to_cart, 
            name='add_to_cart'
        ),

]
