from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def home_view(request):
  return render(request, "pages/home.html", {})

def login_view(request):
  if request.user.is_authenticated:
    return redirect('/shop/')
  elif request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('/shop/')
    else:
      messages.error(request, "Invalid credentials, please try again")
      return redirect("/login/")

  return render(request, "pages/login.html", {})
 
def register_view(request):
  if request.user.is_authenticated:
    return redirect('/shop/')
  elif request.method == "POST":
    username = request.POST.get("username")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    email = request.POST.get("email")
    if password1 == password2:
      user = User.objects.create_user(username=username, password=password1)
      user.first_name = firstname
      user.last_name = lastname
      user.email = email
      user.save()
      return redirect('/login/')
    else:
      return redirect("/register/")
  
  return render(request, "pages/register.html", {})    

def shop_view(request):
  if not request.user.is_authenticated:
    return redirect('/')
  return render(request, 'pages/shop.html', {})

def log_out(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('/')
  else:
    return redirect('/')