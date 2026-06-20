from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("items/",views.items, name="all_items"),
    path("user/<int:user_id>/", views.user_details, name="user_details"),
    path("items/<int:item_id>/", views.item_details, name="item_details")
]
