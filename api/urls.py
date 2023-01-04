
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('about',AboutData),
    path('services', ServicesData),
    path('testimonial',TestimonialsData),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
] 
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



