from django.urls import path

from . import views

urlpatterns =[
    path('users/', views.UsersList.as_view(), name = "users"),

    #all users
    path('auth/signup/',views.CreateUser.as_view(), name = "signup"),
    path('<slug:slug>/',views.RetrieveUpdateDeleteUser.as_view(), name = "retrieve_user"),
    path('<slug:slug>/update/',views.RetrieveUpdateDeleteUser.as_view(), name = "update_user"),
    path('<slug:slug>/delete/',views.RetrieveUpdateDeleteUser.as_view(), name = "delete_user"),

]
