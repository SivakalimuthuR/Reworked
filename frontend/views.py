# from django.shortcuts import render,redirect, get_object_or_404
# from . models import Product,Bid
# from .forms import ProductForm, BidForm
# from django.contrib import messages
# # products=[
# #         {'name':'Rolex watch', 'description': 'More stylish', 'Baseprice': '10,000', 'Currentprice': '15,000',},
# #         {'name':'MRF bat', 'description': 'This is the bat used by MSD', 'Baseprice': '100000', 'Currentprice': '1,50000'},
# #         {'name':'MobilePhone', 'description': '4GB RAM 128 ROM', 'Baseprice': '15000', 'Currentprice': '17054'},
# #         {'name':'Laptop', 'description': 'Ryen 5500 series', 'Baseprice': '45000', 'Currentprice': '47000'},
# #         {'name':'Android TV', 'description': 'Indias n0.1 TV brand', 'Baseprice': '35000', 'Currentprice': '40000'},
# #         {'name':'Keyboard', 'description': 'Long lastin', 'Baseprice': '15000', 'Currentprice': '40500'},
# #         {'name':'Wall clock', 'description': 'More durable', 'Baseprice': '25000', 'Currentprice': '40060'}
# #     ]

# def home(request):
#     products = Product.objects.all()
#     return render (request,'home.html', {"products":products})

# # def product_detail(request, pk):
# #     product = get_object_or_404(Product, pk=pk)
# #     return render(request, 'detail.html', {'product': product})


# def details(request):
#     products = Product.objects.all()
#     return render (request,'details.html', {"products":products})

# def post_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.posted_by = request.user
#             product.save()
#             messages.success(request,'product posted sucessfully')
#             return redirect('home')
#         else:
#             print(form.errors)
#             messages.error(request, "There is an error in this form")
#     else:
#         form = ProductForm()
#     return render(request, 'post_product.html', {'form': form})


# def my_listings(request):
#     products = Product.objects.filter(posted_by=request.user)
#     return render(request, 'auctions/my_listings.html', {'products': products})

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Product, Bid
# from .forms import ProductForm, BidForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# def home(request):
#     products = Product.objects.all()
#     return render(request, 'home.html', {"products": products})

# def details(request):
#     products = Product.objects.all()
#     return render(request, 'details.html', {"products": products})


# def post_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.posted_by = request.user
#             product.save()
#             messages.success(request, 'Product posted successfully')
#             return redirect('home')
#         else:
#             print(form.errors)
#             messages.error(request, "There is an error in this form")
#     else:
#         form = ProductForm()
#     return render(request, 'post_product.html', {'form': form})

# @login_required
# def my_listings(request):
#     user = request.user
#     products = Product.objects.filter(posted_by=user)
#     return render(request, 'antique/my_listings.html', {'products': products})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Bid
from .forms import ProductForm, BidForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {"products": products})



def details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    bids = product.bids.all()
    last_bid = bids.order_by('-created_at').first() if bids.exists() else None

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            new_bid = form.cleaned_data['bid_price']
            if (last_bid and new_bid <= last_bid.bid_price) or new_bid <= product.starting_price:
                messages.error(request, 'The new bid must be higher than the last bid and the starting price.')
            else:
                bid = form.save(commit=False)
                bid.product = product
                bid.user = request.user
                bid.save()
                messages.success(request, 'Bid placed successfully!')
                return redirect('details', pk=product.pk)
        else:
            messages.error(request, 'There was an error in your bid.')
    else:
        form = BidForm()
    return render(request, 'details.html', {'product': product, 'bids': bids, 'form': form, 'last_bid': last_bid})# def details(request):
#     products = Product.objects.all()
#     return render(request, 'details.html', {"products": products})

@login_required
def post_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.posted_by = request.user
            product.save()
            messages.success(request, 'Product posted successfully')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, "There is an error in this form")
    else:
        form = ProductForm()
    return render(request, 'post_product.html', {'form': form})

@login_required
def my_listings(request):
    products = Product.objects.filter(posted_by=request.user)
    return render(request, 'my_listings.html', {'products': products})

def login(request):
    return render(request, 'registration/login.html')
