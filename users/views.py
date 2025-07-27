from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login_view')
        else:
            return render(request, 'users/register.html', context={'form': form})
    
    form = UserCreationForm()

    return render(request, 'users/register.html', context={'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('post_list')
        else:
            return render(request, 'users/login.html', context={'form': form})

    form = AuthenticationForm()

    return render(request, 'users/login.html', context={'form': form})

def logout_view(request):
    logout(request)

    return redirect('post_list')