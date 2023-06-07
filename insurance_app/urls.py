from django.contrib import admin

from django.urls import path
from . import views



urlpatterns = [

#FUNGUJE, NESAHAT!!!!

    path('', views.home, name="home"),
    path('admin/', admin.site.urls, name="admin"),

   #USER C.R.U.D - url links

    path('insurance', views.all_users, name="users_list"),
    path('add_user', views.add_user, name="add_user"),
    path('show_user/<users_id>', views.show_user, name="show_user"),
    path('update_user/<users_id>', views.update_user, name="update_user"),
    path('delete_user/<users_id>', views.delete_user, name="delete_user"),

    # PRODUCT C.R.U.D - url links

    path('add_product', views.add_product, name="add_product"),
    path('products_list', views.products_list, name="products_list"),
    path('show_product/<product_id>', views.show_product, name="show_product"),
    path('update_product/<product_id>', views.update_product, name="update_product"),
    path('delete_product/<product_id>', views.delete_product, name="delete_product"),


    # CONTRACT C.R.U.D - url links

    path('create_contract', views.create_contract, name="create_contract"),

    path('update_contract/<vypis_id>', views.update_contract, name="update_contract"),
    path('delete_contract/<vypis_id>', views.delete_contract, name="delete_contract"),


# TESTOVACI:
    path('insurance/testovaci', views.testovaci, name="testovaci"),


]
