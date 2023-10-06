# task 1
n = int(input('Input n -> '))

tup = 1,2,5,23,2,1,6,4,2,3,6

result = []

for num in tup:
    if num < n:
        result.append(num)

print(result)

# task 2
a = input('Print first string -> ')
b = input('Print second string -> ')
c = input('Print third string -> ')

tup = a, b, c

print(', '.join(tup))

# task 3
dict = { "Name1" : ("author1", 1997, 350),
        "Name2" : ("author2", 1230, 90),
        "Name3" : ("author3", 2000, 150)}

name = input("Input book name -> ")

if name in dict:
    print(name)
    print("Author:\t", dict[name][0])
    print("Year:\t", dict[name][1])
    print("Pages:\t", dict[name][2])
else:
    print("Sorry, we don't have that book :(")

# task 4
students = { "StudSurname1" : ("StudName1", "StudPatr1", 19, "КН-21-1"),
            "StudSurname2" : ("StudName2", "StudPatr2", 21, "КН-21-1"),
            "StudSurname3" : ("StudName3", "StudPatr3", 20, "КІ-21-1"),
            "StudSurname4" : ("StudName4", "StudPatr4", 22, "КІ-21-1"),
           }

surname = input("Input student's surname -> ")

if surname in students:
    stud = students[surname]
    print(surname, stud[0], stud[1])
    print("Age:", stud[2])
    print(stud[3])
else:
    print("Sorry, we know about this student :(")

# task 5
contacts = { "Dude1" : ["+380000000000", "+380000000001"],
            "Dude2" : ["+380000000100", "+380000000101", "+380000000102"],
            "Dude3" : ["+380000000200", "+380000000201"],
            "Dude4" : ["+380000000300", "+380000000301", "+380000000302", "+380000000303"]}

def add_num(dude_name, number):
    global contacts
    if dude_name in contacts:
        if number not in contacts[dude_name]:
            contacts[dude_name].append(number)
    else:
        contacts[dude_name] = [number]

def show_contacts():
    for dude, info in contacts.items():
        print(dude + ":")
        for num in info:
            print("\t" + num)

add_num("Dude5", "+380000000042")
add_num("Dude1", "+380000000012")

show_contacts()
