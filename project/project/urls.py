from django.contrib import admin
from django.urls import path
from carsuri import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.MainFunc),
    path('model/', views.ModelFunc),
    path('detail/', views.DetailFunc),
    # path('upload/', views.UploadImage),
    path('predict/', views.predict_images)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
