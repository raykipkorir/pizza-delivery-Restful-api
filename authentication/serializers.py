from rest_framework import serializers
from django.contrib.auth import get_user_model
from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    phone_number = PhoneNumberField()
    class Meta:
        model = User
        fields = ['id','username','email','phone_number','password']

        
    def validate_phone_number(self, number):
        if User.objects.filter(phone_number = number).exists():
            raise serializers.ValidationError("User with that phone number already exists")
        return number
