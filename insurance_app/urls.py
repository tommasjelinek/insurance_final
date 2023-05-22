from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('insurance', views.all_users, name="users_list"),
    path('products', views.all_products, name="products"),
    path('add_user', views.add_user, name="add_user"),
    path('show_user/<users_id>', views.show_user, name="show_user"),
    path('update_user/<users_id>', views.update_user, name="update_user"),
    path('delete_user/<users_id>', views.delete_user, name="delete_user"),





]
