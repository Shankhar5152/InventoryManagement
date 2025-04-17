from django.urls import path
from .views import (
    StockListView,
    StockCreateView,
    StockUpdateView,
    StockDeleteView,
)

urlpatterns = [
    path('', StockListView.as_view(), name='inventory'),  # Lists all stocks
    path('add/', StockCreateView.as_view(), name='add-stock'),  # Add new stock
    path('edit/<int:pk>/', StockUpdateView.as_view(), name='edit-stock'),  # Edit stock with pk
    path('delete/<int:pk>/', StockDeleteView.as_view(), name='delete-stock'),  # Delete stock with pk
]
