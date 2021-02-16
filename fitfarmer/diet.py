
activity_lut = {'none': 1.2,
                'light': 1.375,
                'moderate': 1.44,
                'heavy': 1.725,
                'extreme': 1.9}

# Helper Function from https://github.com/chrismcglynn/calorie-calculator/edit/master/calorie_calc.py
def get_brm(age, gender, weight, height, activity):

    if gender == 'male':
        c1 = 66
        hm = 6.2 * height
        wm = 12.7 * weight
        am = 6.76 * age
    elif gender == 'female':
        c1 = 655.1
        hm = 4.35 * height
        wm = 4.7 * weight
        am = 4.7 * age

    #BMR = 665 + (9.6 X 69) + (1.8 x 178) – (4.7 x 27)
    return activiy_lut[activity] * (c1 + hm + wm - am)
