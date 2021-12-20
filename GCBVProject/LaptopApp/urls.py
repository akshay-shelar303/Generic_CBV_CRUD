from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.LaptopCreateView.as_view(),name='add_laptop'),
    path('show/',views.LaptopListView.as_view(),name='show_laptop'),
    path('update/<int:pk>/',views.LaptopUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.LaptopDeleteView.as_view(),name='delete'),
]