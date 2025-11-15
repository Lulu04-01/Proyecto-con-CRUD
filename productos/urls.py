from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductoListCreate.as_view(), name='productos-list'),
    path('productos/<int:pk>/', views.ProductoRetrieveUpdateDestroy.as_view(), name='productos-detail'),
]
