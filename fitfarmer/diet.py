
# Helper Function from https://github.com/chrismcglynn/calorie-calculator/edit/master/calorie_calc.py
def get_brm(age, gender, weight, height):

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
    bmr_result = c1 + hm + wm - am
    return(int(bmr_result))

def calculate_activity(bmr_result): 
    activity_level = input('What is your activity level (none, light, moderate, heavy, or extreme): ')

    if activity_level == 'none':
        activity_level = 1.2 * bmr_result
    elif activity_level == 'light':
        activity_level = 1.375 * bmr_result
    elif activity_level == 'moderate':
        activity_level = 1.55 * bmr_result
    elif activity_level == 'heavy':
        activity_level = 1.725 * bmr_result
    elif activity_level == 'extreme':
        activity_level = 1.9 * bmr_result

    return(int(activity_level))


def recommend_diet(age, gender, weight, height, activity="none"):
    return 
    
