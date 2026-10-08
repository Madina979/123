# 1. Переменные и ввод/вывод
#1
from shlex import split

name = "Madina"
age = 15
print(f"{name}, Через 10 лет вам будет {age + 10}")

#2
numbers = [ 23, 34, 45]
print(sum(numbers))

#3
seconds = 45678
hour = seconds // 3600
minute = (seconds % 3600) // 60
s = seconds % 60
print(f"{hour} ч. {minute} min. {s} sec.")

#4
a = 6
b = 7
S = a * b
print(S)

#5
num1 = 23
num2 = 34
num3 = 45
num4 = 56
num5 = 67

average = (num1 + num2 + num3 + num4 + num5) / 5
print(f"Среднее арифметическое: {average}")

# 2. Условные операторы
#6
number = -4
if number < 0:
    print("отрицательное")
elif number > 0:
    print("положительное")
else :
    print("ноль")

#7
num = 35
if num % 2 == 0 :
    print("чётное")
else: print("нечётное")

#8
a = 46
b = 45
if a > b:
    print(a)
else: print(b)

#9
a = 12
b = 34
c = 23
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

#10
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Високосный")
else:
    print("Обычный")

#11
def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a :
        return "Такой треугольник СУЩЕСТВУЕТ."
    else:
        return "Такой треугольник НЕ СУЩЕСТВУЕТ."

print(triangle(3,4,5))

#12
def triangle_type(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        return "Это не треугольник!"

    if a == b == c:
        return "Равносторонний треугольник"
    elif a == b or a == c or b == c :
        return "Равнобедренный треугольник"
    else:
        return "Разносторонний треугольник"

print(triangle_type(5,5,5))

#13
def calc_disc(amount):
    if amount < 100_000:
        disc_percent = 0
    elif 100_000 <= amount < 500_000:
        disc_percent = 5
    elif 500_000 <= amount < 1_000_000:
        disc_percent = 10
    else:
        disc_percent = 15

    discount_amount = amount * disc_percent / 100
    final_amount = amount - discount_amount

    return f"Скидка: {disc_percent}%. К оплате: {final_amount} сум"

print(calc_disc(600_000))

#14
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    else:
        return "Неверная дата"

print(get_zodiac_sign(15, 5))

#15
def simp_calc():
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Деление на ноль невозможно!"
        result = num1 / num2
    else:
        return "Введен неверный оператор!"

    return f"Результат: {result}"

print(simp_calc())

# 3. Циклы
#16
N = 7
for i in range(1, N + 1):
    print(i)

#17
N = 8
for i in range(N, 0, -1):
    print(i)

#18
N = 12
total = 0
for i in range(1, N + 1):
    total = total + i
print(total)

#19
N = 13
total = 1
for i in range(1, N + 1):
    total = total * i
print(total)

#20
N = 5
for i in range(1, 11):
    print(f"{N} * {i} = {N*i}")

#21
N = 10
total = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        total = total + i
print(total)

#22
N = 657463287
count = 0
while N > 0:
    N = N // 10
    count = count + 1
print(count)

#23
N = 3475
total = 0
while N > 0:
    digit = N % 10
    total = total + digit
    N = N // 10
print(total)

#24
N = 87654321
reverse = 0
while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N = N // 10
print(reverse)

#25
N = 12321
org = N
reverse = 0
while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N = N // 10
if org == reverse:
    print("Палиндром")
else:
    print("Не палиндром")

# 4. Вложенные циклы
#26
N = 5
for i in range(N):
    for j in range(N):
        print("*", end="")
    print()

#27
N = 5
for i in range(N):
    for j in range( i + 1):
        print("*", end="")
    print()

#28
N = 5
for i in range(N):
    for j in range(N - i - 1):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print("*", end="")
    print()

#29
N = 5
for i in range(N):
    for j in range(N):
        if (i + j ) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#30
N = 12
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i * j == N:
            print(f"{i} * {j} = {N}")

# 5. Строки
#31
text = "python"
print(len(text))

#32
text = "Привет"
vowels = "аоуыэяёюеиАOUЫЭЯЁЮЕИ"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(count)

#33
text = "Её зовут Анна"
words = text.split()
print(len(words))

#34
text = "level"
if text[::-1] == text:
    print("Палиндром")
else:
    print("Не палиндром")

#35
text = "Hello world "
text = text.replace(" ", "_")
print(text)

#36
text = "banana"
print(text.count("a"))

#37
text = "Её зовут Анна"
words = text.split()
longW = max(words, key=len)
print(longW)

#38
text = "hello"
print(text[::-1])

#39
text = "absd1234"
res = ""
for char in text:
    if not char.isdigit():
        res += char
print(res)

#40
w1 = "read"
w2 = "dear"
if sorted(w1) == sorted(w2):
    print("Анаграммы")
else:
    print("Не анаграммы")

# 6. Списки
#41
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

#42
numbers = [1, 2, 3, 4, 5]
print(max(numbers))

#43
numbers = [1, 2, 3, 4, 5]
print(min(numbers))

#44
numbers = [1, 5, 3, 8, 4]
numbers.sort(reverse=True)
print(numbers[1])

#45
numbers = [1, 1, 2, 3, 4, 4]
numbers = list(set(numbers))
print(numbers)

#46
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])

#47
numbers = [1, 2, 3, 4, 5]
count = 0
for i in numbers:
    if i % 2 == 0 :
        count += 1
print(count)

#48
l1 = [1, 2, 3]
l2 = [3, 4, 5]
resl = list(set(l1 + l2))
print(resl)

#49
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
resl = list(set(l1) & set(l2))
print(resl)

#50
nums = [1, 2, 3, 4, 5]
k = 2
resl = nums[-k:] + nums[:-k]
print(resl)

# 7. Кортежи и множества
#51
num = (1, 2, 3, 4, 5)
print(sum(num))

#52
num = [1, 2, 3, 4, 5]
print(set(num))

#53
a = {1, 2, 3}
b = {3, 4, 5}
if a == b:
    print("True")
else:
    print("False")

#54
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

#55
a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)

# 8. Словари
#56
text = "hello"
count = {}
for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)

#57
text = "apple banana apple orange banana apple"
words = text.split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)

#58
pb = {
    "John": "123456789",
    "Mike": "987654321",
    "Sarah": "555555555"
}
print(pb)

#59
score = {
    "John": 85,
    "Mike": 92,
    "Vasya": 88
}
best_s = max(score, key=score.get)
print(best_s)

#60
person = {
    "name": "John",
    "city": "London",
    "age": "20"
}
rever_per = {}
for key, value in person.items():
    rever_per[value] = key
print(rever_per)

# 9. Функции
#61
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(factorial(5))

#62
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(prime(7))
print(prime(8))

#63
def gcd(a, b):
    res = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0 :
            res = i
    return res
print(gcd(36, 48))

#64
def pow(a, b):
    return a ** b
print(pow(2, 4))

#65
def sum_dig(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res
print(sum_dig(456))



