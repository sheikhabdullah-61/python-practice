print = (10, 20)
print(print[0])
point[0] = 5,
x, y = (3, 4)
print(x, y)
a, b = 1, 20
a, b = b, a
nums = {1, 2, 2, 3, 3, 3}
print(nums)
nums.add(4)
nums.remove(1)
print(2 in nums)
l = [1, 2, 2, 3, 3]
print(list(set(l)))
a = [1, 2, 3]
b = [2, 3, 4]
print(a + b)
print(a + b)
print(a + b)
student = {"naam": "Abdulla", "umar": 15, "sehar": "Allahabaad"}
print(student["naam"])
print(student.get("class", "pata nahi"))
student["umar"] = 16
student["class"] = 10
del student["sehar"]
print("naam" in student)
print(len(student))
for key, value in student.items():
  print(key, "->", value)
for key in student.keys():
  print(key)
for value in student.values():
  print(value)
students = [
  {"naam": "Ali", "marks": 80},
  {"naam": "Sara", "marks": 92},
]
for s in students:
  print(s["naam"], s["marks"])