from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Order, OrderItem, Payment, Review, Discount
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ویو برای نمایش لیست محصولات
class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})
    

    # ویو برای نمایش جزئیات محصول
class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        reviews = product.reviews.all()
        return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})
