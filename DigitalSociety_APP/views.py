from django.shortcuts import render,redirect
from .models import *

default_dic = {
    'acc_page' : ['index', 'profile_page'],
    'class_bg' : "register_page",
    'class_login_bg' : "login_page",
    'class_forgot_bg': "forgot_password"
}

def index(request):
    default_dic['current_page'] = 'index'
    return render(request, 'index.html', default_dic)

def register_page(request):
    default_dic['current_page'] = 'register_page'
    default_dic['class'] = 'register_page'
    default_dic["roles"] = [role for role in Role.objects.all()]
    return render(request, 'register_page.html', default_dic)

def login_page(request):
    default_dic['current_page'] = 'login_page'
    default_dic['class'] = 'login_page'
    return render(request, 'login_page.html', default_dic)

def forgot_password(request):
    default_dic['current_page'] = 'forgot_password'
    default_dic['class'] = 'forgot_password'
    return render(request, 'forgot_password.html', default_dic)

def register(request):
    role = Role.objects.get(id=int(request.POST['role']))
    request.session['email'] = request.POST['email']
    
    master = Master.objects.create(
        Role = role,
        Email = request.POST['email'],
        Password = request.POST['password'],
        Mobile = request.POST['mobile'],
    )
    if role.Name == 'society_member':
        
        Society_member.objects.create(
            Master = master,
           
        )
    else:
        Society_secretary.objects.create(
            Master = master,
        )

    return redirect(login_page)

def login(request):
    master = Master.objects.get(Email=request.POST['email'])
    
    if master.Password == request.POST['password']:
        request.session['email'] = master.Email
        if master.IsActive:
           
            return redirect(index)
        else:
            master.IsActive = True
            return redirect(index)
    else:
        return redirect(index)
