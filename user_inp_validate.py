
# Validating user input
# username mustn't contain any digits
# username mustn't have more than 12 characters
# username mustn't have any spaces

username = input('Enter your username: ')

if len(username) > 12:
    print('Your username is longer than 12 characters. Try again.')

elif not username.find(' ') == -1:
    print('Your username contains spaces. Try again.')

# checks whether username contains invalid elements including numbers, 
# symbols, etc.
elif not username.isalpha():
    print('Your username contains invalid elements. Try again.')

else:
    print(f'Access granted! Welcome {username.title()}')

# using any() function to check if at least one element is True
# 1. Has to contain digits
# 2. Has to contain alphabeticall characters
# 3. Can't contain more than 6 elements
# 4. Has to contain dashes ans spaces
car_num = input('Enter your car number: ').upper().strip()

if not any(ch.isdigit() for ch in car_num):
    print(f'{car_num} is an invalid car number')
    print('Your car number has to contain digits. Try again.')

elif not any(ch.isalpha() for ch in car_num):
    print(f'{car_num} is an invalid car number')
    print('Your car number has to contain characters. Try again.')

elif car_num.find(' ') == -1 or "-" not in car_num:
    print(f'{car_num} is an invalid car number')
    print('Your car number has to contain spaces or dashes. Try again')

elif len(car_num) > 6:
    print(f'{car_num} is an invalid car number')
    print('This was too long! Try again.')

else:

    print(car_num + ' is a valid car number')