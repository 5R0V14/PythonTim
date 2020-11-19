number = int(input("Введите ваше число: "))

num1 = number % 10
num2 = number // 10 % 10
num3 = number // 100

result = num1 * 100 + num2 * 10 + num3
print("Обратное ему число:", result)