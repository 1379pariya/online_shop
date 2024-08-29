from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Order, OrderItem, Payment, Review, Discount
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ویو برای نمایش تخفیف‌ها
class DiscountListView(View):
    def get(self, request):
        discounts = Discount.objects.all()
        return render(request, 'discount_list.html', {'discounts': discounts})