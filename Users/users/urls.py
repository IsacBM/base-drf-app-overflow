from django.urls import path
from .views import ChangePasswordPostView # Importa a View que criamos

app_name = 'users'

urlpatterns = [
    # Adicione esta linha:
    path('change-password/', ChangePasswordPostView.as_view(), name='change-password'),
]
