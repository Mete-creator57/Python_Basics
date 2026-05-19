# 2D collections (tuples, lists, sets)
# 2D Tuple
num_pad = (
(1, 2, 3), 
(4, 5, 6), 
(7, 8, 9), 
('*', 0, '#'))

for row in num_pad:
    for num in row:
        print(num, end=' ')
    print()

# 2D List
hardware = ['motherboard', 'cpu', 'gpu', 'ram', 'ssd', 'cooling fan', 'psu']
software = ['photoshop', 'premier pro', 'youtube']
os = 'windows'
pc = [hardware, software, os]

print(pc)

apps = [{'youtube','youtube'}]
print(apps)
print(help(apps))
print(dir(apps))

# using divmod() func 
# // and % at a time
# returns a tuple (result of an int division, remainder)
print(divmod(10, 2))