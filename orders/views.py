from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Order
from .serializers import OrderSerializer, OrderStatusUpdateSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser



class OrderListCreate(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects

    def get(self, request):
        orders = self.queryset.filter(user =self.request.user)
        serializer = self.serializer_class(instance = orders, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK )
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data = data)
    
        if serializer.is_valid():
            serializer.save(user =self.request.user)
            return Response(data = serializer.data, status = status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class OrderDetail(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects
    
    def get_order(self,pk):
        return get_object_or_404(Order, pk =pk)
    
    def get(self, request, pk):
        order = self.queryset.filter(user =self.request.user).get(pk = pk)
        serializer = self.serializer_class(instance = order)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        order = self.get_order(pk)
        data = request.data
        serializer = self.serializer_class(instance=order, data = data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk):
        data = request.data
        order = self.get_order(pk)
        serializer = self.serializer_class(instance=order, data = data, partial = True)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk):
        order = self.get_order(pk)
        order.delete()
        return Response("Order deleted",status = status.HTTP_204_NO_CONTENT )


#admin and staff
class OrderStatusUpdateView(generics.GenericAPIView):
    serializer_class = OrderStatusUpdateSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        data = request.data
        order = get_object_or_404(Order, pk=pk)
        serializer = self.serializer_class(data = data, instance= order, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)

