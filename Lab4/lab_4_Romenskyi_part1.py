# Task1
print(int(input('Input int ->')) >= 100)

# Task2
a = float(input('Input float a ->'))
b = float(input('Input float b ->'))

max = a
if b > a:
    max = b

print(str(max) + ' is the largest number!')

# Task3
plant = input('Gimme a plant!!')

if plant == 'spathiphyllum':
    print('No, I want a big Spathiphyllum!')
elif plant == 'Spathiphyllum':
    print('Yes - Spathiphyllum is the best plan ever!')
else:
    print('Spathiphyllum! Not ' + plant + '!')

# Task4
income = float(input("Enter the annual income: "))

tax = 0.0

if income < 85_528:
    tax = income * 0.18 - 556.02
else:
    tax = 14_839.02 + (income - 85_528) * 0.32

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# Task5
year = int(input('Input a year ->'))

if year < 1582:
    print('Not within the Gregorian calendar period.')
elif (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0):
    print('Leap year')
else:
    print('Common year')

# Task6
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while int(input()) != secret_number:
    print('Ha-ha! Now you\'re trapped in my loop!')

print('Congrats, muggle! Now you\'re free')