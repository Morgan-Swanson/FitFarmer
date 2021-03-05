import json
import os
from types import SimpleNamespace as Namespace
import sys
import csv
import datetime
import pandas as pd
from .models import Food
from .views import FOOD_BEV, NUTR, MSDPS


class UserFoodStats:
  def __init__(self, username, grain=0, fruit=0, veg=0, dairy=0, wine=0,
              seafood=0, poultry=0, legumes=0, starch=0,
              egg=0, sweet=0, meat=0, oil=0, none=0, total=0):
    self.grain = grain
    self.fruit = fruit
    self.veg = veg
    self.dairy = dairy
    self.wine = wine
    self.seafood = seafood
    self.poultry = poultry
    self.legumes = legumes
    self.starch = starch
    self.egg = egg
    self.sweet = sweet
    self.meat = meat
    self.oil = oil
    self.none = none
    self.total = total
    self.username = username

  def __str__(self):
    s1 = "Username: {}\n".format(self.username)
    s2 = "Whole Grain: {}, Fruits: {}, Vegetables: {}, ".format(self.grain, self.fruit, self.veg)
    s3 = "Dairy: {}, Wine: {}, Seafood: {}, Poultry: {}, ".format(self.dairy, self.wine, self.seafood, self.poultry)
    s4 = "Legumes: {}, Starches: {}, Eggs: {}, Sweets: {}, ".format(self.legumes, self.starch, self.egg, self.sweet)
    s5 = "Red Meat: {}, Oil: {}, None: {}, Total: {}".format(self.meat, self.oil, self.none, self.total)
    return s1 + s2 + s3 + s4 + s5


class UserMacros:
  def __init__(self, calories=0, energyCHO=0, energyPro=0, energyFat=0, vitD=0, vitE=0, vitA=0, vitK=0, vitB12=0, folate=0):
    self.calories = calories
    self.energyCHO = energyCHO
    self.energyPro = energyPro
    self.energyFat = energyFat
    self.vitD = vitD
    self.vitE = vitE
    self.vitA = vitA
    self.vitK = vitK
    self.vitB12 = vitB12
    self.folate = folate


def calcScore(target, actual):
  target = float(target)
  actual = float(actual)
  return max(0, (target - abs(target - actual))) * (10/target)


def updateStats(cat, amount, stats, date):
  today = datetime.datetime.today()
  if date == today:
    if cat == "grain":
      stats.grain += amount
    elif cat == "fruit":
      stats.fruit += amount
    elif cat == "veg":
      stats.veg += amount
    elif cat == "dairy":
      stats.dairy += amount
    elif cat == "wine":
      stats.wine += amount
    elif cat == "seafood":
      stats.seafood += amount
    elif cat == "poultry":
      stats.poultry += amount
    elif cat == "legumes":
      stats.legumes += amount
    elif cat == "starch":
      stats.starch += amount
    elif cat == "egg":
      stats.egg += amount
    elif cat == "sweet":
      stats.sweet += amount
    elif cat == "meat":
      stats.meat += amount
    elif cat == "oil":
      stats.oil = amount
    else:
      stats.none += amount
    stats.total += amount
  else:
    if cat == "grain":
      return stats
    elif cat == "fruit":
      return stats
    elif cat == "veg":
      return stats
    elif cat == "dairy":
      return stats
    elif cat == "wine":
      return stats
    elif cat == "seafood":
      stats.seafood += amount
    elif cat == "poultry":
      stats.poultry += amount
    elif cat == "legumes":
      stats.legumes += amount
    elif cat == "starch":
      stats.starch += amount
    elif cat == "egg":
      stats.egg += amount
    elif cat == "sweet":
      stats.sweet += amount
    elif cat == "meat":
      stats.meat += amount
    elif cat == "oil":
      stats.oil = amount
    else:
      stats.none += amount
    stats.total += amount
  return stats

def calcMedScore(stats, gender):
  score = (calcScore(8, stats.grain) + calcScore(3, stats.fruit) +
           calcScore(6, stats.veg) + calcScore(2, stats.dairy) +
           calcScore(6, stats.seafood) + calcScore(4, stats.poultry) +
           calcScore(4, stats.legumes) + calcScore(3, stats.starch) +
           calcScore(3, stats.egg) + calcScore(3, stats.sweet) +
           calcScore(1, stats.meat))
  if(gender == "male"):
    score += calcScore(3, stats.wine)
  else:
    score += calcScore(1.5, stats.wine)
  if(stats.oil == 0): # 0 represents exclusive use of olive oil
    score += 10
  elif(stats.oil == 1): # 1 represents use of olive oil + vegetable oils
    score += 5
  score = (score/130)*100 # standardizing score on a 0-100 scale
  weight = float((stats.total - stats.none)/stats.total)
  score *= weight # adjust score by % adherent to mediterranean food groups
  print(stats)
  return score


