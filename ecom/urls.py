
from django.urls import path
from ecom import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.about, name='About Us'),
    path('contact/', views.contact, name='Contact Us'),
    path('tracker/', views.tracker, name='Tracking Status'),
    path('search/', views.search, name='Search'),
    path('productview/<int:id>', views.productView, name='Search'),
    path('checkout/', views.checkout, name='Checkout'),
    # path('handlerequest/', views.handlerequest, name='HandleRequest'),

]
