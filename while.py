number = int(input())

while not (number >= 1 and number <= 100):
    print("invalid number")
    number = int(input())

print(f"The number is: {number}")
