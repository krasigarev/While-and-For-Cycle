# s = "Geeks"
#
# for i in s:
#     print(i)
#
# for num in range(2, 10, 2):
#     print(num)
#
# list1 = ["eat", "sleep", "repeat"]
#
# for count, element in enumerate(list1):
#     print(count, element)
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)
#
# list2 = ["geeks", "for", "geeks"]
#
# for i in list2:
#     print(i)
#
# numbers = [x for x in range(11)]
# print(numbers)

print("Dictionary iteration")

d = dict()
d['xyz'] = 123
d['abc'] = 345

d1 = {
    "xyz": 123,
    "abc": 345
}

for i in d:
    print("% s % d" % (i, d[i]))

for key, value in d1.items():
    print(f"{key}: {value}")

t = ((1, 2), (3, 4), (5, 6))
for a, b in t:
    print(a, b)

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]

for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)
