from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    gender = forms.
    BMI = forms.DecimalField(label='BMI')
    Weight = forms.DecimalField(label='Weight')
    Waist_cir = forms.DecimalField(label='Waist_ir')
    SysBP = forms.DecimalField(label='SysBP')
    DiaBP = forms.DecimalField(label='DiaBP')
    HDL = forms.DecimalField(label='HDL')
    LDL = forms.DecimalField(label='LDL')
    Cholesterol = forms.DecimalField(label='Cholesterol')
    Atherogenenciity = forms.DecimalField(label='Atherogenenciity')
    TAG = forms.DecimalField(label='TAG')
    FPG = forms.DecimalField(label='FPG')
    HbA1c = forms.DecimalField(label='HbA1c')
    CRP = forms.DecimalField(label='CRP')
    PulseOx = forms.DecimalField(label='PulseOx')


class FoodForm(forms.Form):
    ServGrain = forms.DecimalField(label='ServGrain')
    ServFruit = forms.DecimalField(label='ServFruit')
    ServVeg = forms.DecimalField(label='ServVeg')
    ServProtein = forms.DecimalField(label='ServProtein')
    ServDairy = forms.DecimalField(label='ServDairy')
    TotalCalories = forms.DecimalField(label='TotalCalories')
    EnergyCHO = forms.DecimalField(label='EnergyCHO')
    EnergyPro = forms.DecimalField(label='EnergyPro')
    EnergyFat = forms.DecimalField(label='EnergyFat')
    VitD = forms.DecimalField(label='VitD')
    VitE = forms.DecimalField(label='VitE')
    VitA = forms.DecimalField(label='VitA')
    VitK = forms.DecimalField(label='VitK')
    VitB12 = forms.DecimalField(label='VitB12')
    Folate = forms.DecimalField(label='Folate')
