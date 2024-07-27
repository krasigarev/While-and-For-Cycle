age = int(input())
price_washing = float(input())
price_toys = int(input())

count_toys = 0
amount = 10
money = 0

for year in range(1, age+1):
    if not year % 2 == 0:
        count_toys += 1
    else:
        money += amount - 1
        amount += 10

money += count_toys * price_toys
differance = abs(money - price_washing)

if money >= price_washing:
    print(f"Yes {differance:.2f}")
else:
    print(f"No {differance:.2f}")

