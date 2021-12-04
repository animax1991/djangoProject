from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product

# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#         else:
#             pass
#     context = {
#         "form": form
#     }
#     return render(request,"products/product_create.html",context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request,"products/product_create.html",context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request,"products/product_detail.html",context)
