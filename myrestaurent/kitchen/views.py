# # views.py
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import Order, OrderItem

# @csrf_exempt
# def receive_order(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         cart = data.get("cart", [])

#         if not cart:
#             return JsonResponse({"message": "Empty cart"}, status=400)

#         order = Order.objects.create()
#         for item in cart:
#             OrderItem.objects.create(
#                 order=order,
#                 name=item["name"],
#                 price=item["price"],
#                 quantity=item.get("quantity", 1)
#             )
#         return JsonResponse({"message": "Order received successfully!"})
#     return JsonResponse({"error": "Invalid request"}, status=400)

# def menu(request):
#     return render(request, 'kitchen/menu.html')

# def biriyani(request):
#     return render(request, 'kitchen/biriyani.html')

# def starters_non_veg(request):
#     return render(request, 'kitchen/starters(non-veg).html')

# def starters_veg(request):
#     return render(request, 'kitchen/starters(veg).html')

# def chinese_non_veg(request):
#     return render(request, 'kitchen/chinese(non-veg).html')

# def chinese_veg(request):
#     return render(request, 'kitchen/chinese(veg).html')

# def curry_non_veg(request):
#     return render(request, 'kitchen/curry(non-veg).html')

# def curry_veg(request):
#     return render(request, 'kitchen/curry(veg).html')

# def indian_breads(request):
#     return render(request, 'kitchen/Indian_breads.html')

# def mandi(request):
#     return render(request, 'kitchen/mandi.html')
# def add_ons(request):
#     return render(request, 'kitchen/add_ons.html')  # Make sure this template exists

# def cart_view(request):
#     return render(request, 'kitchen/cart.html')

# def owner_dashboard(request):
#     orders = Order.objects.prefetch_related('items').order_by('-created_at')
#     return render(request, "owner_dashboard.html", {"orders": orders})
# from django.shortcuts import get_object_or_404

# def print_order_slip(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     return render(request, "kitchen/order_slip.html", {"order": order})



from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date
from django.db.models import Count, Sum
from .models import Order, OrderItem

# -------------------- Order Receiving API --------------------
@csrf_exempt
def receive_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cart = data.get("cart", [])

        if not cart:
            return JsonResponse({"message": "Empty cart"}, status=400)

        order = Order.objects.create()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                name=item["name"],
                price=item["price"],
                quantity=item.get("quantity", 1)
            )
        return JsonResponse({"message": "Order received successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)

# -------------------- Customer Views --------------------
def menu(request):
    return render(request, 'kitchen/menu.html')

def biriyani(request):
    return render(request, 'kitchen/biriyani.html')

def starters_non_veg(request):
    return render(request, 'kitchen/starters(non-veg).html')

def starters_veg(request):
    return render(request, 'kitchen/starters(veg).html')

def chinese_non_veg(request):
    return render(request, 'kitchen/chinese(non-veg).html')

def chinese_veg(request):
    return render(request, 'kitchen/chinese(veg).html')

def curry_non_veg(request):
    return render(request, 'kitchen/curry(non-veg).html')

def curry_veg(request):
    return render(request, 'kitchen/curry(veg).html')

def indian_breads(request):
    return render(request, 'kitchen/Indian_breads.html')

def mandi(request):
    return render(request, 'kitchen/mandi.html')

def add_ons(request):
    return render(request, 'kitchen/add_ons.html')

def cart_view(request):
    return render(request, 'kitchen/cart.html')

# -------------------- Owner Dashboard --------------------
def owner_dashboard(request):
    # All orders
    orders = Order.objects.prefetch_related('items').order_by('-created_at')

    # Today's orders
    today = date.today()
    todays_orders = Order.objects.filter(created_at__date=today)

    # Count of items sold today
    items_today = OrderItem.objects.filter(order__created_at__date=today)
    total_items_sold = items_today.aggregate(total=Sum('quantity'))['total'] or 0

    # Per item count (group by name)
    item_counts = items_today.values('name').annotate(
        quantity_sold=Sum('quantity')
    ).order_by('-quantity_sold')

    return render(request, "kitchen/owner_dashboard.html", {
        "orders": orders,
        "todays_orders": todays_orders,
        "total_items_sold": total_items_sold,
        "item_counts": item_counts
    })

# -------------------- Print Order Slip --------------------
def print_order_slip(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "kitchen/order_slip.html", {"order": order})
