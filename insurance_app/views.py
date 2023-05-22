from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Users
from .models import Pojisteni

from .forms import UserForm

def home(request):
    return render(request, 'insurance/home.html')

def all_users(request):
    users_list = Users.objects.all().order_by('last_name')
    return render(request, 'insurance/users_list.html',
                  {'users_list': users_list})

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
    return render(request, 'insurance/add_user.html', {'form':form, 'submitted':submitted})

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

def all_products(request):
    product_list = Pojisteni.objects.all()
    return render(request, 'insurance/products.html',
                  {'product_list': product_list})
