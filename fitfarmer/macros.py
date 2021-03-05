import pandas as pd
from .medscore import UserMacros
from .models import Food
from .views import FOOD_BEV, NUTR

CAL_FROM_G_PRO = 4
CAL_FROM_G_CHO = 4
CAL_FROM_G_FAT = 9


def getFoodMacros(foods):
    ## Get the foods that the user ate for the day
    serve_field = Food._meta.get_field('servings')
    name_field = Food._meta.get_field('food_text')
    macros = UserMacros()

    for food in foods:
        servings = serve_field.value_from_object(food)
        food_name = name_field.value_from_object(food)
        
        db_food = FOOD_BEV.loc[FOOD_BEV['main_food_description'] == food_name]
        food_code = db_food['food_code'].iloc[0]
        food_item = NUTR.loc[NUTR['food_code'] == food_code]

        macros.calories += food_item['energy_kcal'] * float(food.servings)

        macros.vitD += food_item['vitamin_d_d2_+_d3_mcg'] * float(food.servings)
        macros.vitE += food_item['vitamin_e_alpha-tocopherol_mg'] * float(food.servings)
        macros.vitA += food_item['vitamin_a,_rae_mcg_rae'] * float(food.servings)
        macros.vitK += food_item['vitamin_k_phylloquinone_mcg'] * float(food.servings)
        macros.vitB12 += food_item['vitamin_b-12_mcg'] * float(food.servings)
        macros.folate += food_item['folate,_total_mcg'] * float(food.servings)

        # convert grams of nutrient consumed to calories obtained from that nutrient
        macros.energyCHO += food_item['carbohydrate_g'] * CAL_FROM_G_CHO * float(food.servings)
        macros.energyPro += food_item['protein_g'] * CAL_FROM_G_PRO * float(food.servings)
        macros.energyFat += food_item['total_fat_g'] * CAL_FROM_G_FAT * float(food.servings)
        
    macros.energyCHO = (macros.energyCHO / macros.calories) * 100
    macros.energyCHO = (macros.energyPro / macros.calories) * 100
    macros.energyCHO = (macros.energyFat / macros.calories) * 100

    return macros

