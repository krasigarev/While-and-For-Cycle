n = int(input())

p1_percentage = 0
p2_percentage = 0
p3_percentage = 0
p4_percentage = 0
p5_percentage = 0

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for num in range(1, n+1):
    current_number = int(input())

    if current_number <= 200:
        count_p1 += 1
    elif 201 < current_number <= 399:
        count_p2 += 1
    elif 401 < current_number <= 599:
        count_p3 += 1
    elif 600 < current_number <= 799:
        count_p4 += 1
    else:
        count_p5 += 1


p1_percentage = (count_p1 * 100) / n
p2_percentage = (count_p2 * 100) / n
p3_percentage = (count_p3 * 100) / n
p4_percentage = (count_p4 * 100) / n
p5_percentage = (count_p5 * 100) / n

print(p1_percentage)
print(p2_percentage)
print(p3_percentage)
print(p4_percentage)
print(p5_percentage)