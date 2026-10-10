# word = input("word: ").lower()
# if word == word [::-1]:
#   print("palindrome hai")
# else:
#   print("palindrome nahi hai")
# text = input("Text: ").lower()
# count = 0
# for ch in text:
#   count += 1
#   print("Vowels: ", count)
todo = []
while True:
  print("\n1. add 2, Dikhao 3. Hatao 4. exit")
  choice = input ("choice: ")
  if choice == "1":
    todo.append(input("Kaam: "))
  elif choice == "2":
   for i, kaam in enumerate(todo, 1):
     print(i, kaam)
  elif choice == "3":
    num = int(input("Kaun sa number hatana hai? "))
    todo.pop(num - 1)
  elif choice == "4":
    break
  else:
    print("Galat choice")