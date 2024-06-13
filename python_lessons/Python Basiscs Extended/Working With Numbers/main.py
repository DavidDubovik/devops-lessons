# int
# x1 = 42
# print(f"{x1=}, {type(x1)=}")
#
# x2 = 0b101010 # 0b використувується для позвначеня двійковой системи численя
# print(f"{x2=}, {type(x2)=}")
#
# x3 = 0o52
# print(f"{x3=}, {type(x3)=}")
#
# x4 = 0x2a  # 0x2A [0-9] [a-f] or [A-F]
# print(f"{x4=}, {type(x4)=}")
# print()
#
# # float
# y1 = 42.0
# y2 = 42.
# print(f"{y1=}, {type(y1)=}")
#
# y3 = 0.42e2  # 0.42 * 10 ** 2
# y4 = .42e2
# print(f"{y3=}, {type(y3)=}")
#
# y5 = 42_000_000e-6  # 42_000_000 / 10 ** 6
# print(f"{y5=}, {type(y5)=}")
# --------------------------------->
# def get_century(year: int) -> int:
#     # write your code here
#     if year == 0:
#         return 1
#     return round(abs((year / 100) // -1))
#
#
# get_century(2001)  # == 21
# get_century(1)  # == 1
# get_century(1786)  # == 18
# get_century(1500)  # == 15
# get_century(201)
# --------------------------------->
# 10 в тебе катет номер один
#
#
# 20 це гіпотенуза
#
#
# Для знаходження площі тобі треба знайти катет номер 2
#
#
# Щоб його знайти
#
# Треба
#
# Взяти корінь з (20 в квадраті - 10 в квадраті )
#
# І це буде 2 катет
#
# А площа дорівнює
#
# 1 катет помножений на 2
# import math
#
# def get_rectangle_area(side: int, diagonal: int) -> float | str:
#     # write your code here
#     if diagonal > side:
#         sum_number = math.sqrt(diagonal ** 2 - side ** 2)
#         return round(side * sum_number, 1)
#
#     return "not a rectangle"
#
#
# print(get_rectangle_area(10, 20))  # == 173.2
# print(get_rectangle_area(9, 18))  # == 140.3
# print(get_rectangle_area(100, 98))  # == "not a rectangle"

# --------------------------------->
# def number_checker(number: float) -> list:
#     # write your code here
#     bool_result = [False, False]
#     if number == float("-inf") or number == float("inf"):
#         bool_result[0] = True
#     if number != number:
#         bool_result[1]= True
#     return bool_result
#
#
# print(number_checker(1))  # == [False, False]
# print(number_checker(-1e10000))  # == [True, False]
# print(number_checker(float("nan")))  # == [False, True]
#
#
#
#

# --------------------------------->
# def make_decision(
#         fuel_remaining: int,
#         distance: int,
#         fuel_consumption: float
# ) -> str:
#     # write your code here
#     if 0 > fuel_remaining or 0 >= fuel_consumption or 0 >= distance:
#         return "please, enter the valid data"
#     if (fuel_remaining / (fuel_consumption / 100)) >= distance:
#         return "reach gas station by themselves"
#     if (fuel_remaining / (fuel_consumption / 100)) < distance:
#         return "ask for help"
#
#
# #
# #
#
#
# # print(make_decision(3, 34, 6.5))  # == "reach gas station by themselves"
# # print(make_decision(0, 34, 6.5))  # == "ask for help"
# # print(make_decision(-2, -30, 0))  # == "please, enter the valid data"
# # print(make_decision(0, 34, 6.5))

# --------------------------------->
# def count_networking(quarantine_length: int, frequency: int) -> int:
#     # write your code her
#     parties = []
#     for i in range(quarantine_length, 12, frequency):
#         parties.append(i)
#
#     return len(parties)
#
#
# print(count_networking(0, 1))  # == 12 - кожен місяць
# print(count_networking(3, 1))  # == 9 - кожен місяць починаючи з 4-го
# print(count_networking(3, 2))  # == 5 - місяці 4, 6, 8, 10 та 12
# count_networking(12, 1)  # == 0 - карантин на весь рік
# count_networking(11, 3)  # == 1 - в останній місяць року
# count_networking(2, 5)  # == 2 - місяці 3 та 8
# count_networking(3, 4)  # == 3 - місяці 4, 8 та 12
# --------------------------------->


# import random
#
#
# def generate_random_list(min_value: int, max_value: int, length: int) -> list:
#     # write your code here
#     random_number = []
#     for i in range(length):
#         random_number.append(random.randint(min_value, max_value))
#     return random_number
#
#
# print(generate_random_list(1, 1, 1) ) # == [1]
# print(generate_random_list(1, 3, 5))  # == [2, 3, 1, 1, 3]
# print(generate_random_list(-1, 1, 3))  # == [0, 1, 1]
