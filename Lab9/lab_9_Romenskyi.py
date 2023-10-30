shift = 0

# Перевірка вхідних даних
while True:
    try:
        shift = int(input("Print value from 1 to 25 -> "))
        if shift < 1 or shift > 25:
            continue
        break
    except Exception:
        continue

line = input("Print line to encode -> ")
encoded = ''

# Кодування
for char in line:
    code = ord(char)
    if char.isupper():
        code += shift
        if code > ord('Z'):
            code -= 26
    elif char.islower():
        code += shift
        if code > ord('z'):
            code -= 26
    encoded += chr(code);

print(encoded)

decoded = ''

# Декодування
for char in encoded:
    code = ord(char)
    if char.isupper():
        code -= shift
        if code < ord('A'):
            code += 26
    elif char.islower():
        code -= shift
        if code < ord('a'):
            code += 26
    decoded += chr(code);

print(decoded)