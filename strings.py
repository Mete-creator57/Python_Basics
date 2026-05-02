# Covering String Methods
# shows all available string methods (like a guideline showing 
# all necessary and common used str methods)
str_methods = help(str)
print(str_methods)

name = input('Enter a name: ').strip()

# len() function, returns a length of characters
print(len(name))

# finding the first occurence of a letter "m"
# prints an index of the first occurence
print(name.find('e'))

# '''''''''' the last occurence of a letter
last_occur = name.rfind('e')
print(last_occur)

# Counting (using count method)
ph_num = input('Enter your phone number: ')
# counting how many 0s are there in a phone number
result = ph_num.count('0')
print(f'{result} zeros in your phone number!')

# replace() method
ph_num = ph_num.replace('+90','')
print(f'Your formatted phone number: {ph_num}')