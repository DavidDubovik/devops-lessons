# def create_list(n):
#     if n == 0:
#         return []
#     list_number = []
#     for x in range(1, n+1):
#         if x % 2 == 0:
#             list_number.append(x)
#     return list_number
#
#
#
# print(create_list(7))
# -------------------------------->
# Find and fix the issue

# def calculate_average(numbers):
#     total = 0
#     count = len(numbers)
#     for number in numbers[1:]:
#         total += number
#
#     if count > 0:
#         return total // count
#
#     return 0
#
#
# print(calculate_average([0, 30.0]))
# ---------------------------------------------->
# Find and fix the issue

# Find and fix the issue

# def find_max(numbers):
#     if numbers == []:
#         return None
#
#     max_num = 0
#     for num in numbers:
#         if max_num < num:
#             max_num = num
#     return max_num

# ----------------------------------------------------->
# def make_lemonade(sugar_grams: int, water_liters: int) -> int:
#     #  Write code here
#     if water_liters == 0:
#         return float("nan")
#
#     portions_from_water = water_liters * 2  # 1 літр = 2 порції (500 мл на порцію)
#     portions_from_sugar = sugar_grams // 100  # 100 г цукру на одну порцію
#
#     # Повертаємо мінімальне значення між можливими порціями
#     return min(portions_from_water, portions_from_sugar)
#
#
# print(make_lemonade(600, 6))

# --------------------------------------------------------------->
# user_input = "   username@example.com   "
# cleaned_input = user_input.strip()
# left_strip_input = user_input.lstrip()
# right_strip_input = user_input.rsplit()

#  Write code here
# --------------------------------------------------------------->
# def count_substring(sentence: str, substring: str) -> int:
#     return sentence.count(substring)
#
#
# print(count_substring("Thank you for coming! Thank you for being with us!", "Thank you"))  # 2
# print(count_substring("I love my job because it gives me satisfaction ", "love"))  # 1
# _------------------------------------------------------------------>

# def rotate_list(nums, steps):
#     if not nums:
#         return nums
#
#     return nums[-steps:] + nums[:-steps]
#
#
# # Тестування функції
# print(rotate_list(nums=[1, 2, 3, 4, 5, 6, 7], steps=3))  # [5, 6, 7, 1, 2, 3, 4]
# print(rotate_list(nums=[-1, -100, 3, 99], steps=2))  # [3, 99, -1, -100]
# ---------------------------------------------------------------------------------->
# def odd_ones_out(numbers: list) -> list:
#     # Підрахунок частоти кожного числа
#     counts = {}
#     for num in numbers:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1
#
#     result = []
#     for num in numbers:
#         if counts[num] % 2 == 0:
#             result.append(num)
#
#     return result
#
#
# print(odd_ones_out([26, 23, 24, 17, 23, 24, 23, 26]))  # == [26, 24, 24, 26]
# print(odd_ones_out([1, 2, 3, 1, 3, 3]))  # == [1, 1]
# print(odd_ones_out([1, 2, 3]))  # == []
# --------------------------------------------------------------->
# def coin_combination(cents: int) -> list:
#     # Створюємо список з чотирма елементами, щоб зберігати кількість монет
#     coins = [0, 0, 0, 0]
#
#     # Спочатку обчислюємо кількість четвертаків (25 центів)
#     coins[3] = cents // 25
#     cents %= 25
#
#
#     # Далі обчислюємо кількість даймів (10 центів)
#     coins[2] = cents // 10
#     cents %= 10
#
#     # Потім обчислюємо кількість п'ятаків (5 центів)
#     coins[1] = cents // 5
#     cents %= 5
#
#     # Нарешті, обчислюємо кількість пенні (1 цент)
#     coins[0] = cents
#
#     return coins
#
#
# # [0, 0, 0, 0]
# # індекс [0] відображає пенні (1 цент)
# # індекс [1] відображає п'ятаки (5 центів)
# # індекс [2] відображає дайми (10 центів)
# # індекс [3] відображає четвертаки (25 центів)
#
# # print(coin_combination(6))  # == [1, 1, 0, 0]
#
# print(coin_combination(42))  # == [2, 1, 1, 1]
#
# # print(print(coin_combination(100)))  # == [0, 0, 0, 4]
# ------------------------------------------------------------->
# def two_to_one(first_str: str, second_str: str) -> str:
#     # write your code here
#     one_str = first_str + second_str
#     sorted_text = "".join(sorted(set(one_str)))
#     return sorted_text
#
#
# two_to_one(first_str="abcde", second_str="ABCDE")  # == "ABCDEabcde"
#
# two_to_one(first_str="xyaabbbccccdefww", second_str="xxxxyyyyabklmopq")  # == "abcdefklmopqwxy"
# ------------------------------------------------------------->
# def detect_capital(word: str) -> bool:
#     # write your code here
#     if word == word.lower():
#         return True
#     if word == word.upper():
#         return True
#     for item in word[1:]:
#         if item.isupper():
#             return False
#     if word[0].isupper():
#         return True
#
#
# #
# print(detect_capital("USA"))  # is True
# #
# print(detect_capital("FlaG"))  # is False
# #
# print(detect_capital("python"))  # is True
# print(detect_capital("mAte"))

# ---------------------------------------------------------->

# def capitals_first(sentence: str) -> str:
#     # write your code here
#     words = sentence.split()
#     capital_words = [word for word in words if word[0].isupper()]
#     lower_words = [word for word in words if word[0].islower()]
#
#     return " ".join(capital_words + lower_words)
#
#
# print(capitals_first("academy Mate"))  # == "Mate academy"
#
# print(capitals_first("one Two three Four"))  # == "Two Four one three"
# -------------------------------------------------------------------------->
# def maximum_product(num_list: list) -> int:
#     # write your code here
#     count = 1
#     sum_list = []
#     for num in num_list:
#         for item in num_list[count:]:
#             sum_list.append(num * item)
#             count += 1
#             break
#
#     return max(sum_list)
#
#
# print(maximum_product([1, 2, 3]))  # == 6
# print(maximum_product([-5, 0, 3, 5, 2]))  # == 15
