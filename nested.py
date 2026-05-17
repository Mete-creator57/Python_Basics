# Nested Loops (outer, inner)

for x in range(9):
    if x == 8:
        print('The last one!', end=' -> ')
        print('x' + 'y' * 8 )
        break
    else:
        print('x',end='')
    
    for y in range(9):
        if y == 8:
            print('y',end='')
            # going on to the next line
            print()
        else:
            print('y',end='')

# rows and columns
rows = int(input('Enter the row number: '))
columns = int(input('Enter the column number: '))

for row in range(rows):
    print('Printing a new row...')
    print(f'{row + 1}:',end=' ')
    for column in range(columns):
        print('*',end='') # leaving no space in between
    
    print()
    if row == rows - 1:
        print('That was a final row!')


while not x == 9:
    for x in range(10):
        print(x)
    

        
        