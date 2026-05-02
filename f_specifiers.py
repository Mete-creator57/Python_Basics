
# Format Specifiers (.1f, <1, >1, ^, +, ,, ) 
# {value:flags}

price_1 = 3444.33
price_2 = 332223
price_3 = -123422.348392

# '2' in .2f determines how many decimal places there will be displayed
print(f'Price 1: {price_1:.2f} USD')
print(f'Price 2: {price_2:.2f} USD')
print(f'Price 3: {price_3:.2f} USD')

# determines how many space there will be before a value
print(f'Price 1 again: {price_1:10} USD')

# 0 padded (starting with 0)
print(f'\nPrice 2 again: {price_2:010} USD')

# using left angle bracket
print(f'Price 3: USD {price_3:>20.2f}')

ps_price_slim = 5000.03726
print(f'Playstation Slim is priced at {ps_price_slim:+,.1f}')


ps_digital = 453932.743
# alignment in python (6 spaces before an actual value)
print(f"Playstation Digital would cost around {' ' * 6}{ps_digital:^.2f}")




