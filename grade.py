name = input()
counter_grade = 1
result = 0

while counter_grade <= 12:
    score = float(input())

    if score >= 4:
        result += score
        counter_grade += 1

average_score = result / 12

print(f"{name} graduated. Average grade: {average_score:.2f}")
