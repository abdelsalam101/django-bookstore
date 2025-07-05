from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm

def login_pg(request):
    if request.user.is_authenticated:
        return redirect('books:book_list') 

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url) if next_url else redirect('books:book_list') 
        messages.info(request, "Username or password is incorrect")

    return render(request, 'books/login.html')  


def signout(request):
    logout(request)
    return redirect('accounts:login') 


def signup(request):
    if request.user.is_authenticated:
        return redirect("books:book_list")

    if request.method == "POST":
        signup_form = UserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(
                request,
                f"User account created for username: {signup_form.cleaned_data.get('username')}"
            )
            return redirect('accounts:login')
    else:
        signup_form = UserForm()

    context = {'signup_form': signup_form}
    return render(request, 'books/signup.html', context)
