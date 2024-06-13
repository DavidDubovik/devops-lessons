# Dict
# first_name1 = "John"
# last_name1 = "Dou"
# age1 = 25
#
# first_name2 = "Alex"
# last_name2 = "Smith"
# age2 = 25
#
#
#
#
# def print_user(first_name: str, last_name: str, age: int):
#     print(f"User {first_name} {last_name} (age {age})")
#
#
# # %%
# print_user(first_name1, last_name1, age1)
# print_user(first_name2, last_name2, age2)

# %% теж саме тільки з використанням словника

# user1 = {
#     "first_name": "John",
#     "last_name": "Dou",
#     "age": 25,
# }
# user2 = {
#     "first_name": "Alex",
#     "last_name": "Smith",
#     "age": 20,
# }
#
#
# def print_user_info(user: dict):
#     print(f"User {user["first_name"]} {user["last_name"]} (age {user["age"]})")
#
#
# # %%
# print_user_info(user1)
# print_user_info(user2)

# ----------------------------------->
# Dict keys and values

# user = {
#     "first_name": "John",
#     "last_name": "Dou",
#     "age": 25,
# }
# %%
# user["first_name"]
# %%
# user["John"]
# %%
# шоб отримати значання по ключи на потрібно написати наступну конструкцію
# example_sict = {
#     1: {"key1": "value1"},
#     "some_key": "some_value",
#     None: [123, 456],
#     (1, 2): 10.1
# }

# %%
# example_sict[None]
# %%
# example_sict[(1, 2)]
# %%
# example_sict["some_key"]
# ----------------------------------->
# Change dict
# user = {
#     "first_name": "John",
#     "last_name": "Dou",
#     "age": 25,
# }
#
# # %%
# # user["first_name"]
# # %%
# # для того щоб змінити значення по ключу треба використати таку конструкцію
# user["first_name"] = "Alex"
# # %%
# user["last_name"] = "Smith"
# # %%
# print(
#     user["first_name"],
#     user["last_name"]
# )
# # %%
# # user["full_name"]
# # %%
# # якщо такого яключа немає то ми можимо створити наступною конструцією
# user["full_name"] = "Alex Smith"
# # %%
# # user["first_name"]
# # %%
# print(user)
# # %%
# del user["first_name"]
# #%%
# del user["last_name"]
# #%%
# print(user)
# ----------------------------------->
# Dict in, get
# user = {
#     "first_name": "John",
#     "last_name": "Dou",
#     "age": 25,
# }
#
# # %%
# user["age"]
# # %%
# user["ag"]
# # %%
# "age" in user
# # %%
# "ag" in user
# # %%
# print(user.get("age"))
# # %%
# print(user.get("ag"))
# # %%
# print(user.get("ag", 20))
# # %%
# print(user.get("age", 20))
# # %%


# ----------------------------------->
# Dict values overriding
# data = {
#     "3": 1,
#     "3": 2,
#     3: 3,
#     1 + 2: 4,
#     3.0: 5
# }
# # %%
# print(f"""
#    {data["3"]}
#    {data["3"]}
#    {data[3]}
#    {data[1 + 2]}
#    {data[3.0]}
#
# """)
# # %%
# {1: "Hello", True: "world"}
# # %%
# {True: "Hello", 1: "world"}
# # %%
# ----------------------------------->
# Dict methods
# user = {
#     "first_name": "John",
#     "last_name": "Dou",
#     "age": 25,
# }
# # %%
# len(user)
# # %%
# user.keys()
# # %%
# list(user.keys())
# # %%
# user.values()
# # %%
# list(user.values())
# # %%
# user.items()
# # %%
# list(user.items())
# # %%
# user
# # %%
# extended_info = {
#     "is_married": False,
#     "gender": "male"
# }
# # %%
# user.update(extended_info)
# # %%
# user
# # %%
# del user["is_married"]
# ----------------------------------->
# Dict iteration, keys(),values(),items()
# user = {
#     "first_name": "John",
#     "last_name": "Dou",
#     "age": 25,
# }
# # %%
# for key in user:
#     print(key)
#
# # %%
# for key in user:
#     print(key, user[key])
#
#
# #%%
# for pair in user.items():
#     key, value = pair
#     print(key, value)
#
#
# #%%
# for key, value in user.items():
#     print(key,value)
#
# #%%
# for value in user.values():
#     print(value)
# ----------------------------------->
# Set
# fruits = {"apple", "banana", "cherry", "apple"}
# # %%
# fruits
# # %%
# {1, 2, 3, 1, 2, 4}
# # %%
# {True, 1, 2, 3, 1, 2, 4}
# # %%
# {[1, 4, 5], (1, 4, 5)}
# # %%
# {{1: 2}, {2: 3}}
# # %%
# {"abc", "def"}
# ----------------------------------->
# Set methods
# fruits = {"apple", "banana", "cherry", "apple"}
# # %%
# len(fruits)
# # %%
# fruits.add("mango")
# # %%
# fruits.remove("cherry")
# # %%
# "cherry" in fruits
# # %%
# "mango" in fruits
# # %%
# fruits[0]
# # %%
# fruits[0] = "grape"
# %%
# for item in fruits:
#     print(item)
# # %%
# list(fruits)
# # %%
# like_football = {"Bob", "Alice", "John"}
# like_swimming = {"katrin", "Bob", "Alice", "Felix"}
# # %%
# like_football.intersection(like_swimming)
# # %%
# like_swimming.intersection(like_football)
# # %%
# like_football.union(like_swimming)

