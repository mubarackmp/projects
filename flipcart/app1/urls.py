from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
	path('', views.all_products, name='all_products'),
	path('catogorizedproducts/<int:catogory_id>/', views.product_list, name='product_list'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('itempage/<int:p>/', views.itempage, name='itempage'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('logine/',views.user_logine,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('signup/',views.user_signup,name='user_signup'),
    path('search/',views.search,name='search'),

]
