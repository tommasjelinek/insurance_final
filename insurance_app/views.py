from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Database Tables:

from .models import Users

from .models import Contract

from .models import Product



# User, Product, Contract forms:

from .forms import UserForm
from .forms import ContractForm
from .forms import ProductForm





def home(request):
    return render(request, 'insurance/home.html')

def testovaci(request):
    return render(request, 'insurance/testovaci.html')

def all_users(request):
    users_list = Users.objects.all().order_by('last_name')
    return render(request, 'insurance/users_list.html',
                  {'users_list': users_list})

# UZIVATEL C.R.U.D

def add_user(request):
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_user?submitted=True')

    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'insurance/add_user.html', {'form': form, 'submitted': submitted})
def show_user(request, users_id):
    user = Users.objects.get(pk=users_id)
    return render(request, 'insurance/show_user.html',
                  {'user': user})

def update_user(request, users_id):
    user = Users.objects.get(pk=users_id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return  redirect('users_list')

    return render(request, 'insurance/update_user.html',
                  {'user': user,
                   'form': form})

def delete_user(request, users_id):
    user = Users.objects.get(pk=users_id)
    user.delete()
    return redirect('users_list')


#--------------------------------------------------------------------------

# PRODUCT C.R.U.D:

def add_product(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_product?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'insurance/add_product.html', {'form': form, 'submitted': submitted})

def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products_list?submitted=True')



    return render(request, 'insurance/update_product.html',
                  {'product': product, 'form': form})

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products_list')

def show_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'insurance/show_product.html',
                  {'product': product})

def products_list(request):
    products_list = Product.objects.all()
    return render(request, 'insurance/products_list.html',
                  {'products_list': products_list})


# POJISTENI C.R.U.D

def create_contract(request):
    submitted = False
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_contract?submitted=True')
    else:
        form = ContractForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'insurance/create_contract.html', {'form': form, 'submitted': submitted})

def update_contract(request, vypis_id):
    contract = Contract.objects.get(pk=vypis_id)
    form = ContractForm(request.POST or None, instance=contract)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/insurance?submitted=True')
        #return HttpResponseRedirect('/insurance')



    return render(request, 'insurance/update_contract.html',
                  {'contract': contract, 'form': form})

def delete_contract(request, vypis_id):
    contract = Contract.objects.get(pk=vypis_id)
    contract.delete()
    return redirect('users_list')








# NEFUNGUJE








"""

def add_product(request):
    submitted = False
    if request.method == "POST":
        form = PojisteniForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_product?submitted=True')

    else:
        form = PojisteniForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'insurance/create_contract.html', {'form': form, 'submitted': submitted})


"""



