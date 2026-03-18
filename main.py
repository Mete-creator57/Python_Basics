import math
# this is my very first python programm

# strings
email = "fakegmail@gmail.com" 
name = "Dev"

# integers
num_of_bombs = 20 
age = 67 #

print("Hello World!") # first thing in programming
print(f"Your name is: {name}")
print(f"Your current age is: {age}") # integer print
print(email) 
print(f"Bombs number: {num_of_bombs}")

# floats
price = 67.99
discount = 10.99
gpa = 87.67
print(f"Student's gpa is {gpa} which is enough for us to accept him")
print(f"The price: {price} USD and the discount: {discount} USD")

# Booleans
is_good = True

if is_good: # statement next to "if" has to be true if the goal is to execute something
    print("Nice!")
else:
    print("Sorry to hear that.")

is_cheap = False
if is_cheap:
    print("Think of buying it!")
else:
    print("That's too expensive for us to buy")

    # Typecasting str(), int(), bool(), float()

uncles = 67 # int
surname = "" # string
random_string = "25"
decimal_num = 67.67 # float
is_valid = True

print(type(uncles)) # printing class a variable belongs to (<class 'int'>)

decimal_num = int(decimal_num) # explicit conversion (data loss from float to int)
print(f"Decimal number coverted to int -> {decimal_num}")

uncles = float(uncles)
print(uncles)

uncles = str(uncles) # converting int to string
print(uncles)
uncles = uncles + "1" # adding "1" to the end of the string 67.0 ->> 67.01

print(uncles)
print(type(uncles))

random_string = int(random_string) # converting string to int
print(random_string)
print(type(random_string)) # now this variable belongs to int's class , not string anymore

random_string = random_string + 1 # becomes 26
print(random_string)

surname = bool(surname) # if we don't have any characters inside quotes in a string variable
                        # and converted it to a bool, the  value would be False
                        # used for checking whether users type something or not. and if not, we could do something with it
                        # e.g. ask users to type again since it's now valid
print(surname)

  # Input() function

# favColor = input("What's your favorite color?: ")
# age = input("What's your age?: ")
# gender = input("Type your gender: ")
# age = int(age) # typecasting (string -> int)
# rabbits_num = int(input("How many rabbits do you have?: "))



#print(f"{favColor} is a very good color!")
#print(f"You are {age} years old!")
#print(f"After 1 year you'll become {age + 1} years old!")
#print(f"You have {rabbits_num} rabbits")

#if gender == "boy":
    #print("You are male!")
#else:
   # print("You are female!")

# Exercise 1: Triangle area
# length = float(input("Enter the length: "))  # converting what user types directly to int
# width = float(input("Enter the width: "))
# result = length * width 
# print(f"The area is: {result} cm") 

#Exercise 2: Shopping Cart
# item = input("What item would you like to purchase?: ")
# quantity = int(input(f"How many {item}s would you like to purchase?: "))
# price = float(input(f"What's the price of 1 {item}?: "))

# summary = price * quantity

# if quantity <= 0:
  # print(f"You haven't bought any {item}s")
    # print(f"The total is: {summary}$")

# if quantity > 1: 
   # print(f"You have bought {quantity} {item}s")
  #  print(f"The total is: {summary}$")

# if quantity == 1:
    # print(f"You have bought {quantity} {item}")
   # print(f"The total is: {summary}$")

# madlibs game
# print("You're going to fill in the missing words in a story. Become a professional story-writer!")

# verb = input("Enter a verb (with ing): ") # assigning what user types (user's input) to a variable named "verb" so the value is stored in it
# noun = input("Enter a noun: ")
# money = float(input("Enter an amount of money: "))
# print(f"Yesterday I was {verb}  in the park when I suddenly realized that {noun} wasn't in my pocket")
# print(f"I had to make a plan to get out of such an unpleasant situation, so I decided to pay {money}$ to all of my family members")

# Arithmetic / Math

boxes = 5
boxes += 1 # or boxes = boxes + 1
boxes -= 2 # or boxes = boxes - 2 -> 6 - 2 = 4
boxes *= 3 # or boxes = boxes * 3 which is 12
boxes /= 4 # or boxes = boxes / 4 which is 12 / 4 = 3

# Exponents
boxes = boxes ** 3 # which is 3 * 3 * 3 = 27
boxes = 3 # reassigning boxes number back to 3
boxes **= 3 # augmented version

# Remainder
number = 45
number = number % 3 # no remainer
number = 66
number %= 5 # remainder is 1 (of division by 5)
# print(number)

# print(boxes)


y = 67.5
z = 47
# Round 

x = round(3.14) # rounds to the nearest integer
result = round(y)
# print(x) 

# print(result)

# Absolute Value

smth = -47
result_1 = abs(smth)
# print(result_1)

#Pow function

number_1 = pow(3, 4)
# print(number_1)

