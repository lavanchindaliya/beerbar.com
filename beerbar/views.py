from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .models import Rum, Task, Beer, Whisky, Gin, Mezcal, Wine, Vodka,  Order
from django.template import loader
from .serializers import TaskSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework.generics import  CreateAPIView
from datetime import datetime
from django.db.models import Sum
from .forms import SignUPFrom, ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


#logout function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


#prfile view function
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated!!')
                fm.save()
                fm = ProfileForm(instance= request.user)
        else:
            fm = ProfileForm(instance= request.user)
        return render(request, 'beerbar/profile.html', {'name': request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login')
#signup view

def sign_up(request): 
    if request.method == "POST":
        fm = SignUPFrom(request.POST)
        if fm.is_valid():
            # messages.success(request, 'Account Created Sucessfully !!')
            fm.save()
            return HttpResponseRedirect('/login')
            
    else:
        fm = SignUPFrom()
    return render(request, 'beerbar/sign_up.html', {'form':fm})


#login view function
def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'beerbar/profile.html', {'name': request.user})
    else:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile')
                else:
                    messages.success(request, 'invalid user OR password !!')
                    fm = AuthenticationForm()

        else:
            fm = AuthenticationForm()
        return render(request, 'beerbar/userlogin.html', {'form': fm})




def index(request):
    return render(request, 'beerbar/index.html')
    

def add_to_cart(request, name, price, category):
    if request.user.is_authenticated:
            if request.method == 'POST':
                pi = Order()
                pi.customer = request.user
                pi.name = name
                pi.price = price
                pi.save()
            if category == 'vodka':
                return HttpResponseRedirect('/products_vodka')
            elif category == 'rum':
                return HttpResponseRedirect('/products_rum')
            elif category == 'whisky':
                return HttpResponseRedirect('/products_whisky')
            elif category == 'gin':
                return HttpResponseRedirect('/products_gin')
            elif category == 'mezcal':
                return HttpResponseRedirect('/products_mezcal')
            elif category == 'wine':
                return HttpResponseRedirect('/products_wine')
    else:
        return HttpResponseRedirect('/login')


def delete(request, id):
    if request.method == 'POST':
        pi = Order.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/yourorder')



def products(request):
    all_whisky = Whisky.objects.all()
    all_rum = Rum.objects.all()
    all_vodka = Vodka.objects.all()
    all_beer = Beer.objects.all()
    all_gin = Gin.objects.all()
    all_wine = Wine.objects.all()
    all_mezcal = Mezcal.objects.all()
    template = loader.get_template('beerbar/products.html')
    context = {
        'all_vodka': all_vodka,
        'all_beer': all_beer,
        'all_gin': all_gin,
        'all_wine': all_wine,
        'all_mezcal': all_mezcal,
        'all_rum': all_rum,
        'all_whisky': all_whisky
        
        
    }
    return HttpResponse(template.render(context, request))





def products_whisky(request):
    all_whisky = Whisky.objects.all()
    template = loader.get_template('beerbar/products_whisky.html')
    context = {
        'all_whisky': all_whisky
    }
    return HttpResponse(template.render(context, request))



def products_rum(request):
    all_rum = Rum.objects.all()
    template = loader.get_template('beerbar/products_rum.html')
    context = {
        'all_rum': all_rum
    }
    return HttpResponse(template.render(context, request))
 

def products_vodka(request):
    all_vodka = Vodka.objects.all()
    template = loader.get_template('beerbar/products_vodka.html')
    context = {
        'all_vodka': all_vodka
    }
    return HttpResponse(template.render(context, request))


def products_beer(request):
    all_beer = Beer.objects.all()
    template = loader.get_template('beerbar/products_beer.html')
    context = {
        'all_beer': all_beer
    }
    return HttpResponse(template.render(context, request))


def products_gin(request):
    all_gin = Gin.objects.all()
    template = loader.get_template('beerbar/products_gin.html')
    context = {
        'all_gin': all_gin
    }
    return HttpResponse(template.render(context, request))


def products_wine(request):
    all_wine = Wine.objects.all()
    template = loader.get_template('beerbar/products_wine.html')
    context = {
        'all_wine': all_wine
    }
    return HttpResponse(template.render(context, request))


def products_mezcal(request):
    all_mezcal = Mezcal.objects.all()
    template = loader.get_template('beerbar/products_mezcal.html')
    context = {
        'all_mezcal': all_mezcal
    }
    return HttpResponse(template.render(context, request))



def contact(request):
    return render(request, 'beerbar/contact.html')


def vision(request):
    return render(request, 'beerbar/vision.html')


def yourorder(request):
    if request.user.is_authenticated:
        all_orders = Order.objects.filter(customer=request.user)
        template = loader.get_template('beerbar/yourorder.html')
        total = Order.objects.filter(customer=request.user).aggregate(Sum('price'))
        context = {
            'all_orders':all_orders,
            'total': total
    
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('login/')



# def testView(request):
#     all_rum = Rum.objects.all()
#     context = {
#         'all_rum': all_rum
#     }
#     return render(request, 'beerbar/testView.html', context)




class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('completed',)
    ordering = ('-date_created',)
    search_fields = ('task_name',)


class CreateuserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer




# class DueTaskViewSet(viewsets.ModelViewSet):
#
#     queryset = Task.objects.all().order_by('date_created').filter(completed=False)
#     serializer_class = TaskSerializer
#
#
# class CompletedTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('date_created').filter(completed=True)
#     serializer_class = TaskSerializer
