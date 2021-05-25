# Calculate BMI
# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

def bmi(weight, height):
    bmi = weight/(height**2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"


print(bmi(50, 1.80))


# alternative
# place the conditions inside the index of the array
def bmi2(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
