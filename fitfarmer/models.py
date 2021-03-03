from django.db import models

class FoodGroupStats:
  def __init__(self, gender, weight, name, grain=0, fruit=0, veg=0, dairy=0, wine=0,
               seafood=0, poultry=0, legumes=0, starch=0,
               egg=0, sweet=0, meat=0, oil=0):
    grain = models.IntegerField()
    fruit
    veg
    dairy
    wine
    seafood
    poultry
    legumes
    starch
    egg
    sweet
    meat
    oil
    gender
    weight
    name

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

class UserFoodStats:
  def __init__(self, username, grain=0, fruit=0, veg=0, dairy=0, wine=0,
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
    self.username = username

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
# Create your models here.
