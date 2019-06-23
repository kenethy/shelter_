from django.shortcuts import render
from .models import Unburden

# Create your views here.
def dashboard(request):
    data = {}
    return render(request, 'shelter_dashboard/dashboard.html', data)

def home(request):
    data = {}
    return render(request, 'shelter_dashboard/home.html', data)

def unburden(request):
    data = {}
    data['unburden'] = Unburden.objects.all()
    return render(request, 'shelter_dashboard/unburden.html', data)

def base(request):
    data = {}
    return render(request, 'shelter_dashboard/base.html', data)

def index(request):
    data = {}
    return render(request,'shelter_dashboard/rotas/index.html', data)

def login(request):
    data = {}
    return render(request, 'shelter_dashboard/rotas/login.html', data)

def password(request):
    data = {}
    return render(request, 'shelter_dashboard/rotas/forgot-password.html',data)

