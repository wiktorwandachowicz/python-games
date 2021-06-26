age = 43
print("Your age is " + str(age) + ", so...")

if age == 11:
	print("You are my age!")
elif age < 0:
	print("You are not alive.")
elif age < 1:
	print("You are BARELY alive!")
elif age == 43:
	print("You are as old as my mother!")
elif age > 43 and age < 45:
	print("You are older than my mother and younger than my dad!")
elif age == 45:
	print("You are as old as my dad!")
elif age > 45:
	print("You are older than my dad!")
else:
	print("You are NOT my age!")
