# create phone number
# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(arr):
    string = ''.join(map(str, arr))
    return '(' + string[0] + string[1] + string[2] + ') ' + string[3] + string[4] + string[5]+'-'+string[6]+string[7]+string[8]+string[9]


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# alternative


def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
