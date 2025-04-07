from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form}) 

def home(request):
    return render(request, 'home.html')