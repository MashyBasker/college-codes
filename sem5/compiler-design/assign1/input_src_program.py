# NAME: SAYAN KARMAKAR
# REG. NO.: 735

import random

# Program to generate a list of random numbers then sorting it...
print('\nProgram to generate a list of random numbers then sorting it...\n')

# Taking inputs:
number = int(input('Enter no. of random variables you need: '))
low = int(input('Enter the low range: '))
high = int(input('Enter the high range: '))
random_number_list = []

while (high - low + 1) < number:
    print('\n<high - low + 1> must be equal to total numbers')
    print('Enter again: ')
    number = int(input('Enter no. of random variables you need: '))
    low = int(input('Enter the low range: '))
    high = int(input('Enter the high range: '))

for i in range(number):
    random_number = random.randint(low, high)
    while random_number in random_number_list:
        random_number = random.randint(low, high)
    random_number_list.append(random_number)

# Display results:
print(f'\nGenerated list of random numbers is: {random_number_list}\n')
random_number_list.sort()
print(f'\nGenerated list of random numbers sorted is: {random_number_list}\n')