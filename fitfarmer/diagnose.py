from enum import Enum


class Disease(Enum):
    # Diabetes
    DIABETIC = 1
    PREDIABETIC = 2

    # Obesity
    UNDERWEIGHT = 3
    OVERWEIGHT = 4
    OBESE = 5

    # PreDiabetes
    PrePreDIABETIC = 6
    TempPrePREDIABETIC = 7

    # Vitamin deficiencies
    VITAMIN_K_DEFICIENT = 8
    VITAMIN_B12_DEFICIENT = 9


def diagnose_diabetes(a1c):
    if a1c > 6.5:
        return Disease.DIABETIC
    elif a1c > 5.7:
        return Disease.PREDIABETIC


def diagnose_obesity(bmi):
    if bmi < 18.5:
        return Disease.UNDERWEIGHT
    elif bmi > 30:
        return Disease.OBESE
    elif bmi >= 25:
        return Disease.OVERWEIGHT


def diagnose_pre_diabetes(fpg):
    if fpg > 125:
        return Disease.PrePreDIABETIC
    elif fpg > 100:
        return Disease.TempPrePREDIABETIC


def diagnose_dietary_vitK(vitK):
    if vitK < 120:
        return Disease.VITAMIN_K_DEFICIENT


def diagnose_dietary_vitB12(vitB12):
    if vitB12 < 2.4:
        return Disease.VITAMIN_B12_DEFICIENT


def diagnose(patient):
    '''returns a list of diagnostics given a dictionary of patient data'''
    diagnostics = []
    diagnostics.append(diagnose_diabetes(patient['HbA1c']))
    diagnostics.append(diagnose_obesity(patient['BMI']))
    diagnostics.append(diagnose_pre_diabetes(patient['FPG']))
    diagnostics.append(diagnose_dietary_vitK(patient['VitK']))
    diagnostics.append(diagnose_dietary_vitB12(patient['VitB12']))
    diagnostics = [d for d in diagnostics if d is not None]
    return diagnostics
