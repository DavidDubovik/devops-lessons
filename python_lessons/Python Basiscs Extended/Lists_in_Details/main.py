# List reverse, sort, copy
# numbers = [5, 3, 6, 1, 7]
# # %%
# print(numbers.reverse())
# # %%
# numbers = [5, 3, 6, 1, 7]
# reversed(numbers)
# # %%
# numbers = [5, 3, 6, 1, 7]
# reversed_numbers = reversed(numbers)
# reversed_numbers
# # %%
# list(reversed_numbers)
# # %%
# reversed_numbers
# # %%
# numbers = [5, 3, 6, 1, 7]
# numbers[::-1]  # так можна швидко розмернути список
# # %%
# numbers = [5, 3, 6, 1, 7]
# print(numbers.sort())
# # %%
# numbers
# # %%
# numbers = [5, 3, 6, 1, 7]
# numbers.sort(reverse=True)
# numbers
# # %%
# numbers = [5, 3, 6, 1, 7]
# sorted(numbers, reverse=True)
# # %%
# numbers = [5, 3, 6, 1, 7]
# numbers.copy()
# # %%
# numbers[:]  # так можна створити копію списку за допомогою слайсів
# --------------------------------------->
# List sorted key function
# marks = ["good", "excellent", "bad", "good", "bad"]
# # %%
# sorted(marks)
#
#
# # %%
# def mark_order(mark: str) -> int:
#     if mark == "bad":
#         return 1
#     if mark == "good":
#         return 2
#     return 3
#
#
# sorted(marks, key=mark_order)
# #%%
# sorted(marks, key=mark_order, reverse=True)
# --------------------------------------->
# List +, extend
# girls = ["Alice", "Maria", "Susan"]
# boys = ["John", " Bob"]
# # %%
# for boy in boys:
#     girls.append(boy)
#
# # %%
# girls = ["Alice", "Maria", "Susan"]
# boys = ["John", " Bob"]
# girls.extend(boys)
# # %%
# girls = ["Alice", "Maria", "Susan"]
# boys = ["John", " Bob"]
#
# stidents = []
# for girl in girls:
#     stidents.append(girl)
#
# for boy in boys:
#     stidents.append(boy)
# # %%
# girls = ["Alice", "Maria", "Susan"]
# boys = ["John", " Bob"]
# stidents = []
# stidents.extend(girl)
# stidents.extend(boys)
# #%%
# girls = ["Alice", "Maria", "Susan"]
# boys = ["John", " Bob"]
#
# stidents = girls + boys # так можна швидко об'єднати два списка
# --------------------------------------->
# Min,max,sum
# min(1, 2, 3, 4)
# # %%
# max(1, 2, 3, 4)
# # %%
# numbers = [1, 2, 3, 4]
# # %%
# min(numbers)
# # %%
# max(numbers)
# # %%
# sum(numbers)
# # %%
# sum(numbers, start=10)
# # %%
# text = "abcd"
# # %%
# min(text)
# # %%
# max(text)
# # %%
# arr = ["a", "b", "c", "d"]
# sum(arr)
# # %%
# arr = ["a", "b", "c", "d"]
# sum(arr, start="")
# # %%
# arr = ["a", "b", "c", "d"]
# "".join(arr)
# # %%
# numbers = [100, 1, 2, 4, 111, 8]
#
#
# # %%
# def is_even_or_minus_1(x: int) -> int:
#     if x % 2 == 0:
#         return x
#     return -1
#
#
# # %%
# max(numbers, key=is_even_or_minus_1)
# # %%
# max(numbers, key=lambda x: x if x % 2 == 0 else -1)# повертає максимальне число що ділиться на 2

# --------------------------------------->
# All, any

# all_true = [True, True, True]
# not_all_true = [True, True, False]
# all_false = [False, False, False]
#
# numbers1 = [1, 2, 3, 4]
# numbers2 = [1, 2, 3, 0]
# numbers3 = [0, 0, 0]
#
# stidents1 = ["John", "Bob", "Alice"]
# stidents2 = ["John", "", "Alice"]
# # %%
# all(all_true)
# # %%
# all(not_all_true)
# # %%
# all(all_false)
# # %%
# all(numbers1)
# # %%
# all(numbers2)
# # %%
# all(numbers3)
# # %%
# all(stidents1)
# # %%
# all(stidents2)
# #%%
# any(all_true)
# # %%
# any(not_all_true)
# # %%
# any(all_false)
# # %%
# any(numbers1)
# # %%
# any(numbers2)
# # %%
# any(numbers3)
# # %%
# any(stidents1)
# # %%
# any(stidents2)


