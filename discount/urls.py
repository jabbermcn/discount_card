from django.urls import path

from .views import *

urlpatterns = [
    path('card/add/', CardCreateView.as_view(), name='discount_card_add'),
    path('card/', CardListView.as_view(), name='discount_card_list'),
    path('card/<int:card_id>', CardDetailView.as_view(), name='discount_card_detail'),
]
