for i in range(10):
  print("Hello", i)
for i in range(1, 9):
  print("Hello", i)
for i in range(0, 10, 2):
  print("Hello", i)
for i in range(10, 0, -2):
 print("Hello", i)
n = int(input("Kaisa table? "))
for i in range(1,11):
  print(f"{n} x {i} = {n * i}")
total = 0
for i in range(1, 101):
 total = total + i
print("Jod =", total)
for akshar in "python":
  print(akshar)
count = 1
while count <= 10:
  print(count)
  count = count + 1
print("Khatam")
password = ""
while password != ("python6101"):
  password = input("Password daal be: ")
print("Andar aao be!")
for i in range(1, 100):
  if i == 4:
    break
print(i)
for i in range(1,6):
  if i == 3:
    continue
  print(i)
while True:
  naam = input("Naam(band karne ke liye q): ")
  if naam == "q":
    break
    print("Hello", naam)
print("Bye")
for i in range(1, 6):
  print("*" * i)
n = int(input("Kitni lines? "))
for i in range(1,n + 1 ):
  print("*" * i)