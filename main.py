
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
                        # and converted it to a bool, the false value would be False
                        # used for checking whether users type something or not. and if not, we could do something with it
                        # e.g. ask users to type again since it's now valid
print(surname)


