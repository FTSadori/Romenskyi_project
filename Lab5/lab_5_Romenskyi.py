# task1
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
a = int(input('Give me a number! => '))
hat_list[2] = a

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)

# task2
arr = [3, 1, 5, 4, 6, 1, 2, 4, 2]
n = len(arr)

for i in range(n - 2):
    done = True
    for j in range(1, n - i):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            done = False
    if done:
        break

print(arr)

# task3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for num in my_list:
    if num not in new_list:
        new_list.append(num)

print("The list with unique elements only:")
print(new_list)

# task4
board = [["_" for i in range(8)] for i in range(8)]

board[0][0] = "r"
board[0][7] = "r"
board[7][0] = "R"
board[7][7] = "R"

for i in range(8):
    print(board[i])
