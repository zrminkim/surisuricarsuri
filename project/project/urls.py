from django.contrib import admin
from django.urls import path
from carsuri import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.MainFunc),
    path('model', views.ModelFunc)
]
