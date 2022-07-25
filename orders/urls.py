from django.urls import path
from . import views

urlpatterns = [
    #all users
    path('',views.OrderListCreate.as_view(), name = "orders"),
    path('create/',views.OrderListCreate.as_view(), name = "create_order"),
    path('<int:pk>/',views.OrderDetail.as_view(), name = "retrieve_order"),
    path('<int:pk>/update',views.OrderDetail.as_view(), name = "update_order"),
    path('<int:pk>/delete',views.OrderDetail.as_view(), name = "delete_order"),

    #admin and staff
    path('update-status/<int:pk>/',views.OrderStatusUpdateView.as_view()),

]
