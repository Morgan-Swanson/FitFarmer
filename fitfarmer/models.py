from django.db import models

 
class User:
    name = models.CharField(label='Your name', max_length=100)
    gender = models.CharField(max_length=20)
    BMI = models.DecimalField(label='BMI')
    Weight = models.DecimalField(label='Weight')
    Waist_cir = models.DecimalField(label='Waist_ir')
    SysBP = models.DecimalField(label='SysBP')
    DiaBP = models.DecimalField(label='DiaBP')
    HDL = models.DecimalField(label='HDL')
    LDL = models.DecimalField(label='LDL')
    Cholesterol = models.DecimalField(label='Cholesterol')
    Atherogenenciity = models.DecimalField(label='Atherogenenciity')
    TAG = models.DecimalField(label='TAG')
    FPG = models.DecimalField(label='FPG')
    HbA1c = models.DecimalField(label='HbA1c')
    CRP = models.DecimalField(label='CRP')
    PulseOx = models.DecimalField(label='PulseOx')

    def __str__(self):
        return self.name


class Food:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consume_date = models.DateTimeField('date consumed', auto_now_add=True)
    servings = models.DecimalField(label='servings', default=0)
    food_text = models.CharField(max_length=100)

    def __str__(self):
        return self.food_text
