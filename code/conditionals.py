# 1.
x = 5
y = 10
if 2 * x > 10:
    print("#1 answer: works!")
else:
    print("#1 answer: Oooo needs some work")

# 2.
x = 5
y = 10
if len("Dog") < x:
    print("#2 answer: this works!")
else:
    print("#2 answer:: Still missing out")

# 3.
age = 21
if age > 20:
    print("#3 answer: you are of drinking age!")
else:
    print("#3 answer:: Argggh! You think you can hoodwink me, matey?! You're too young to drink!")

# 4.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("#4 answer: the above statement is true")
else:
    print("#4 answer: the above statement is false")

# 5.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("#5 answer: Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("#5 answer:Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("#5 answer:Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("#5 answer:Can ride bumper cars")
else:
    print("#5 answer:Stick to lazy river")

