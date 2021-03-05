import datetime
from django.test import TestCase
from .models import User, Food
from .medscore import UserMacros, msdpsCalc
from .macros import getFoodMacros
from .diagnose import diagnose


def test_macro_diagnosis():
    user = User.objects.filter(id=1)
    foods = Food.objects.filter(user_id=1).filter(consume_date__date=datetime.date(2021,3,5))
    macros = getFoodMacros(foods)
    diagnoses = diagnose(user[0], macros)
    
    print(user)
    print(diagnoses)


def test_msdps():
    week = datetime.datetime.today() - datetime.timedelta(7)
    msdps_week = Food.objects.filter(user_id=1).filter(consume_date__gte=week)
    msdps_score = msdpsCalc(msdps_week)

    print(msdps_score)


test_msdps()
test_macro_diagnosis()

