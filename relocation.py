width = int(input())
length = int(input())
height = int(input())

all_space = width * length * height
boxes = None

while all_space > 0:
    boxes = input()

    if boxes == "Done":
        print(f"{all_space} Cubic meters left.")
        break

    all_space -= int(boxes)

if not boxes == "Done":
    print(f"No more free space! You need {abs(all_space)} Cubic meters more.")
