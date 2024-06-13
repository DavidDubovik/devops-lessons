# import this
# import pdb
# def parse_students(students_data: str) -> list[str]:
#     return students_data.split(", ")
#
#
# if __name__ == "__main__":
#     print(parse_students("mark, borys, Kate, anna, Viktor"))
# ------------------------------->
# дебагинг
# a = 10
# b = a + 5
# # pdb.set_trace()
# print(f"{b = } {float(b) = }")
# c = a + b
# d = a + b + c
# print(f"{d = }")
# print(c)
# як дебажить в середені функцій і циклів
# def print_index_ok(index: int):
#     print(index)
#     print("Ok!")
#
# print("~~~~~ START ~~~~~")
#
# for i in range(3):
#     print_index_ok(i)
#
#
# print("~~~~~ END ~~~~~")