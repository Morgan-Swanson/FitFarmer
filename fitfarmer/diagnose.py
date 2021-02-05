class Diseases(Enum):
    # Diabetes
    DIABETIC = 1
    PREDIABETIC = 2
    
    # Obesity
    UNDERWEIGHT = 3
    OVERWEIGHT = 4
    OBESE = 5
def diagnose_diabetes(a1c):
    if a1c > 6.5:
        return 'diabetic'
    elif a1c > 5.7:
        return 'prediabetic'

def diagnose_obesity(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi > 30:
        return 'obese'
    elif bmi >= 25:
        return 'overweight'
    
    
def diagnose(patient):
    '''returns a list of diagnostics given a dictionary of patient data'''
    diagnostics = []
    diagnostics.append(diagnose_diabetes(patient['HbA1c']))
    return diagnostics
    
