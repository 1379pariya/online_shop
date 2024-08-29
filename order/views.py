from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Order, OrderItem, Payment, Review, Discount
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ویو برای ایجاد سفارش
@method_decorator(login_required, name='dispatch')
class CreateOrderView(View):
    def post(self, request):
        cart_items = request.POST.getlist('cart_items')  # فرض بر این است که آیتم‌های سبد خرید به صورت لیست ارسال شده‌اند
        order = Order.objects.create(user=request.user)
        total_amount = 0
        
        for item in cart_items:
            product_id, quantity = item.split(':')  # فرض بر این است که هر آیتم به صورت "product_id:quantity" ارسال شده است
            product = get_object_or_404(Product, id=product_id)
            total_amount += product.price * int(quantity)
            OrderItem.objects.create(order=order, product=product, quantity=int(quantity), price=product.price)

        order.total_amount = total_amount
        order.save()
        return redirect('order_detail', pk=order.pk)

# ویو برای نمایش جزئیات سفارش
@method_decorator(login_required, name='dispatch')
class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'order_detail.html', {'order': order})