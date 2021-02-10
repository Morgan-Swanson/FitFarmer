from enum import Enum


class Disease(Enum):
    def __str__(self):
        return str(self.value)

    # Diabetes
    DIABETIC = 1
    PREDIABETIC = 2

    # Obesity
    UNDERWEIGHT = 3
    OVERWEIGHT = 4
    OBESE = 5

    # Any of the energy things
    LOW = 6
    HIGH = 7

    # PreDiabetes
    PrePreDIABETIC = 8
    TempPrePREDIABETIC = 9

    # Vitamin deficiencies
    VITAMIN_K_DEFICIENT = 10
    VITAMIN_B12_DEFICIENT = 11


def diagnose_diabetes(a1c):
    if a1c > 6.5:
        return Disease.DIABETIC.name
    elif a1c > 5.7:
        return Disease.PREDIABETIC.name


def diagnose_obesity(bmi):
    if bmi < 18.5:
        return Disease.UNDERWEIGHT.name
    elif bmi > 30:
        return Disease.OBESE.name
    elif bmi >= 25:
        return Disease.OVERWEIGHT.name


def diagnose_pre_diabetes(fpg):
    if fpg > 125:
        return "FPG is High: " + Disease.PrePreDIABETIC.name
    elif fpg > 100:
        return "FPG is borderline: " + Disease.TempPrePREDIABETIC.name


def diagnose_dietary_vitA(vitA):
    if vitA < 900:
        return "Vitamin A: " + Disease.LOW.name
    elif vitA > 3000:
        return "Vitamin A: " + Disease.HIGH.name


def diagnose_dietary_vitB12(vitB12):
    if vitB12 < 2.4:
        return "Vitamin B12: " + Disease.LOW.name


def diagnose_dietary_vitD(vitD):
    if vitD < 600:
        return "Vitamin D: " + Disease.LOW.name
    elif vitD > 3000:
        return "Vitamin D: " + Disease.HIGH.name


def diagnose_dietary_vitE(vitE):
    if vitE < 15:
        return "Vitamin E: " + Disease.LOW.name
    elif vitE > 900:
        return "Vitamin E: " + Disease.HIGH.name


def diagnose_dietary_vitK(vitK):
    if vitK < 120:
        return "Vitamin K: " + Disease.LOW.name


def diagnose(patient):
    '''returns a list of diagnostics given a dictionary of patient data'''
    diagnostics = []
    diagnostics.append(diagnose_diabetes(patient['HbA1c']))
    diagnostics.append(diagnose_obesity(patient['BMI']))
    diagnostics.append(diagnose_pre_diabetes(patient['FPG']))
#    diagnostics.append(diagnose_dietary_vitA(patient['VitA']))
    diagnostics.append(diagnose_dietary_vitB12(patient['VitB12']))
    diagnostics.append(diagnose_dietary_vitD(patient['VitD']))
    diagnostics.append(diagnose_dietary_vitE(patient['VitE']))
    diagnostics.append(diagnose_dietary_vitK(patient['VitK']))
    diagnostics = [d for d in diagnostics if d is not None]
    return diagnostics
