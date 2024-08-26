from django.urls import path
from .views import ProductoListCreateView, index

urlpatterns = [
    path('api/productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('', index, name='index'),


]
