max_sum = 0
letter_sum = 0
winner = None

while True:
    name = input()

    if name == "STOP":
        print(f"Winner is {winner} - {letter_sum}! ")
        break

    for letter in name:
        letter_sum += ord(letter)

    if letter_sum > max_sum:
        max_sum = letter_sum
        winner = name


