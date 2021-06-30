from django.contrib.auth import authenticate, login ,get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title" : "Hello world",
        "content" : "Welcome to the home page"
      }
    if request.user.is_authenticated():
        context["premium_content"]= "you are inside the bubble"  
    return render(request, "home_page.html", context)   

def about_page(request):
    context = {
        "title" : "about page",
        "content" : "welcome to about page"
    }    
    return render(request, "home_page.html", context) 

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "contact page",
        "content" : "welcome to contact page",
        "form"    : contact_form
        }    
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #commented because we are passing request.POST in contactform instace
    """if request.method == "POST":
        print(request.POST)
        print(request.POST.get("full_name"))
        print(request.POST.get("email"))
        print(request.POST.get("content"))"""
    return render(request, "contact/view.html", context)      

def login_page(request):
    context = {}
    form = LoginForm(request.POST or None)
    #predefined django method for authentication
    context["form"] = form
    print("User logged in: ",request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("user_name")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        print("our user",user)
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            # A backend authenticated the credentials
            #context['form'] = LoginForm()
            return redirect("/login")
        else:
            # No backend authenticated the credentials  
            print("Error")      
    return render(request,"auth/login.html", context)

User = get_user_model()  #predefined method
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    print("valid check")
    print(form.is_valid())
    if form.is_valid():
        print("valid")
        print(form.cleaned_data)
        context['form'] = RegisterForm()
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = User.objects.create_user(username, email, password)
        print(user)
    return render(request, "auth/register.html", context)    

def home_page_old(request):
    html_="""<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
  <div class = "text-center">
    <h1>Hello, world!</h1>
  </div>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
  </body>
</html>"""
    return HttpResponse(html_)
