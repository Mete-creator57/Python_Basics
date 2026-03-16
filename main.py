
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

decimal_num = int(decimal_num)
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
length = float(input("Enter the length: "))  # converting what user types directly to int
width = float(input("Enter the width: "))
result = length * width 
print(f"The area is: {result} cm") 

#Exercise 2: Shopping Cart
item = input("What item would you like to purchase?: ")
quantity = int(input(f"How many {item}s would you like to purchase?: "))
price = float(input(f"What's the price of 1 {item}?: "))

summary = price * quantity

if quantity <= 0:
    print(f"You haven't bought any {item}s")
    print(f"The total is: {summary}$")

if quantity > 1: 
    print(f"You have bought {quantity} {item}s")
    print(f"The total is: {summary}$")

if quantity == 1:
    print(f"You have bought {quantity} {item}")
    print(f"The total is: {summary}$")

# madlibs game
print("You're going to fill in the missing words in a story. Become a professional story-writer!")

verb = input("Enter a verb (with ing): ") # assigning what user types (user's input) to a variable named "verb" so the value is stored in it
noun = input("Enter a noun: ")
money = float(input("Enter an amount of money: "))
print(f"Yesterday I was {verb}  in the park when I suddenly realized that {noun} wasn't in my pocket")
print(f"I had to make a plan to get out of such an unpleasant situation, so I decided to pay {money}$ to all of my family members")

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



print(boxes)
