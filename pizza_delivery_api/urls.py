from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('orders/', include("orders.urls")),
    path('', include("djoser.urls.jwt")),

]
