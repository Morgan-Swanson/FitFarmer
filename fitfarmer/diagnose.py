def diagnose_diabetes(A1c):
    if A1c > 6.5:
        return 'diabetic'
    elif A1c > 5.7:
        return 'prediabetic'
    else:
        return None

    
def diagnose(patient):
    '''returns a list of diagnostics given a dictionary of patient data'''
    diagnostics = []
    diagnostics.append(diagnose_diabetes(patient['HbA1c']))
    return diagnostics
    
