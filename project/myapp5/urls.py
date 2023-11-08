from django.urls import path
from .views import index, LastDay, ProductView


urlpatterns = [
    path('', index, name='index'),
    path('lastday/<int:client_id>/<int:days>', LastDay.as_view(), name='lastday'),
    path('product/', ProductView.as_view(), name='product_form'),
]
