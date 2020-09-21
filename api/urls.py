from django.urls import path

from .views import ProductList, CreateProduct, OrderList, UserCreate, LoginView, ProductDetail,OrderDetail, OrderDetailCreate, OrderDetailList, OptionsList

from rest_framework.authtoken import views


urlpatterns = [
    path('', OptionsList.as_view(), name='options-list'),
    path('products/', ProductList.as_view(), name='products-list'), 
    path('create-product/', CreateProduct.as_view(), name='create-product'), 
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'), 
    path('orders/', OrderList.as_view(), name='order-list'), 
    path('order-detail/<int:pk>/', OrderDetail.as_view(), name='order-detail'), 
    
    path('order-detail-list/<int:pk>/', OrderDetailList.as_view(), name='order-detail-list'),
    
    path('create-detail/<int:pk>/product/<int:product_pk>/', OrderDetailCreate.as_view(), name='create-detail'), 
    
    path('users/', UserCreate.as_view(), name='user-create'),
    path('login/', views.obtain_auth_token, name='login'),
]