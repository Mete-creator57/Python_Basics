
name = input('Enter your name: ')

while name == '':
    print('You did not entered anything...')
    print('Enter your name: ')

print('Hello, ' + name.title() + '.')


# Note: .isdigit() method returns False if value is negative e.g.(-5)
while True:
    num = input('Enter a number between 1 and 10 (q to quit): ').strip()
    if num.lower() == 'q':
        break
    
    try:
        num = int(num)
    except ValueError:
        print('Invalid integer!')
        continue
    
    if num < 1 or num > 10:
        print('This value is not in the specified range!')
        continue
    
    print(f"Your number: {num}")