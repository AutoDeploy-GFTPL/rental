from django.urls import path
from . import views
from . models import *


urlpatterns = [
    path('',views.Homepage, name="index"),
    path('apartment/',views.PropertyPage, name="apartment"),
    path('apartment_detail/<slug>',views.apartmentDetailPage, name="apartment-detail"),
    path('gallery/',views.GalleryPage, name="gallery"),
    path('contact/',views.ContactPage, name="contact"),
    path('about/',views.AboutPage, name="about"),
    path('blogs/',views.blogPage, name="blogs"),
    path('blogs_detail/<slug>',views.blogsDetail, name="blogs_detail"),
]