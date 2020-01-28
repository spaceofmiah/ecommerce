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
            'update-cloth/<int:id>', 
            views.update_cloth, 
            name='update_cloth'),

    path(
            'cloth-detail/<int:cloth_id>', 
            views.cloth_detail, 
            name='cloth_detail'),

    path(
            'delete-cloth/<int:cloth_id>', 
            views.delete_handler, 
            name='delete_cloth'),

    path(
            'create-new-user', 
            views.sign_up_handler,
            name='create_new_user'),

    path(
            'about-us', 
            views.about_us,
            name='about_us'),

    path(
            'contact-us', 
            views.contact_us,
            name='contact_us'),
]
