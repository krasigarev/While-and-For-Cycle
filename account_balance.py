payments = int(input())

bank_sum = 0
counter = 0

while counter < payments:
    current_sum = float(input())

    if current_sum < 0:
        print("Invalid operation!")
        break

    bank_sum += current_sum
    counter += 1

    print(f"Increase: {current_sum:.2f}")
print(f"Total: {bank_sum:.2f}")