def msdpsCalc(weekly):
  serve_field = Food._meta.get_field('servings')
  name_field = Food._meta.get_field('food_text')
  date_field = Food._meta.get_field('consume_date')
  msdps_inv = {value: key for key in MSDPS for value in MSDPS[key]}
  stats = UserFoodStats("Anthony")

  for food in weekly:
    date = date_field.value_from_object(food)
    servings = serve_field.value_from_object(food)
    food_name = name_field.value_from_object(food)
    db_food = FOOD_BEV.loc[FOOD_BEV['main_food_description'] == food_name]
    category = db_food['wweia_category_description'].iloc[0]
    msdps_cat = msdps_inv[category]
    stats = updateStats(msdps_cat, servings, stats, date)

  return calcMedScore(stats, "male")


'''

class FoodGroupStats:
  def __init__(self, gender, weight, name, grain=0, fruit=0, veg=0, dairy=0, wine=0,
               seafood=0, poultry=0, legumes=0, starch=0,
               egg=0, sweet=0, meat=0, oil=0):
    self.grain = grain
    self.fruit = fruit
    self.veg = veg
    self.dairy = dairy
    self.wine = wine
    self.seafood = seafood
    self.poultry = poultry
    self.legumes = legumes
    self.starch = starch
    self.egg = egg
    self.sweet = sweet
    self.meat = meat
    self.oil = oil
    self.gender = gender
    self.weight = weight
    self.name = name

class Food:
  def __init__(self, name, category, servings):
    self.name = name
    self.category = category
    self.servings = servings

class User:
  def __init__(self, name, gender, weight):
    self.name = name
    self.gender = gender
    self.weight = weight


def getBroadCategory(group, foodGroups, msdps):
  broad = foodGroups[group]
  return msdps[broad]


def generateProfiles():
  healthy = FoodGroupStats("male", 1, "Mr. Mediterranean", 
                           8, 3, 6, 2, 3, 6, 4, 4, 3, 3, 3, 1, 0)
  healthyOut = json.dumps(healthy.__dict__)
  f1 = open("../data/foodProfiles/healthy.json", "w")
  f1.write(healthyOut)
  f1.close()

  overconsume = FoodGroupStats("male", 1, "Lotso Eding", 
                                16, 6, 12, 4, 6, 12, 8, 8, 6, 6, 6, 2, 0)
  overconsumeOut = json.dumps(overconsume.__dict__)
  f1 = open("../data/foodProfiles/overconsume.json", "w")
  f1.write(overconsumeOut)
  f1.close()

  someperson = FoodGroupStats("female", 0.65, "Some Person", 
                              11.2, 6.6, 3, 1, 1.5, 1.2, 0, 0, 0, 0, 0, 0, 1)
  somepersonOut = json.dumps(someperson.__dict__)
  f1 = open("../data/foodProfiles/someperson.json", "w")
  f1.write(somepersonOut)
  f1.close()

def processFoodGroups():
  foodGroups = {}
  msdps = {}
  with open("../data/food_bev_ontology.csv", "r") as f:
    reader = csv.reader(f, skipinitialspace=True)
    for line in reader:
      foodGroups[line[2]] = line[6]
  with open("../data/msdps_categories.json", "r") as f:
    data = f.read()
    msdps = json.loads(data)
  inverted_msdps = {value: key for key in msdps for value in msdps[key]}
  return foodGroups, inverted_msdps

def loadProfiles():
  profiles = []
  directory = "../data/foodProfiles/"
  for filename in os.listdir(directory):
    f = open(directory + filename, "r")
    data = f.read()
    f.close()
    profile = json.loads(data, object_hook=lambda d: Namespace(**d))
    profiles.append(profile)
  return profiles

def loadProfiles1():
  profiles = []
  directory = "../data/dailyFood/"
  for filename in os.listdir(directory):
    f = open(directory + filename, "r")
    data = f.read()
    f.close()
    profile = json.loads(data)
    profiles.append(profile)
  return profiles

def main():
  if len(sys.argv) > 1:
    if sys.argv[1] == "-g":
      generateProfiles()
  profiles = loadProfiles1()
  foodGroups, msdps = processFoodGroups()
  for p in profiles:
    score = calcMedScore(p, "John Doe", foodGroups, "male", msdps)
    print("{}: {}".format("John Doe", score))
  return 0

if __name__ == "__main__":
  main()

'''