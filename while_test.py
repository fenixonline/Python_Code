list1 = []
final = False
while not final:
    cant=input("Please type an activity, type done to finish ")
    if cant != "done":
        list1.append(cant)
        print("added to the list")
    else:
        print("Here is your list: ",list1)
        final = True
