
from django.contrib import admin
from django.urls import path, include
# from api import views
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'student',views.Students, 'student')
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