# --------------------------------------->
# # Tuple
# numbers = (1, 2, 3, 4, 4)
# # %%
# len(numbers)
# # %%
# numbers.index(4)
# # %%
# numbers.index(1)
# # %%
# numbers.count(4)
# # %%
# numbers.count(3)
# # %%
# numbers[0]  # err
# # %%
# numbers[3]  # err
# # %%
# double = numbers + numbers
# double
#
# # %%
# numbers.append(1)  # err
# # %%
# arr1 = ([1, 2, 3], [1, 2])
# arr1[1].append(5)
# # %%
# arr1 = ([1, 2, 3], [1, 2])
# tmp = arr1[1]
# # %%
# arr1 = ([1, 2, 3], "John", 0.1, ((1, 2), (2, 3)))
# # %%
# arr2 = 1, 2, 3
# # %%
# a = 1
# b = 2
#
# a, b = b, a  # змінюємо значення зміних  не використовуючи третю зміну
# # %%
# (a, b) = (b, a)  # з використанням розпаковки
# arr3 = (1,)
# arr4 = (1)
#
#
# # %%
# def get_pair(a: int, b: int, c: int, d: int) -> tuple:
#     sum1 = a + b
#     sum2 = c + b
#     return sum1, sum2
#
#
# result = get_pair(1, 2, 3, 4)
# print(f"""
#     {result=}
#     {type(result)}
# """)
# # %%
# seq1 = [1, 2, 3, 4]
#
# seq2 = tuple(seq1)
# seq2
# # %%
# tuple("abcd")
# --------------------------------------->
#  Practice


# def get_reversed_list(ls: list) -> list:
#     # write your code here
#     new_ls = ls.copy()
#     return new_ls.reverse()
#
#
# print(get_reversed_list([1, 2, 3]))  # == [3, 2, 1]
# print(get_reversed_list([70, -2]))  # == [-2, 70]


# %%
# def weekday_order(weekday: str) -> int:
#     # write your code here
#     if weekday == "Monday":
#         return 1
#     if weekday == "Tuesday":
#         return 2
#     if weekday == "Wednesday":
#         return 3
#     if weekday == "Thursday":
#         return 4
#     if weekday == "Friday":
#         return 5
#     if weekday == "Saturday":
#         return 6
#     if weekday == "Sunday":
#         return 7
#
#
# def sort_weekdays(weekdays: list) -> list:
#     # write your code here
#     sorted(weekdays, key=weekday_order)
#
#
# sort_weekdays(["Monday"])  # == ["Monday"]
# sort_weekdays(["Saturday", "Wednesday"])  # == ["Wednesday", "Saturday"]

# %%

# def get_speed_statistic(test_results: list) -> list:
#     # write your code here
#     speed_statistic = []
#     speed_statistic.append(min(test_results))
#     speed_statistic.append(max(test_results))
#     speed_statistic.append(int(sum(test_results) / len(test_results) // 1))
#     print(speed_statistic)
#
#
# get_speed_statistic([10, 10, 11, 9, 12, 8])  # == [8, 12, 10]
# get_speed_statistic([10])  # == [10, 10, 10]
# get_speed_statistic([8, 9, 9, 9])  # == [8, 9, 8]
# get_speed_statistic([5])  # == [5, 5, 5]
# get_speed_statistic([8, 12, 10])

# %%
# def all_targets_hit(attempts_for_each_target: list) -> bool:
#     # write your code here
#     hit = []
#     for i in range(len(attempts_for_each_target)):
#         hit.append(any(attempts_for_each_target[i]))
#     return all(hit)
#
#
# attempts = [
#     [True, False, True],  # Постріли у першу мішень
#     [False, True, False, True],  # Постріли у другу мішень
#     [False, True],  # Постріли у третю мішень
# ]
# print(all_targets_hit(attempts))  # is True # всі мішені були вражені хоча б один раз
#
# attempts = [
#     [True, False, True],  # Постріли у першу мішень
#     [False, False, True],  # Постріли у другу мішень
#     [False, False],  # Постріли у третю мішень
# ]
# print(all_targets_hit(attempts))  # is False # Третя мішень не була вражена


# %%

def create_dino_archive(
        dino_names: list,
        dino_lengths: list,
        dino_diets: list,
) -> list:
    # write your code here
    info_dino = []
    for i in range(len(dino_names)):
        info_dino.append((dino_names[i], dino_lengths[i], dino_diets[i]))
    return info_dino


print(create_dino_archive(
    ["Triceratops", "Saltopus"],
    [9, 1],
    ["carnivorous", "herbivorous"]
))  # == [("Triceratops", 9, "carnivorous"), ("Saltopus", 1, "herbivorous")]
