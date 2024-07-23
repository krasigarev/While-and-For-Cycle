width = int(input())
length = int(input())
height = int(input())

all_space = width * length * height

while all_space > 0:
    boxes = int(input())
    all_space -= boxes
