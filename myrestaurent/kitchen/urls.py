# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('biriyani/', views.biriyani, name='biriyani'),
    path('starters-non-veg/', views.starters_non_veg, name='starters_non_veg'),
    path('starters-veg/', views.starters_veg, name='starters_veg'),
    path('chinese-non-veg/', views.chinese_non_veg, name='chinese_non_veg'),
    path('chinese-veg/', views.chinese_veg, name='chinese_veg'),
    path('curry-non-veg/', views.curry_non_veg, name='curry_non_veg'),
    path('curry-veg/', views.curry_veg, name='curry_veg'),
    path('indian-breads/', views.indian_breads, name='indian_breads'),
    path('add-ons/', views.add_ons, name='add_ons'),
    path('mandi/', views.mandi, name='mandi'),
    path('cart/', views.cart_view, name='cart'),
    path('receive_order/', views.receive_order, name='receive_order'),
    path("owner/dashboard/", views.owner_dashboard, name="owner_dashboard"),
    path("owner/print_order/<int:order_id>/", views.print_order_slip, name="print_order_slip"),

]
