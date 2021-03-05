import datetime
from django.test import TestCase
from .models import User, Food
from .medscore import UserMacros
from .macros import getFoodMacros
from .diagnose import diagnose


def test_macro_diagnosis():
    user = User.objects.filter(id=1)
    foods = Food.objects.filter(user_id=1).filter(consume_date__date=datetime.date(2021,3,5))
    macros = getFoodMacros(foods)
    diagnoses = diagnose(user[0], macros)
    
    print(macros)
    print(user)
    print(diagnoses)


test_macro_diagnosis()

