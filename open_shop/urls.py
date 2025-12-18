from django.urls import path

from open_shop import views

urlpatterns = [
    path('', views.HelloWorld.as_view())
]
