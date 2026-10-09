# n = int(input("Number: "))
# if n % 2 == 0:
#   print(n, "even hai")
# else:
#   print(n, " odd hai")
# marks = int(input("Marks(0-100): "))
# if marks >= 90:
#   print("Grade A")
# elif marks >= 75:
#   print("Grade B")
# elif marks >= 50:
#   print("Grade C")
# else:
#   print ("Fail")
a = float(input("Pahla Number: "))
b = float(input("Doosra Number: "))
op = input("Opration( +, -, *, /): ")
if op == "+":
  print(f"Jawab = {a + b}")
elif op == "-":
  print(f"Jawab = {a - b}")
elif op == "*":
  print(f"Jawab = {a * b}")
elif op == "/":
  print(f"Jawab = {a / b}")
else:
  print("Galat opration")