import json
import pandas as pd
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from.models import User
from .diagnose import diagnose
from django.views.generic import ListView, FormView


FOOD_BEV = pd.read_csv('data/food_bev_ontology.csv')
NUTR = pd.read_csv('data/nutrient_ontology.csv')
with open('data/msdps_categories.json') as infile:
    MSDPS = json.load(infile)


class UserList(ListView):
    model = User
    template_name = 'user_list.html'


class UserAdd(FormView):
    template_name = 'form.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def index(request):
    return render(request, 'index.html')

# def get_details(request):
#     form = UserForm()
#     return render(request, 'form.html', {'form': form})

# def save_details(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = UserForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("index"))