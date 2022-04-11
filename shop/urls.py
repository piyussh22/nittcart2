from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginpage, name="login"),
    path("about/", views.about, name="AboutUs"),
    path("index/", views.index, name="index"),
    path("contact/", views.contact, name="ContactUs"),
    path("addproduct/", views.addproduct, name="AddProduct"),
    path("connectnitt/", views.home, name="home"),
  
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
   
    path('register/',views.register),
    path('loginpage/',views.loginpage),
    path('addpost/',views.addpost),
    path('registerhandle/',views.registerhandle),
    path('loginhandle/',views.loginhandle),
    path('posthandle/',views.posthandle),
    path('buy/<int:myid>',views.buy)

]
