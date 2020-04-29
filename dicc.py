print("**************************")
print("Welcome to people facts")
print("**************************")

dicc = {'Jeff':'Is afraid of clowns', 'David': 'Plays the piano', 'Dany': 'Can fly an airplane'}

opt=input("Type 'S' to see the list of peoples, Type 'C' to change facts, Type 'A' to add and 'D' to delete: \n").upper()
input=input
if opt == "S":
    for x, y in dicc.items():
        print(x, '>>', y)

if opt == "C":
    key=input("type the name of the person: ")
    value=input("Type the modification: ")
    if key in dicc.keys():
        dicc[key] = value

    print("here the update: ")
    for x, y in dicc.items():
        print(x, '>>', y)

if opt == "A":
    key2=input("Type new person name: ")
    value2=input("Type the fact: ")
    if key2 not in dicc.keys():
        dicc[key2] = value2
        print("new value added: ")
        for x, y in dicc.items():
            print(x, '>>', y)
        
    else:
        print("the user exists in the dicc")

if opt == "D":
    key3=input("Type the name of the person you want yo remove from the list: ")
    if key3 in dicc.keys():
        del dicc[key3]
        print("The person was removed as requested: ")
        for x, y in dicc.items():
            print(x, '>>', y)
    else:
        print("that person is not on the list")