# ----------------------------------->
#   Practice
#
# warehouse = {
#     "memory": 15,
#     "processors": 10,
#     "displays": 15
# }
# %%

# def restore_names(users: list) -> None:
#     # write your code here
#     # users[0]["first_name"] = users[0]["full_name"].split()[0]
#     # users[i]["first_name"] = users[0]["full_name"].split()[0]
#     for i in range(len(users)):
#         name = {"first_name": users[i]["full_name"].split()[0]}
#         users[i].update(name)
#
#
# users = [
#     {
#         "last_name": "Holy",
#         "full_name": "Jack Holy",
#     },
#     {
#         "last_name": "Adams",
#         "full_name": "Mike Adams",
#     },
# ]
#
# restore_names(users)
#
# #  users == [
# #    {
# #      "first_name": "Jack",
# #      "last_name": "Holy",
# #      "full_name": "Jack Holy",
# #    },
# #    {
# #      "first_name": "Mike",
# #      "last_name": "Adams",
# #      "full_name": "Mike Adams",
# #    },
# #  ]


# %%
# def add_full_name(user: dict) -> None:
#     # write your code here
#     user["full_name"] = user["first_name"] + " " + user["last_name"]
#     print(user)
#
#
# user = {
#     "first_name": "Ivan",
#     "last_name": "Vasylchenko",
# }
#
# add_full_name(user)
#
# # user == {
# #   "first_name": "Ivan",
# #   "last_name": "Vasylchenko",
# #   "full_name": "Ivan Vasylchenko",
# # }


# %%
# def remove_country(users: list) -> None:
#     # write your code here
#     for i in range(len(users)):
#         if users[i]["status"] == "active":
#             del users[i]["country"]
#
#
# users = [
#     {"name": "Emma", "status": "active", "country": "Ukraine"},
#     {"name": "Avram", "status": "disabled", "country": "Poland"},
# ]
#
# # Видаляємо інформацію про країну у тих користувачів, у кого поле "status"
# # має значення "active" та отримуємо:
# remove_country(users)
# # users == [
# #     {"name": "Emma", "status": "active"},
# #     {"name": "Avram", "status": "disabled", "country": "Poland"},
# # ]


# %%
# def get_outdated(robots: list, new_version: int) -> list:
#     # write your code here
#     old_robots = []
#     for i in range(len(robots)):
#         if robots[i]["core_version"] < new_version:
#             old_robots.append(i)
#
#     print(old_robots)
#
#
# robots = [
#     {"core_version": 9},
#     {"core_version": 13},
#     {"core_version": 16},
#     {"core_version": 9},
#     {"core_version": 14},
# ]
#
# get_outdated(robots, 10)  # == [0, 3]
# get_outdated(robots, 14)  # == [0, 1, 3]
# get_outdated(robots, 8)  # == []
# get_outdated(robots, 18)  # == [0, 1, 2, 3, 4]


