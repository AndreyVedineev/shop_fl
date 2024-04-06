from django.shortcuts import render


# Create your views here.
def create_orders(request):
    return render(request, 'orders/create_order.html')
