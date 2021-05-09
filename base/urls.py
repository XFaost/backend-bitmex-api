from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.Orders.as_view()),
    path('orders/<str:order_id>/', views.Order.as_view()),
]
