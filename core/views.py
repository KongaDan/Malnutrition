from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def stat_province(request):
    provinces = Province.objects.all()
    return render(request,'stat_province.html',{'provinces':provinces})


@login_required
def stat_zone(request):
    zone_sanitaires = ZoneSanitaire.objects.all()
    return render(request,'stat_zone.html',{'zone_sanitaires':zone_sanitaires})

@login_required
def stat_aire(request):
    aire_sanitaires = AireSanitaire.objects.all()
    return render(request,'stat_aire.html',{'aire_sanitaires':aire_sanitaires})

def login_page(request):
    if request.method=='POST':
        name=request.POST['username']
        pword=request.POST['password']
        user=authenticate(request,username=name,password=pword)
        if user is not  None:
            login(request,user )
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            message='l\'email ou le mot de passe est incorrecte '
            return render(request,'login.html',{'message':message})
    return render(request,'login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@login_required
def province_list(request):
    provinces = Province.objects.all()
    return render(request,'province_list.html',{'provinces':provinces})

@login_required
def zone_sanitaire_list(request): 
    zone_sanitaires = ZoneSanitaire.objects.all()
    return render(request,'zone_sanitaire_list.html',{'zone_sanitaires':zone_sanitaires,'view':'create'})

@login_required
def aire_sanitaire_list(request):
    aire_sanitaires = AireSanitaire.objects.all()
    return render(request,'aire_sanitaire_list.html',{'aire_sanitaires':aire_sanitaires})

@login_required
def province_create(request):
    view = 'Nouvelle'
    form = ProvinceForm()
    if request.method =="POST":
        form = ProvinceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:province_list')
    return render(request,'province_create.html',{'form':form,'view':view})

@login_required
def zone_sanitaire_create(request):
    view = 'Nouvelle'
    form = ZoneSanitaireForm()
    if request.method=="POST":
        form = ZoneSanitaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:zone_sanitaire_list')
    return render(request,'zone_sanitaire_create.html',{'form':form,'view':view})

@login_required
def aire_sanitaire_create(request):
    form = AireSanitaireForm()
    view = 'Nouvelle'
    if request.method == "POST":
        form = AireSanitaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:aire_sanitaire_list')
    return render(request,'aire_sanitaire_create.html',{'form':form,'view':view})

@login_required
def province_update(request, pk):
    view='Modifier'
    province = Province.objects.get(pk=pk)
    form = ProvinceForm(instance = province)
    if request.method == "POST":
        form = ProvinceForm(request.POST,instance = province)
        if form.is_valid():
            form.save()
        return redirect('core:province_list')
    return render(request,'province_create.html',{'form':form,'view':view})

@login_required
def zone_sanitaire_update(request, pk):
    view = 'Modifier'
    zone_sanitaire = ZoneSanitaire.objects.get(pk=pk)
    form = ZoneSanitaireForm(instance = zone_sanitaire)
    if request.method == "POST":
        form = ZoneSanitaireForm(request.POST,instance = zone_sanitaire)
        if form.is_valid():
            form.save()
        return redirect('core:zone_sanitaire_list')
    return render(request,'zone_sanitaire_create.html',{'form':form,'view':view})

@login_required
def aire_sanitaire_update(request, pk):
    view = 'Modifier'
    aire_sanitaire = AireSanitaire.objects.get(pk=pk)
    form = AireSanitaireForm(instance = aire_sanitaire)
    if request.method == "POST":
        form = AireSanitaireForm(request.POST,instance = aire_sanitaire)
        if form.is_valid():
            form.save()
        return redirect('core:aire_sanitaire_list')
    return render(request,'aire_sanitaire_create.html',{'form':form,'view':view})
