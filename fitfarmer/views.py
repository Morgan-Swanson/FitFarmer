from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm
from .diagnose import diagnose



def index(request):
    return render(request, 'index.html')


def get_details(request):
    form = NameForm()
    return render(request, 'form.html', {'form': form})

def save_details(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))