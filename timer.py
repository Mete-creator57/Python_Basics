import time

first = input('Enter your first number to start counting down from: ')
while not first.isdigit():
    first = input('Enter your first number to start counting down from: ')
first = int(first)

print('Counting Down!')
for i in range(first, -1, -1):
    if i == first:
        print('Timer begins!')
    # waiting for 1 sec
    time.sleep(1)
    print(i, sep=' ')
    if i == 0:
        print('Timer is over!')
    
my_time = int(input('Enter the time in seconds: '))
for i in reversed(range(0, my_time + 1)):
    seconds = i % 60
    minutes = int(i % 3600) // 60
    hours = int(i // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    if i == 0:
        print('Time is over!')
        break
    time.sleep(1)


# using reversed function (return iterable object)
my_list = list(reversed(range(1, 4)))
print(my_list)