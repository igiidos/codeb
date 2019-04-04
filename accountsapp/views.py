from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'accountsapp/signup_form.html', {
        'form': form,
    })


def profile(request):
    return render(request, 'accountsapp/profile.html')


class Loginviews(LoginView):
    template_name = 'accountsapp/login.html'


loginview = Loginviews.as_view()


class LogoutViews(LogoutView):
    next_page = settings.LOGIN_URL


logoutview = LogoutViews.as_view()