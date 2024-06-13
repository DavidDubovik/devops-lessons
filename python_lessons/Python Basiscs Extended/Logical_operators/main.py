# Logical operators in details
# def left_operand(value: int) -> int:
#     print("Left operand")
#     return value
#
#
# def right_operand(value: int) -> int:
#     print("Right operand")
#     return value
#
#
# print(left_operand(1) or right_operand(0))  # 1 or 0
# ------------------------------->
# Multiple logical operators
# def lo(value: int) -> int:
#     print("Left operand")
#     return value
#
#
# def ro(value: int) -> int:
#     print("Right operand")
#     return value
#
#
# print(lo(1) and ro(0))


# ------------------------------->
# Practice
#
# def can_they_book(adults_count: int, children_count: int = 0) -> bool:
#     # write your code here
#     if (adults_count + children_count) <= 8 and adults_count >= 1 and children_count <= adults_count * 2:
#         return True
#
#     return False
#
#
# print(can_they_book(0, 2))  # is False - 0 дорослих, 2 дитини. Порушення правил готелю.
# print(can_they_book(2, 4))  # is True - 2 дорослих, 4 дитини. Бронювання дозволено.
# print(can_they_book(2))  # is True - 2 дорослих. Бронювання дозволено.
# print(can_they_book(9))  # is False - 9 дорослих. Перевищено кількість осіб для однієї кімнати.

# %%

# def can_they_book(
#         adults_count: int,
#         children_count: int = 0,
#         babies_count: int = 0
# ) -> bool:
#     if adults_count == 0:
#         return False
#     total_people = adults_count + children_count + babies_count
#     if (total_people <= 8 or total_people == 9 and babies_count > 0) and adults_count >= 1 and (
#             babies_count + children_count) < adults_count * 2:
#         return True
#     return False

# %%
# def can_they_book(adults_count: int, children_count: int = 0, babies_count: int = 0) -> bool:
#     # Не можна бронювати, якщо немає дорослих
#     if adults_count == 0:
#         return False
#
#     # Розрахунок загальної кількості людей без додаткового місця для малюка
#     total_people = adults_count + children_count + babies_count
#
#     # Перевірка, чи загальна кількість людей не перевищує ліміт кімнати # Перевірка, чи є більше ніж 8 осіб без урахування додаткового місця для малюка
#     if total_people > 9 or total_people == 9 and babies_count == 0:
#         return False  # Більше ніж 9 людей, навіть з додатковим місцем для малюка, не дозволено
#
#     # Переконайтесь, що співвідношення дорослих до дітей+малюків є доречним
#     if (children_count + babies_count) > adults_count * 2:
#         return False
#
#     return True
#
#
# print(can_they_book(2, 3, 1))  # is True - Бронювання дозволено
# print(can_they_book(8, 0, 1))  # is True - Бронювання дозволено
# print(can_they_book(4, 2, 3))  # is True - Бронювання дозво/лено
# print(can_they_book(0, 1, 1))  # is False - Не можна бронювати без дорослих
# print(can_they_book(9))  # is False - Забагато людей
# print(can_they_book(8, 1))  # is False - Дитина не может бути дев'ятою
# print(can_they_book(2, 2, 3))  # is False - Недостатньо дорослихprint
# # print(can_they_book(4, 4, 2))  # False)
# # print(can_they_book(4, 4, 1))  # True


# %%


# def recommend_room(
#         adults_count: int,
#         children_count: int = 0,
#         babies_count: int = 0
# ) -> str:
#     total_people = adults_count + children_count + babies_count
#     # write your code here
#     if total_people <= 4:
#         return "small room"
#     elif total_people <= 5 and babies_count > 0:
#         return "small room + extra bed"
#     elif total_people <= 8:
#         return "big room"
#     elif total_people > 8 and babies_count > 0:
#         return "big room + extra bed"
#
#
# # print(recommend_room(2, 2, 1))  # == "small room + extra bed"
# # print(recommend_room(2, 1, 1))  # == "small room"
# # print(recommend_room(3, 2))  # == "big room"
# # print(recommend_room(3, 0, 2))  # == "small room + extra bed"
# # print(recommend_room(7, 0, 2))  # == "big room + extra bed"
# # print(recommend_room(8))  # == "big room"
# print(recommend_room(2, 3,))# == "big room"
