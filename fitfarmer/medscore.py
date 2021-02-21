import json
import os
from types import SimpleNamespace as Namespace
import sys

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

def calcScore(target, actual):
  return max(0, (target - abs(target - actual))) * (10/target)

def calcMedScore(stats):
  score = (calcScore(8, stats.grain) + calcScore(3, stats.fruit) +
           calcScore(6, stats.veg) + calcScore(2, stats.dairy) +
           calcScore(6, stats.seafood) + calcScore(4, stats.poultry) +
           calcScore(4, stats.legumes) + calcScore(3, stats.starch) +
           calcScore(3, stats.egg) + calcScore(3, stats.sweet) +
           calcScore(1, stats.meat))
  if(stats.gender == "male"):
    score += calcScore(3, stats.wine)
  else:
    score += calcScore(1.5, stats.wine)
  if(stats.oil == 0): # 0 represents exclusive use of olive oil
    score += 10
  elif(stats.oil == 1): # 1 represents use of olive oil + vegetable oils
    score += 5
  score = (score/130)*100 # standardizing score on a 0-100 scale
  score *= stats.weight # adjust score by % adherent to mediterranean food groups
  return score

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

def main():
  if len(sys.argv) > 1:
    if sys.argv[1] == "-g":
      generateProfiles()
  profiles = loadProfiles()
  for p in profiles:
    score = calcMedScore(p)
    print("{}: {}".format(p.name, score))
  return 0

if __name__ == "__main__":
  main()