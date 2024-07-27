word = input()

result = 0

for latter in word:
    if latter == "a":
        result += 1
    elif latter == "e":
        result += 2
    elif latter == "i":
        result += 3
    elif latter == "o":
        result += 4
    elif latter == "u":
        result += 5

print(result)