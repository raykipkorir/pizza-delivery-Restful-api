from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

#admin and staff
class UsersList(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()

    def get(self, request):
        user = User.objects.all()
        serializer = self.serializer_class(instance = user)
        return Response(serializer.data, status = status.HTTP_200_OK)


#all users
class CreateUser(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RetrieveUpdateDeleteUser(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def put(self,request, slug):
        data = request.data
        user = get_object_or_404(User, username = slug)
        serializer = self.serializer_class(data = data, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def get(self,request,slug):
        user = get_object_or_404(User, username = slug)
        serializer = self.serializer_class(instance = user)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self,request,slug):
        user = get_object_or_404(User, username = slug)
        user.delete()
        return Response("User deleted", status = status.HTTP_204_NO_CONTENT)

