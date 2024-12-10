# infinite loop
# age = 0
# # for _ in range(1, 5 + 1):
# # можна ще записати так:
# # for _ in iter(int, 1):  # int генерує безкінечне число нуль і получться безконечна послідовність
# # але можна записати на багато краще через цикл while
# while True:
#     age = input("Please enter your age")
#     if age.strip().isnumeric():
#         age = int(age)
#         break
# print(f"Your age is {age}")
# ----------------------------------->
# Break,continue
# def calc(a: int, b: int, c: int) -> float:
#     if b == 0:
#         return 0.0
#     d = a + c
#     result = d / b
#     return result
# %%
# for index in range(1, 10 + 1):
#     if index % 2 != 0:
#         continue
#     print("index equals ", end="")
#     print(index)
# %%
# for index in range(1, 100 + 1):
#     if index >= 5:
#         break
#     print(index)
# print("loops finished")
# ----------------------------------->
# Loop variable
# number = -1
# for n in range(1, 10 + 1):
#     print(n)
#     number = n
#
# print(number)
# ----------------------------------->
# Loop condition calculation
# import time
# def get_value() -> int:
#     time.sleep(5)
#     value = 10
#     print("'gent_value' is generated a value")
#     return value
#
#
# get_value()
#
# for number in range(get_value()):
#     print(number)
# %%
# import time


# def get_value() -> int:
#     time.sleep(5)
#     value = 10
#     print("'gent_value' is generated a value")
#     return value
#
#
# start = time.time()
# VALUE = get_value()
#
# for number in range(5):
#     result = number * VALUE
#     print(number)
#
# print(f"It took {time.time() - start} secs ")
# ----------------------------------->
# When to use infinite loop
# import random
#
#
# def get_value() -> int | float:
#     value = random.random()
#
#     if value < 0.2:
#         return 0
#
#     return value
#
#
# while True:
#     x = get_value()
#     if x == 0:
#         break
#     print(x)

# ----------------------------------->
# loop in loop
# seq1 = 1, 2, 3, 4, 5
# seq2 = 10, 20, 30, 40, 50

# seq1 = range(1, 5 + 1, 1)
# seq2 = range(10, 50 + 1, 10)


# def calc(a: int, b: int) -> int:
#     return a + b
#
#
# for dozens in seq2:
#     for units in seq1:
#         res = calc(dozens, units)
#         print(res)


# ----------------------------------->
#          Practice
# def check_is_prime(number: int) -> bool:
#     # write your code here
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
#
# # print(check_is_prime(1))  # is False
# # print(check_is_prime(2))  # is True
# print(check_is_prime(13))  # is True
# # print(check_is_prime(-3))  # is False
# print(check_is_prime(25))  # is False
# %%
# def get_years(amount: int, percent: int, limit: int) -> int:
#     # write your code here
#     start_limit = amount
#     years = 0
#     while start_limit <= limit:
#         years += 1
#         start_limit = start_limit + (start_limit * (percent / 100))
#
#     return years - 1
#
#
# print(get_years(1600, 10, 2000))  # == 2
# print(get_years(500, 3, 550))  # == 3
# %%
# def detect_lowercase_words() -> None:
#     # write your code here
#     while True:
#         text = input()
#         if text == "exit":
#             break
#         if text.islower():
#             print(f"{text} detected")
#
#
# detect_lowercase_words()
# ------------------------------------------------------->
# def seating_arrangement(rows, seats_per_row):
#     arrangement = []
#     for row in range(1, rows + 1):
#         seats = [f"Seat {seat}" for seat in range(1, seats_per_row + 1)]
#         row_str = f"Row {row}: " + ", ".join(seats)
#         arrangement.append(row_str)
#     return arrangement
#
# # Приклад використання
# print(seating_arrangement(3, 0))
# #     "Row 1: Seat 1, Seat 2, Seat 3, Seat 4",
# #     "Row 2: Seat 1, Seat 2, Seat 3, Seat 4",
# #     "Row 3: Seat 1, Seat 2, Seat 3, Seat 4"
# # ]

# ------------------------------------------------------->
# def check_emails_against_blacklist(emails: list[str], blacklist: set) -> str:
#     #  Write code here
#     for email in emails:
#         if email in blacklist:
#             return email
#     return ""
#
#
# emails = ["user@example.com", "spam@blacklist.com", "anotheruser@example.com"]
# blacklist = {"spam@blacklist.com", "banneduser@example.com"}
#
# print(check_emails_against_blacklist(emails, blacklist))  # ["spam@blacklist.com"]
# ------------------------------------------------------->
# Базовий клас Human
class Human:
    pass

# Підкласи Man та Woman
class Man(Human):
    pass

class Woman(Human):
    pass

# Функція god, яка повертає список з об'єктами Адама і Єви
def god():
    return [Man(), Woman()]

# Виклик функції та перевірка результату
adam_and_eve = god()
print(adam_and_eve)  # Виведе список з екземплярами Man і Woman