# %%
# def count_boxes(boxes: str) -> dict:
#     # write your code here
#     dict_boxes = {}
#     for i in boxes:
#         if not (i in dict_boxes):
#             dict_boxes[i] = boxes.count(i)
#     return dict_boxes
#
#
# print(count_boxes("aabca"))  # == {"a": 3, "b": 1, "c": 1}
# count_boxes("aaaaca31")  # == {"a": 5, "c": 1, "3": 1, "1": 1}
# count_boxes("")  # == {}


# %%


# def compare_robots(robot1: dict, robot2: dict) -> bool:
#     # write your code here
#     pass
#
#
# charlie = {"serial_no": 1, "chip_ver": 12}
#
# lordy = {"serial_no": 2, "chip_ver": 12}
# compare_robots(charlie, lordy)  # True
#
# paul = {"serial_no": 3, "chip_ver": 15}
# compare_robots(paul, charlie)  # False
#
# mike = {"serial_no": 4, "chip_ver": 12, "wheels": 1}
# compare_robots(mike, charlie)  # False
#
# max = {"serial_no": 5, "engine_ver": 12}
# compare_robots(max, charlie)  # False
#
# steve = {"serial_no": 6}
# compare_robots(steve, charlie)  # False

# %%
# def compare_robots(robot1: dict, robot2: dict) -> bool:
#  """
# robot1.items() - Це метод словника, що повертає пари ключ-значення для словника robot1.
#
# for key, value in robot1.items() - Це цикл, який проходить крізь кожну пару ключ-значення в словнику robot1.
#  key - це ключ, а value - відповідне значення.
#
# if key != "serial_no" - Це умова, яка перевіряє, чи ключ не дорівнює "serial_no".
#  Якщо умова виконується, пара ключ-значення додається до нового словника robot1_filtered.
#
# Аналогічно, robot2_filtered створюється за допомогою аналогічного підходу для robot2
# """
#     # Перевіряємо, чи збігаються характеристики за винятком "serial_no"
#     robot1_filtered = {key: value for key, value in robot1.items() if key != "serial_no"}
#     robot2_filtered = {key: value for key, value in robot2.items() if key != "serial_no"}
#     # Порівнюємо характеристики двох роботів
#     return robot1_filtered == robot2_filtered
#
#     # for i in robot1.keys():
#     #     if i not in robot2 or "chip_ver" not in robot1:
#     #         return False
#     #     if robot1["chip_ver"] == robot2["chip_ver"]:
#     #         return True
#     # return False
#
#
# charlie = {"serial_no": 1, "chip_ver": 12}
#
# lordy = {"serial_no": 2, "chip_ver": 12}
# print(compare_robots(charlie, lordy))  # True
#
# paul = {"serial_no": 3, "chip_ver": 15}
# print(compare_robots(paul, charlie))  # False
#
# mike = {"serial_no": 4, "chip_ver": 12, "wheels": 1}
# print(compare_robots(mike, charlie))  # False
#
# max = {"serial_no": 5, "engine_ver": 12}
# print(compare_robots(max, charlie))  # False
#
# steve = {"serial_no": 6}
# print(compare_robots(steve, charlie))  # False

# %%


# def count_marks(class_register: dict) -> dict:
#     evaluations = {}
#     for i in class_register.values():
#         if i not in evaluations:
#             evaluations[i] = 1
#         else:
#             evaluations[i] += 1
#     return evaluations
#
#
# class_register = {
#     "Robb Stark": 10,
#     "Sansa Stark": 12,
#     "Arya Stark": 6,
#     "Bran Stark": 8,
#     "Jon Snow": 8,
# }
#
# count_marks(class_register)


# %%


# def get_unique_marks(class_register: dict) -> list:
#     # write your code here
#     unique_assessments = set()
#     for value in class_register.values():
#         unique_assessments.add(value)
#     return list(unique_assessments)
#
#
# class_register = {
#     "Robb Stark": 2,
#     "Sansa Stark": 12,
#     "Arya Stark": 2,
#     "Bran Stark": 2,
#     "Jon Snow": 2,
# }
#
# print(get_unique_marks(class_register))


# %%
# def get_unique_items(ls: list) -> list:
#     # write your code here
#     numbers = set(ls)
#     return list(numbers)
#
#
# print(get_unique_items([1, 2, 4, 4]))  # == [1, 2, 4]
# print(get_unique_items([1, 7, 10]))  # == [1, 7, 10]
# print(get_unique_items([2, 7, 2, 8, 8, 1]))  # == [2, 7, 8, 1]
