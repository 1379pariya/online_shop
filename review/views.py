from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Order, OrderItem, Payment, Review, Discount
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ویو برای ایجاد نظرسنجی
@method_decorator(login_required, name='dispatch')
class CreateReviewView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        rating = request.POST['rating']
        comment = request.POST.get('comment', '')
        
        Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)
        return redirect('product_detail', pk=product.id)
