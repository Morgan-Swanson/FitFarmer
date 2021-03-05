import datetime
from django.test import TestCase
from .models import User, Food
from .medscore import UserMacros
from .macros import getFoodMacros


def test_macro_diagnosis():
    foods = Food.objects.filter(consume_date__date=datetime.date(2021,3,5))
    macros = getFoodMacros(foods)
    
    print(macros)
        


test_macro_diagnosis()

