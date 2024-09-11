from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import NewOrderForm


@login_required
def all_orders(request):
    return render(request, 'orders/all_orders.html', context={'page_title': 'Заказы'})


@login_required
def my_orders(request):
    return render(request, 'orders/my_orders.html', context={'page_title': 'Мои заказы'})


@login_required
def add_new(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST, user_id=request.user.id)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(to='my-orders-page')
    return render(request, 'orders/add_order.html', context={'page_title': 'Новый заказ'})