# Max and Min Values (functions)

max_num = max(1, 2, 3)
min_num = min(1,  2, 3)
# print(max_num)
# print(min_num)

# math library

# print(math.pi)
# print(math.e)
pi_rounded = round(math.pi) # rounding pi to 3
# Square Root
some_num = math.sqrt(3)

# Ceil and Floor Functions (round float numbers up or down)

any_num = math.ceil(4.7) # rounds to 5 (UP to the nearest Whole Int Number)
# print(any_num)
any_num = round(4.7) # round function (rounds to the nearest WHOLE INT number)
# print(any_num)
any_num_2 = math.floor(4.7) # rounds to 4 (DOWN to the nearest Whole Int number)
# print(any_num_2)

#print(some_num)
# print(pi_rounded) 

# EXERCISES WITH MATH (Circle circumference and area)
# radius = float(input("Enter the radius of a circle: ")) # circumference of a circle
# circumference = 2 * math.pi * radius
# area = math.pi * pow(radius, 2) #raising radius to the power of 2 (area formula = PI * radius²)
# print("The results are rounded")
# print(f"The circumference is: {round(circumference, 3)}cm²")
# print(f"The area is: {area}cm² ")

# Exercise Hypotenuse
# height = float(input("Enter the height of the triangle(side a): "))
# base = float(input("Enter the base of the triangle(side b): "))

# hypotenuse = math.sqrt(pow(height, 2) + pow(base, 2)) # raising both height and base to the power of 2 (square)

# print(f"The hypotenuse is: {round(hypotenuse, 3)}")

# IF statements
# money = float(input("Enter an amount of money you currently have(in USD): "))
# print(f"You have {round(money, 1)}$! ")

# if money >= 1000:
    # print(f"You can afford a gaming PC!")
# elif money < 0: # elif = else + if
   # print("You are out of money! You have some debt! ")
# elif money == 0:
   # print("You are poor!")
# else:
   #  print("You have to have at least 1000$ for a gaming PC")
   #  print(f"{round(money, 1)}$ is not sufficient for a gaming PC")

# some_Number = 47.5433243
# user_input = input(f"Do you want the programm round the number {some_Number} and truncate it(2 digits agter comma)?: ")

# if user_input == "":
   # print("You didn't type anything!")

# elif user_input == "no":
   # print(f"Okay then. The number remains {some_Number}")

# elif user_input == "yes":
   #  round(some_Number, 2)
   # print(some_Number)
    
# else:
   # print("What is that?")



# IF statements with booleans
# signed_in = False
# if signed_in:
   # print("You are signed in!")
   
# else:
   # print(f"You aren't signed in!")
    
# Python Calculator

# operator = input("Enter an operator (+, -, *, /): ")
# num_1 = float(input("Enter a first number: "))
# num_2 = float(input("Enter a second number: "))

# print("The result is going to be rounded")

# if operator == " ":
    # print(f"Invalid operator: {operator} . Try again.")
# elif operator == "+":
    # result = num_1 + num_2
    # print(round(result, 3))
    # result = int(result)
   #  print(f"Converted to int: {result}")
# elif operator == "-":
    # result = num_1 - num_2
    # print(round(result, 3))
    # result = int(result)
    # print(f"Converted to int: {result}")
# elif operator == "*":
   #  result = num_1 * num_2
   #  print(round(result, 3))
   #  result = int(result)
   #  print(f"Converted to int: {result}")
# elif operator == "/":
   # result = num_1 / num_2
  #  print(round(result, 3))
   # result = int(result)
   # print(f"Converted to int: {result}")
# else:
  #  print("You haven't typed anything! Try again later.")

# Python Weight Converter

# weight = float(input("Enter your weight: "))
# unit = input("K / L (K = KG, L = LBS): ")

# if unit == "K":
   # weight *= 2.205 # the same as weight = weight * 2.205
   # unit = "lbs"
   # print(f"Converting from kg to lbs...")
   # print(f"Your weight is: {round(weight)}{unit} ") #rounded result
# elif unit == "L":
    # weight /= 2.205
    # unit = "kg"
    # print(f"Converting from lbs to kg...")
    # print(f"Your weight is: {round(weight)}{unit} ") #rounded result
# else:
    # print(f"{unit} is invalid measurement type. Try again")

# Temperature Conversion
temp = float(input("Enter the temperature: "))
unit = input(f"Is {temp} in Celcius or Fahreheit? (C/F): ")

if unit == "C":  # rounding
    temp = round((9 * temp) / 5 + 32, 2) # formula to convert Celcius to Fahrenheit 
    unit = "°F"
    print(f"The temperature is {temp}{unit}")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2) # F -> C (round to 2 decimal places)
    unit = "°C"
    print(f"The temperature is {temp}{unit}")

else:
    print(f"The measurement unit: {unit} is invalid. Try again later.")