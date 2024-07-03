# from django.urls import path
# from . import views

# urlpatterns=[
#     path('',views.home, name='home'),
#     path('details',views.details, name='details'),
#     # path('details/<int:pk>/', views.product_detail, name='product_detail'),
#     path('post-product/', views.post_product, name='post_product'),
#     path('my-listings/', views.my_listings, name='my_listings'),
# ]

from django.contrib import admin
from django.urls import path, include
from frontend import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('details/<int:pk>/', views.details, name='details'),
    path('post-product/', views.post_product, name='post_product'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('account/', include('django.contrib.auth.urls')),  # This line includes allauth URLs
    path('login/', views.login, name='login'),
]
