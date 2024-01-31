from django.urls import path
from .views import personal_list, personal_detail, raiz, globos_dibujo

urlpatterns = [
    path('', personal_list, name='personal_list'),
    path('<int:id>/', personal_detail, name='personal_detail'),
    path('globos/', globos_dibujo, name='globos')
]