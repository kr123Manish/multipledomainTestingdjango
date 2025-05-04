from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AdminOnlyView, ManagerOnlyView, ResearcherOnlyView,CreateReadUser,UpdateDeleteViewUser

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', AdminOnlyView.as_view()),
    path('manager/', ManagerOnlyView.as_view()),
    path('researcher/', ResearcherOnlyView.as_view()),
    path('users/', CreateReadUser.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UpdateDeleteViewUser.as_view(), name='user-retrieve-update-destroy'),
]

