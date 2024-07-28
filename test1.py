for i in range(1, 4):
    print(i)
else:
    print("No Break\n")


clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_sock = []

for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"Washing {item}")
paired_sock.append("sock")
print(f"Washing {paired_sock}")

for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")

x = [1, 2]
y = [4, 5]

for i in x:
    for j in y:
        print(i, j)

i = 0
while i < len(x):
    j = 0
    while j < len(y):
        print(x[i], y[j])
        j += 1
    i += 1

for i in range(2, 4):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print()

list_1 = ["I am", "You are"]
list_2 = ["healthy", "fine", "geek"]
list_2_size = len(list_2)

for item in list_1:
    print("start outer for loop")
    i = 0
    while i < list_2_size:
        print(item, list_2[i])
        i += 1
    print("end for the loop")

for i in range(2, 4):
    for j in range(1, 11):
        if i == j:
            break
        print(i, "*", j, "=", i * j)
    print()

for i in range(2, 4):
    for j in range(1, 11):
        if i == j:
            continue
        print(i, "*", j, "=", i * j)
    print()

list_3 = [[j for j in range(3)] for i in range(5)]
print(list_3)

r = lambda q: q * 2
s = lambda q: q * 3
x = 2
x = r(x)
x = s(x)
x = r(x)
print(x)
