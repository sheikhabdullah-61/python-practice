import random
secret = random.randint(1, 50)
chances = 5
print("Maine 1 se 50 ke beesh ek number socha hai. ")
while chances > 0:
  guess = int(input(f"Tumhara gess ({chances} chances baaki): "))
  if guess == secret:
    print("Sahi! tum jeet gaye!")
    break
  elif guess < secret:
    print("Thoda bada socho")
  else :
    print("Thoda chhota socho")
  chances = chances - 1
  if chances == 0:
    print(f"chances khatam. Number tha {secret}")
    