# s = "python"
# print(s[0])
# print(s[5])
# print(s[-1])
# print(s[-2])
# print(len(s))
# print(s[0:3])
# print(s[2:])
# print(s[:4])
# print(s[::-1])
# naam = " SHEIKH ABDULLA "
# print(naam.strip())
# print(naam.upper())
# print(naam.lower())
# print(naam.title())
# print(naam.replace("Abdulla", "Ali"))
# print("banana".count("a"))
# print("banana".find("n"))
# print("py" in "python")
# line = "apple,banana,mango"
# phal = line.split(",")
# print("-".join(phal))
# s = "python"
# s[0] = "P"
# s = "P" + s[1:]
# phal = ["apple", "banana", "mango"]
# print(phal[0])
# print(phal[-1])
# print(phal[0:2])
phal = ["apple", "banana", "mango"]
phal.append("kela")
print(phal)
phal.insert(1, "orange")
print(phal)
phal.remove("banana")
print(phal)
x = phal.pop()
print(x, phal)
phal.pop(0)
print(phal)
phal[0] = "seb"
print(phal)
nums = [5, 2, 9, 1]
print(sum(nums))
print(max(nums))
print(min(nums))
print(sorted(nums))
nums.sort()
nums.reverse()
for p in phal:
  print(p)
for i, p in enumerate(phal, 1):
 print(i, p)