from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from .services.orders import view_active_orders, view_active_order, delete_order, create_order


class Orders(APIView):

    def get(self, request):
        return Response(view_active_orders(request))

    def post(self, request):
        return Response(create_order(request))


class Order(APIView):

    def get(self, request, order_id):
        return Response(view_active_order(request, order_id))

    def delete(self, request, order_id):
        return Response(delete_order(request, order_id))


class Subscribes(APIView):

    def get(self, request):
        return render(request, 'base/subscribes.html', {'text': 'test'})