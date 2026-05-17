# Shopping Cart Programm

foods = []
prices = []
discount = 0


def main() -> None:
    print('Welcome to the main programm! ')
    while True:
        print('Enter q to quit...')
        food = input('Enter a food to add to your cart: ')
        if food.upper() == 'Q':
            print('Quiting...')
            return
        else:
            foods.extend(food)
    
        while True:
            price = input(f'Enter the price of a {food}: ')
            if price.upper() == 'Q':
                print('Quiting...')
                return
            try:
                price = int(price)
            except Exception as err:
                print(f'Error encountered: {err}')
                continue
            else:
                prices.append(price)
                break

main()

print('--- Your Cart ---')
print('Foods:')
for f in foods:
    print(f)

print('Prices: ')
for i, p in enumerate(prices):
    print(str(i) + ': ' + str(p))
 

            




    

