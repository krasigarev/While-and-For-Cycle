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


for index in range(0, len(word)):
    if word[index] == "a":
         result += 1
    elif word[index] == "e":
         result += 2
    elif word[index] == "i":
         result += 3
    elif word[index] == "o":
         result += 4
    elif word[index] == "u":
         result += 5


print(result)