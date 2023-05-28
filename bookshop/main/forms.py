from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)


from .forms import AddToCartForm


def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            # Обробка додавання товару до кошика
            quantity = form.cleaned_data['quantity']
    else:
        form = AddToCartForm()

    return render(request, 'add_to_cart.html', {'form': form})

class OrderingForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)


from .forms import OrderingForm


def ordering(request):
    if request.method == 'POST':
        form = OrderingForm(request.POST)
        if form.is_valid():
            # Обробка створення замовлення
            quantity = form.cleaned_data['quantity']
    else:
        form = OrderingForm()

    return render(request, 'ordering.html', {'form': form})

class ListOfProductsForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)


from .forms import ListOfProductsForm


def list_of_products(request):
    if request.method == 'POST':
        form = ListOfProductsForm(request.POST)
        if form.is_valid():
            # Обробка відображення списку продуктів
            quantity = form.cleaned_data['quantity']
    else:
        form = ListOfProductsForm()

    return render(request, 'list_of_products.html', {'form': form})
