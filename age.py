age = 11

def checkage(age):
    if age == 11:
            return ("you are my age!")
    elif age < 0:
            return ("you are not alive.")
    elif age < 1:
            return ("you are BARELY alive!")
    elif age == 43:
            return ("you are as old as my mother!")
    elif age > 43 and age < 45:
            return ("you are older than my mother and younger than my dad!")
    elif age == 45:
            return ("you are as old as my dad!")
    elif age > 45:
            return ("you are older than my dad!")
    else:
            return ("you are NOT my age!")

x = checkage(age)

howifeelabouturage = "Your age is " + str(age) + ", so " + x

print(howifeelabouturage)
