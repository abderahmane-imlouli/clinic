from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .views import AppointmentViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('signup/', views.SignUpView.as_view(), name='signup'), 
     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


