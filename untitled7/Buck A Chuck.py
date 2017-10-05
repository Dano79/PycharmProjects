name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to club Deez Nuts, {0}".format(name))
else:
    print("You are not old enough")