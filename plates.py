plates = 5

while plates > 0:
    doorbell = bool(input())
    if doorbell:
        break
    print("washing the dishes")
    plates -= 1