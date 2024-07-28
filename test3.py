a = True
b = False
c = False

if a or b and c:
    print("geeksforgeeks".upper())
else:
    print("geeksforgeeks".lower())


if not a or b:
    print(1)
elif not a or not b and c:
    print(2)
elif not a or b or not b and a:
    print(3)
else:
    print(4)

count = 1


def do_this():
    global count
    for i in (1, 2, 3):
        count += 1


do_this()
print(count)

test_tup = (5, 20, 3, 7, 6, 8)

print("The original data(tuple) is: " + str(test_tup))

K = 2

res = []
test_tup = list(sorted(test_tup))

for index, value in enumerate(test_tup):
    if index < K or index >= len(test_tup) - K:
        res.append(value)

res = tuple(res)

print("The extracted values: " + str(res))
