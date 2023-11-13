def contains(first, second):
    for c in second:
        if first.find(c) == -1:
            return False
    return True

word = input("Write a word: ")
line = input("Write a symbols combination: ")

if contains(line, word):
    print("Yes")
else:
    print("No")



while True:
    try:
        date = input("Введіть дату народження у форматі YYYYMMDD:")
        if not date.isdigit() or len(date) != 8:
            raise ValueError()
        break
    except:
        print("Введене значення не є допустимою датою. Повторіть спробу...")

while True:
    sum = 0
    for symbol in date:
        sum += int(symbol)

    date = str(sum)

    if len(date) == 1:
        break

print(sum)


def is_in_range(val, min, max):
    if val < min or val > max:
        raise ValueError("Error: the value is not within permitted range ({0}..{1})".format(min, max))
    return val


while True:
    try:
        v = input("Input a value: ")
        mi = input("Input a min: ")
        ma = input("Input a max: ")

        if not (v.isdigit() and mi.isdigit() and ma.isdigit()):
            raise ValueError("Error: wrong input")

        print(is_in_range(v, mi, ma));
        break;
    except ValueError as verr:
        print(verr)