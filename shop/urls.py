
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('tracker/',views.tracker,name="tracker"),
    path('search/',views.search,name="search"),
    path("products/<int:myid>",views.productView,name="ProductView"),
    path('checkout/',views.checkout,name="checkout"),
    

]
