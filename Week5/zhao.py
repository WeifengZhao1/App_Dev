"""
Weifeng Zhao
Tuesday, Aug 29
"""

# FUNCTION
print('\n --- User defined functions --- \n')
def my_function():
    print('my_functon code')

my_function()
my_function()
my_function()

print('\n --- function with parameters --- \n')
def my_name(fname):
    print(f'Welcome to Python coding {fname}')

name = input('Enter a name: ')
my_name(name)

"""
#DICTIONARY
print('Dictionary')
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(f'\n {car}')
print(f"Model = {car['model']}")
print('\n --- loop each key in the dictionary --- \n')
for k in car:
    print(f'key = {k}')
    print(f'value = {car[k]}')

lenCar = len(car)
print(f'The size of the dictionary is {lenCar}')
"""


"""
# LOOPS
n = 0
while n < 6:
    print(f'n = {n}')
    n += 1
print('\nUse while loop to check if a number is between 0 and 10 \n')
num = int(input('Enter a number: '))
while (num < 0 or num > 10):
    num = int(input('Enter a  valid number number (0-10) '))
else:
    print(f'Number {num} is correct!')

print('Use while loop as a validation program')

while True:
    conf = input('Do you want to continue? (y/n)')
    if(conf == 'n' or conf=='N'):
        break

print('Thank you for visiting!')
"""

"""
for i in range(11):
    if i == 5:
        print(f'Now counting 5. Loop will break')
        break
    print(i)

for i in range(11):
    if i == 5:
        print(f'Now counting 5. Loop will break')
        continue
    print(i)

print('for-else loop')
for n in range(6):
    print(f'n = {n}')
else:
    print('Finish')

"""

"""
print('\nloop through a list')
colors = ['orange','olive','blue','pink','yellow']
for c in colors:
    print(c)

print('stepup counter with increment of 3')
for counter in range(-10,10,3):
    print(f'Counting now = {counter}')

print('Stepdown counter')
for x in range(5,-2,-1):
    print(f'Counting now = {x}')

# check if a user is an adult
age = int(input("Enter an age: "))
print(f'Age: {age}')


if age >= 21:
    print(f'{age} is an adult age!')
else:
    print(f'{age} is under age')

# logical operators and, or, not
gender = input('Enter a gender: ')
kidAge = int(input('Enter an age: '))

if((gender=='m' or gender == 'b') and kidAge > 2 and kidAge < 12):
    print(f'For a boy of {kidAge} should eats more broccoli')
elif((gender=='m' or gender == 'b') and kidAge>=12 and kidAge<=18):
    print(f'For a teen of {kidAge} should practice some sports!')
elif((gender=='f' or gender == 'g') and kidAge > 2 and kidAge<12):
    print(f'For a girl of {kidAge} should eats more fruits')
elif((gender=='f' or gender == 'g') and kidAge>=12 and kidAge<=18):
    print(f'For a teen of {kidAge} should learn to play an instrument!')
else:
    print(f'No comments for {kidAge}')

"""