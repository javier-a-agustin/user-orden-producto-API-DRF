from django.shortcuts import render

from rest_framework import permissions

from django.contrib.auth import authenticate

from rest_framework import generics, status, viewsets

from rest_framework.exceptions import PermissionDenied

from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import OrderDescription, Order, Product
from .serializers import OrderDescriptionSerializer, OrderSerializer, ProductSerializer, UserSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    # Custom permission
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.order.createdBy == request.user

class OptionsList(generics.ListAPIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        data = {
            "options": "/",
            "list of products": "products/",
            "create a product": "create-product/",
            "product detail": "product-detail/<int:pk>/",
            "list of orders that belong to a logged in user": "orders/",
            "order detail that belong to a logged in user": "order-detail/<int:pk>/",
            "list of all the details that belong to a order": "order-detail-list/<int>pk>/",
            "create detail for a order - product related": "create-detail-list/<int:pk>/product/<int:product_pk>/",
            "create a user": "users/",
            "log in a user - return a token if user is valid": "login/",
        }
        
        return Response(data)


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            user.a
            return Response({'Token': user.auth_token.key})
        else:
            return Response({'Error': 'Wron Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ProductList(generics.ListAPIView):

    permission_classes = ()
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    serializer_class = ProductSerializer

class CreateProduct(generics.CreateAPIView):
    #*
    permission_classes = (IsAdminUser, )
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        queryset = Product.objects.filter(pk=self.kwargs['pk'])
        return queryset 
    serializer_class = ProductSerializer

class OrderList(generics.ListCreateAPIView):
    # List of all orders that owns a user
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        queryset = Order.objects.filter(createdBy=self.request.user)
        return queryset

    serializer_class = OrderSerializer

class OrderDetailList(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        queryset = OrderDescription.objects.filter(order=self.kwargs['pk'])
        return queryset
    
    serializer_class = OrderDescriptionSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):           
    # list all the Order description in a order
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        queryset = OrderDescription.objects.filter(order=self.kwargs['pk'])
        return queryset

    serializer_class = OrderDescriptionSerializer

class OrderDetailCreate(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        queryset = OrderDescription.objects.filter(order=self.kwargs['pk'])
        return queryset
    
    serializer_class = OrderDescriptionSerializer

    def post(self, request, pk, product_pk):
        
        quantity = request.data.get('quantity')
        data = {'order': pk, 'product': product_pk, 'quantity': quantity}
        serializer = OrderDescriptionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)