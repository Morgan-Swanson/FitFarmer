from enum import Enum

class Disease(Enum):
    # Diabetes
    DIABETIC = 1
    PREDIABETIC = 2
    
    # Obesity
    UNDERWEIGHT = 3
    OVERWEIGHT = 4
    OBESE = 5
    
    
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
    
def diagnose(patient):
    '''returns a list of diagnostics given a dictionary of patient data'''
    diagnostics = []
    diagnostics.append(diagnose_diabetes(patient['HbA1c']))
    diagnostics.append(diagnose_obesity(patient['BMI']))
    diagnostics = [d for d in diagnostics if d is not None]
    return diagnostics
    
