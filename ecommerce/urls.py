from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clothing.urls')),
    path('cart/', include('cart.urls')),
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
]


if settings.DEBUG == True:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)