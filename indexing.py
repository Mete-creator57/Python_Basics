
# start: end: step size
ph_number = '0536-632-5643'

last_three = ph_number[-3:: 2]
print(last_three)

print(f'From the beggining to an end: {ph_number[:]}')

print(f'From the 1st to 5th element: {ph_number[0:5]}')

print(f'From the end: {ph_number[-1]}')

print(f'From the beggining to an end using a step of 2: {ph_number[::2]}')

print(ph_number[::3])
for ch in ph_number[::3]:
    print(ch)

# range() function can also accept step size as a parameters
for num in range(1, 10, 2):
    print(num)

print(f'Original: {ph_number}')
# reversing a string using a step backwards (-1 means start from an end)
ph_number = ph_number[::-1]
print(f'Reversed: {ph_number}')

# we could also reverse a string like this
ph_number = '0536-632-5643'
print(f'Original again: {ph_number}')

# reversed() function is only for strings, only returns 
# an object you can loop through. 
# list() function here is used to turn this object into a list 
# [3, 4, 6, 5....]
print(f'Reversed string: {list(reversed(ph_number))}')

# you can loop through it
for ch in reversed(ph_number):
    print(ch)

# '' is a divider between elements
print(''.join(reversed(ph_number)))

