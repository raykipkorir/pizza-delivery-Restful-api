from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default = 'PENDING', read_only = True)
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['size','order_status', 'quantity','created_at','updated_at']
          
class OrderStatusUpdateSerializer(serializers.Serializer):
    order_status = serializers.CharField(default = "PENDING")
    def update(self, instance, validated_data):
        instance.order_status = validated_data.get("order_status",instance.order_status)
        instance.save()
        return instance
