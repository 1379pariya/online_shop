from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Order, OrderItem, Payment, Review, Discount
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ویو برای ایجاد پرداخت
@method_decorator(login_required, name='dispatch')
class CreatePaymentView(View):
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        amount = order.total_amount  # فرض بر این است که مبلغ پرداختی برابر با مبلغ کل سفارش است
        payment_method = request.POST['payment_method']
        
        Payment.objects.create(order=order, amount=amount, payment_method=payment_method, status='completed')
        order.status = 'completed'
        order.save()
        
        return redirect('order_detail', pk=order.id)
