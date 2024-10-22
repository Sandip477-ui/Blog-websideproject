from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='home'),
    path('post/<int:id>', views.single_post, name='single_post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  
]

# from django.urls import path
# from .views import index, single_post, about, contact

# urlpatterns = [
#     path('', index, name='home'),
#     path('post/<int:id>/', single_post, name='single_post'),  # single post URL
#     path('about/', about, name='about'),
#     path('contact/', contact, name='contact'),
# ]