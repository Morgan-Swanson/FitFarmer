from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=4)
    bmi = models.DecimalField('BMI', decimal_places=1, max_digits=4)
    weight = models.DecimalField('Weight (Kg)', decimal_places=1, max_digits=4)
    waist_cir = models.DecimalField('Waist Circumference (cm)', decimal_places=1, max_digits=4)
    sys_bp = models.DecimalField('Systolic Blood Pressure (mmHg)', decimal_places=1, max_digits=4)
    dia_bp = models.DecimalField('Diastolic Blood Pressure (mmHg)', decimal_places=1, max_digits=4)
    cholesterol = models.DecimalField('Total Cholesterol (mg/dL)', decimal_places=1, max_digits=4)
    hdl = models.DecimalField('HDL Cholesterol (mg/dL)', decimal_places=1, max_digits=4)
    ldl = models.DecimalField('LDL Cholesterol (mg/dL)', decimal_places=1, max_digits=4)
    atherogenicity = models.DecimalField('Atherogenicity Index (Total/HDL)', decimal_places=1, max_digits=4)
    tag = models.DecimalField('TAG (mg/dL)', decimal_places=1, max_digits=4)
    fpg = models.DecimalField('Fasting Plasma Glucose (mg/dL)', decimal_places=1, max_digits=4)
    hb_a1c = models.DecimalField('Hemoglobin A1c (%)', decimal_places=1, max_digits=4)
    crp = models.DecimalField('C-reactive Protein (mm/L)', decimal_places=1, max_digits=4)
    pulse_ox = models.DecimalField('Pulse Oximeter Measurement (%)', decimal_places=1, max_digits=4)

    def __str__(self):
        return self.name


class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consume_date = models.DateTimeField('date consumed', auto_now_add=True)
    servings = models.DecimalField('servings', decimal_places=1, max_digits=4, default=0)
    food_text = models.CharField(max_length=100)

    def __str__(self):
        return self.food_text


# class Macros(models.Model):
#     food = models.ForeignKey(Food, on_delete=models.CASCADE)
#     TotalCalories = models.DecimalField(decimal_places=10, max_digits=4, 'TotalCalories')
#     EnergyCHO = models.DecimalField(decimal_places=10, max_digits=4, 'EnergyCHO')
#     EnergyPro = models.DecimalField(decimal_places=10, max_digits=4, 'EnergyPro')
#     EnergyFat = models.DecimalField(decimal_places=10, max_digits=4, 'EnergyFat')
#     VitD = models.DecimalField(decimal_places=10, max_digits=4, 'VitD')
#     VitE = models.DecimalField(decimal_places=10, max_digits=4, 'VitE')
#     VitA = models.DecimalField(decimal_places=10, max_digits=4, 'VitA')
#     VitK = models.DecimalField(decimal_places=10, max_digits=4, 'VitK')
#     VitB12 = models.DecimalField(decimal_places=10, max_digits=4, 'VitB12')
#     Folate = models.DecimalField(decimal_places=10, max_digits=4, 'Folate')
#
#     def __str__(self):
#         return self.TotalCalories
#
