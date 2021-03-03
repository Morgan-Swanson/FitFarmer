from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import NameForm
from .diagnose import diagnose


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_details(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # name = form.cleaned_data.get("name")
            # bmi = form.cleaned_data.get("bmi")
            # weight = form.cleaned_data.get("weight")
            # waist_Cir = form.cleaned_data.get("waist_Cir")
            # SysBP = form.cleaned_data.get("SysBP")
            # DiaBP = form.cleaned_data.get("DiaBP")
            # HDL = form.cleaned_data.get("HDL")
            # LDL = form.cleaned_data.get("LDL")
            # Cholesterol = form.cleaned_data.get("Cholesterol")
            # Atherogenenciity = form.cleaned_data.get("Atherogenenciity")
            # TAG = form.cleaned_data.get("TAG")
            # FPG = form.cleaned_data.get("FPG")
            # HbA1c = form.cleaned_data.get("HbA1c")
            # CRP = form.cleaned_data.get("CRP")
            # PulseOx = form.cleaned_data.get("PulseOx")
            # ServGrain = form.cleaned_data.get("ServGrain")
            # ServFruit = form.cleaned_data.get("ServFruit")
            # ServVeg = form.cleaned_data.get("ServVeg")
            # ServProtein = form.cleaned_data.get("ServProtein")
            # ServDairy = form.cleaned_data.get("ServDairy")
            # TotalCalories = form.cleaned_data.get("TotalCalories")
            # EnergyCHO = form.cleaned_data.get("EnergyCHO")
            # EnergyPro = form.cleaned_data.get("EnergyPro")
            # EnergyFat = form.cleaned_data.get("EnergyFat")
            # VitD = form.cleaned_data.get("VitD")
            # VitE = form.cleaned_data.get("VitE")
            # VitA = form.cleaned_data.get("VitA")
            # VitK = form.cleaned_data.get("VitK")
            # VitB12 = form.cleaned_data.get("VitB12")
            # Folate = form.cleaned_data.get("Folate")

            d = diagnose(form.cleaned_data)


            return render(request, 'name.html', {'diagnosis': d})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
