choice = int(input(" 1-add \n 2-edit \n 3-read \n 4-delete \n 5-exit \n what you wana enter: "))

students = []

while choice != 5:
    if choice == 1:
        addchoice = input("what you wana add: ")
        students.append(addchoice)
        choice = int(input(" 1-add \n 2-edit \n 3-read \n 4-delete \n 5-exit \n what you wana enter: "))
    elif choice == 2:
        editchoice = int(input("what you wana change: "))
        perchoice = input("what you wana change for?: ")
        students[editchoice] = perchoice
        choice = int(input(" 1-add \n 2-edit \n 3-read \n 4-delete \n 5-exit \n what you wana enter: "))
    elif choice == 3:
        print(students)
        choice = int(input(" 1-add \n 2-edit \n 3-read \n 4-delete \n 5-exit \n what you wana enter: "))
    elif choice == 4:
        print(students)
        deletechoice = int(input("what do you wana delete: "))
        students.remove(deletechoice)
        choice = int(input(" 1-add \n 2-edit \n 3-read \n 4-delete \n 5-exit \n what you wana enter: "))
    
print("bye bye!")