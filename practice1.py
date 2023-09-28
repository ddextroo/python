Red_Horse = 1000
San_Mig_Light = 1000
San_Mig_Pilsen = 1000
Colt_45 = 1000
Gold_Eagle = 1000
Heineken = 1000
Tiger_Cystan = 1000

print("Menu : \n ID 1 - Red Horse\n ID 2 - San Mig Light\n ID 3 - San Mig Pilsen\n ID 4 - Colt 45\n ID 5 - Gold Eagle\n"
      " ID 6 - Heineken\n ID 7 - Tiger Crystan")
print("")

while True:
    print("1. Weekly Sales\n2. Weekly Purchase\n3. Inventory\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        id_choice = input("Enter Brand ID: ")
        quantity = int(input("Enter quantity: "))
        if id_choice == '1':
            Red_Horse -= quantity
        elif id_choice == '2':
            San_Mig_Light -= quantity
        elif id_choice == '3':
            San_Mig_Pilsen -= quantity
        elif id_choice == '4':
            Colt_45 -= quantity
        elif id_choice == '5':
            Gold_Eagle -= quantity
        elif id_choice == '6':
            Heineken -= quantity
        elif id_choice == '7':
            Tiger_Cystan -= quantity
        else:
            print("Invalid ID")

    elif choice == '2':
        id_choice = input("Enter Brand ID: ")
        quantity = int(input("Enter quantity: "))
        if id_choice == '1':
            Red_Horse += quantity
        elif id_choice == '2':
            San_Mig_Light += quantity
        elif id_choice == '3':
            San_Mig_Pilsen -= quantity
        elif id_choice == '4':
            Colt_45 += quantity
        elif id_choice == '5':
            Gold_Eagle += quantity
        elif id_choice == '6':
            Heineken += quantity
        elif id_choice == '7':
            Tiger_Cystan += quantity
        else:
            print("Invalid ID")

    elif choice == '3':
        print(f'Red Horse - {Red_Horse}')
        print(f'San_Mig_Light - {San_Mig_Light}')
        print(f'San_Mig_Pilsen - {San_Mig_Pilsen}')
        print(f'Colt_45 - {Colt_45}')
        print(f'Gold_Eagle - {Gold_Eagle}')
        print(f'Heineken - {Heineken}')
        print(f'Tiger_Cystan- {Tiger_Cystan}')

    elif choice == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice")













