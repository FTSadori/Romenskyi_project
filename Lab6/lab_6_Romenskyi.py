# task1
def is_year_leap(year):
    return (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0)

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# task2
def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days[1] = 29
    if month < 1 or month > 12:
        return None
    return days[month - 1]

test_years = [1900, 2000, 2016, 1987, 1000]
test_months = [2, 2, 1, 11, 24]
test_results = [28, 29, 31, 30, None]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
    	print("OK")
    else:
    	print("Failed")

# task3
def day_of_year(year, month, day):
    sum = day;
    for i in range(1, month):
        sum += days_in_month(year, i)
    return sum

print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(2000, 2, 28))

# task4
def is_prime(num):
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# task5
def liters_100km_to_miles_gallon(liters):
    km_l = 100.0 / liters
    return km_l / 1.609344 * 3.785411784


def miles_gallon_to_liters_100km(miles):
    gal_100m = 100.0 / miles
    return gal_100m / 1.609344 * 3.785411784


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# task6
def is_a_triangle(a, b, c):
    l = [a, b, c]
    l.sort()
    return l[0] + l[1] > l[2]

print(is_a_triangle(3, 5, 3))

# task7
def is_a_right_triangle(a, b, c):
    l = [a, b, c]
    l.sort()
    return l[0] ** 2 + l[1] ** 2 == l[2] ** 2

print(is_a_right_triangle(3, 5, 4))