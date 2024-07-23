name = input()
counter_grade = 1
result = 0
fail_counter = 0
is_not_graduated = False

while counter_grade <= 12:
    score = float(input())

    if score >= 4:
        result += score
        counter_grade += 1
    else:
        fail_counter += 1
        if fail_counter > 1:
            is_not_graduated = True
            print(f"{name} has been excluded ar {counter_grade} grade.")

if not is_not_graduated:
    average_score = result / 12
    print(f"{name} graduated. Average grade: {average_score:.2f}")
