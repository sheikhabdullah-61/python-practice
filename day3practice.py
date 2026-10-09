# for i in range(1,101):
#   if i % 2 == 0:
#     print(i)
# for i in range(2, 101, 2):
#   print(i)
# n = int(input("Number: "))
# result = 1
# for i in range(1, 20):
#   result = result * 1
# print("f{n}! = {result}") 
shai = "python"
chances = 3
while chances > 0:
  guess = input("Password: ") 
  if guess == "python1":
     print("Access granted")
     break
  chances = chances - 1
  print(f"Galat! {chances} chances bakki")
if chances == 0:
  print("Locked")
  