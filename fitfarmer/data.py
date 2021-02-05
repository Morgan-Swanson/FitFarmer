import pandas as pd

def get_patient_csv_data(path):
    df = pd.read_csv(path, names=['BMI', 'Weight', 'Waist_cir', 'SysBP', 'DiaBP',
                                  'LDL', 'Cholesterol', 'Atherogenenciity', 'TAG',
                                  'FPG', 'HbA1c', 'CRP', 'PulseOx', 'ServGrain', 'ServFruit',
                                  'ServVeg', 'ServProtein', 'ServDairy', 'TotalCalories', 
                                  'EnergyCHO', 'EnergyPro', 'EnergyFat', 'VitD', 'VitE',
                                  'VitA', 'VitK', 'VitB12', 'Folate'], header=0)
    patient_data = df.to_dict(orient='records')
    return patient_data

