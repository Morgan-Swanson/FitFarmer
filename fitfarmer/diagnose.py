from enum import Enum
from .models import User


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

    # Hypertension
    Hypertension = 10


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
        return "FPG is borderline"


def diagnose_hypertension(sysBP, diaBP):
    if (sysBP > 180) and (diaBP > 120):
        return "Hypertensive Crisis"
    elif (sysBP > 140) and (diaBP > 90):
        return "Hypertensive Stage 2"
    elif (sysBP > 130) and (diaBP > 80):
        return "Hypertensive Stage 1"


def diagnose_dyslipidemia(Total, LDL, HDL, TAG):
    if (Total < 200) and (LDL < 100) and (HDL > 60) and (TAG < 150):
        return "Desireable Cholestrol"
    elif (Total > 239) and (LDL > 160) and (HDL < 40) and (TAG > 200):
        return "Dyslipidemia Crisis - all levels at risk"
    elif (Total > 239):
        if (LDL > 160) or (HDL < 40) or (TAG > 200):
            return "Dyslipidemia Crisis - Total cholestrol and one additional level at risk"
    elif (LDL > 160):
        if (Total > 239) or (HDL < 40) or (TAG > 200):
            return "Dyslipidemia Crisis - LDL too high and one additional level at risk"
    elif (HDL < 40):
        if (Total > 239) or (LDL > 160) or (TAG > 200):
            return "Dyslipidemia Crisis - HDL too low and one additional level at risk"
    elif (Total > 200):
        if (LDL > 100) or (HDL > 40) or (TAG > 150):
            return "Dyslipidemia Borderline - two or more levels borderline."
    elif (LDL > 100):
        if (Total > 200) or (HDL > 40) or (TAG > 150):
            return "Dyslipidemia Borderline - two or more levels borderline."
    elif (HDL > 40):
        if (Total > 200) or (LDL > 100) or (TAG > 150):
            return "Dyslipidemia Borderline - two or more levels borderline."
    elif (Total > 200) or (LDL > 100) or (HDL > 40) or (TAG > 150):
        return "Dyslipidemia Borderline - one level borderline."


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


def diagnose_dietary_folate(folate):
    if folate < 400:
        return "Folate level: " + Disease.LOW.name
    elif folate > 1000:
        return "Folate level: " + Disease.HIGH.name


def diagnose_fat(fat_levels):
    if fat_levels < 20:
        return "Fat levels: " + Disease.LOW.name
    elif fat_levels > 35:
        return "Fat levels: " + Disease.HIGH.name


def diagnose_CHO(CHO_levels):
    if CHO_levels < 45:
        return "CHO levels: " + Disease.LOW.name
    elif CHO_levels > 65:
        return "CHO levels: " + Disease.HIGH.name

def diagnose_protein(protein_levels):
    if protein_levels < 10:
        return "Protein levels: " + Disease.LOW.name
    elif protein_levels > 35:
        return "Protein levels: " + Disease.HIGH.name


def diagnose(user, macros):
    '''returns a list of diagnostics given a dictionary of patient data'''
    diagnostics = []
    
    hb_a1c = User._meta.get_field('hb_a1c').value_from_object(user)
    diagnostics.append(diagnose_diabetes(hb_a1c))
    
    bmi = User._meta.get_field('bmi').value_from_object(user)
    diagnostics.append(diagnose_obesity(bmi))

    fpg = User._meta.get_field('fpg').value_from_object(user)
    diagnostics.append(diagnose_pre_diabetes(fpg))

    sysbp = User._meta.get_field('sys_bp').value_from_object(user)
    diabp = User._meta.get_field('dia_bp').value_from_object(user)
    diagnostics.append(diagnose_hypertension(sysbp, diabp))

    chol = User._meta.get_field('cholesterol').value_from_object(user)
    ldl = User._meta.get_field('ldl').value_from_object(user)
    hdl = User._meta.get_field('hdl').value_from_object(user)
    tag = User._meta.get_field('tag').value_from_object(user)
    diagnostics.append(diagnose_dyslipidemia(
        chol, ldl, hdl, tag))

    diagnostics.append(diagnose_dietary_vitA(macros.vitA))
    diagnostics.append(diagnose_dietary_vitB12(macros.vitB12))
    diagnostics.append(diagnose_dietary_vitD(macros.vitD))
    diagnostics.append(diagnose_dietary_vitE(macros.vitE))
    diagnostics.append(diagnose_dietary_vitK(macros.vitK))
    diagnostics.append(diagnose_dietary_folate(macros.folate))
    
    diagnostics.append(diagnose_fat(macros.energyFat))
    diagnostics.append(diagnose_CHO(macros.energyCHO))
    diagnostics.append(diagnose_protein(macros.energyPro))
    
    diagnostics = [d for d in diagnostics if d is not None]
    return diagnostics
    
