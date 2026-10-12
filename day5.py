contacts= {}
while True:
  print("\n1. add 2. search 3. Sab dikhao 4. Exit")
  choice = input("Choice: ")
  if choice == "1":
    naam = input("Naam: ")
    number = input("Number: ")
    contacts[naams] = number
  elif choice == "2":
    naam = input("Kisko dhundna hai? ")
    print(contacts.get(naam, "Nahi mila"))
  elif choice == "3":
    for naam, number in contacts.items():
      print(naam, "->", number)
  elif choice == "4":
    break
  else:
    print("Galat choice")