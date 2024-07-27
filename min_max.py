import sys

n = int(input())

min_number = sys.maxsize
max_number = -sys.maxsize - 1

for num in range(1, n+1):
    number = int(input())
    if number > max_number:
        max_number = number

    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
