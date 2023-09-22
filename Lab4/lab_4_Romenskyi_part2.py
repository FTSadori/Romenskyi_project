# Task7
import time

for i in range(5):
    print(i + 1, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

# Task8
while True:
    if input('Input a word ->') == "chupacabra":
        break

print('You\'ve successfully left the loop.')

# Task9
word = input('Input a word ->').upper()

for ch in word:
    if ch in 'AEIOU':
        continue
    print(ch)

# Task10
word_without_vowels = ""

word = input('Input a word ->').upper()

for ch in word:
    if ch in 'AEIOU':
        continue
    word_without_vowels += ch

print(word_without_vowels)

# Task11
n = int(input('Enter a number of bricks ->'))

i = 0

while n > i + 1:
    i += 1
    n -= i

print(i)

# Task12
steps = 0

c0 = int(input('Enter c0 ->'))

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = c0 * 3 + 1
    print(c0)
    steps += 1

print('Steps = ' + str(steps))