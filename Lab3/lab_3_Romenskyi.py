import math


# task 1 #
def gauss(x, mu, sig):
    exp = math.exp(-((x - mu) ** 2) / (2 * sig ** 2))
    frac = 1 / (sig * math.sqrt(2 * math.pi))
    return frac * exp


print(gauss(0.00, mu=5, sig=15))

# task 2 #

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=', ')

total_apple = john + mary + adam
print("Загальна кількість яблук:", total_apple)

# task 3 #

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# task 4 #

X = [0.0, 1.0, -1.0]

Y = [(3 * (x ** 3) - 2 * (x ** 2) + (3 ** x) - 1) for x in X]

# При x = 0 y = 3 * 0 - 2 * 0 + 1 - 1 = 0
# При x = 1 y = 3 * 1 - 2 * 1 + 3 - 1 = 3
# При x = 0 y = 3 * -1 - 2 + 1/3 - 1 = -6 + 1/3 = -5 2/3

print("y =", Y)

# task 5 #

# this program computes the number of seconds in a given number of hours

hours = 2
seconds_in_hour = 3600

print("Hours: ", hours)
print("Seconds in Hours: ", hours * seconds_in_hour)

# task 6 #

a = float(input("Input a float value for variable a: "))
b = float(input("Input a float value for variable b: "))

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

print("\nThat's all, folks!")

# task 7 #

x = float(input("Enter value for x: "))

def frac(x, times = 4):
    if x == 0: raise Exception("Hey, stop it")
    f = 1 / x
    for i in range(times):
        f = 1 / (x + f)
    return f

# при х = 1 буде 0.625
y = frac(x)
print("y =", y)

# task 8 #

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

extra_hours = (mins + dura) // 60
mins = (mins + dura) % 60
hour = (hour + extra_hours) % 24

print(str(hour) + ":" + str(mins))