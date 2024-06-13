# Conversion to bool
# condition = True
# if condition:
#     print("Hello", end=" ")
#     print("world")
# %%
# print(f"""
#  FALSY VALUE
# ================
#  False and None
# {bool(False) = }
# {bool(None) =}
#
# Numeric
#
# {bool(0) =}
# {bool(0.0) =}
# {bool(0j) =}
# {bool(Decimal(0)) =}
# {bool(Fraction(0)) =}
#
# Collections and sequences
#
# {bool("") =}
# {bool([]) =}
# {bool(()) =}
# {bool({}) =}
#
# {bool(set()) =}
# {bool(frozenset()) =}
# {bool(range(0)) =}
# """)
#
# print(f"""
# TRUTHY VALUE
# ============
# True
# {bool(True) = }
#
# Numeric
#
# {bool(1) =}
#
# {bool(0.1) = }
#
# {bool(1j) =}
# {bool(Decimal(1)) = }
# {bool(Fraction(1, 2)) = }
#
# Collections and sequences
# {bool("e") =}
# {bool([1, ]) =}
# {bool((1, )) =}
# {bool({1: 1}) =}
#
# {bool({1, }) =}
# {bool(frozenset({1, })) =}
# {bool(range(2)) = }
#
# Function
# {bool(int) = }
# """)
#
# students = []
# if students:  # good
#     print("Students are here")
#
# if len(students) != 0:  # bad
#     print("Students are here")
# # %%
# is_success = True
# if is_success:  # good
#     print("Good job")
#
# if is_success is True:  # bad
#     print("Good job")
# # %%
# owner = None
#
# if owner:
#     print("Owner is here")
#
# if owner is not None:
#     print("Owner is here")
# ------------------------------------>
# Conversion to number
# print(f"""
#    bool to int
#    {int(False) = }
#    {int(True) = }
#
#    string to int
#    {int("42") = }
#    {int("  42  ") = }
#    {int("42", 10) = }
#
#    bin
#    {int("0b10101", 2) = }
#
#    oct
#    {int("42", 8) = }
#    {int("0o42", 8) = }
#
#
#    hex
#    {int("4A", 16) = }
#    {int("0x4A", 16) = }
#
#    float to int
#    {int(0.6) = }
#    {int(1.6) = }
# """)
# # %%
# # ці обєкти не можна конвартирувать в числа типу int
# int([])  # {} [] () set() frozenset()
# # %%
# int("")
# int("adc")
# # %%
# int("1.1")
# # %%
# int(None)
# # %%
# # безпечні типи даних які можна конвертувати в число типа float
# print(f"""
#    {float("1") = }
#    {float("1.01") = }
#    {float("   1.01") = }
#    {float(True) = }
#    {float(False) = }
#
#    {float(2) = }
#
#    {float("nan") = }
#
#    {float("inf") = }
#    {float("-inf") =}
#
# """)
# # %%
# # ці обєкти не можна конвартирувать в числа типу float
# float([])  # {} [] () set() frozenset()
# # %%
# float("")
# float("adc")
# # %%
# float("1.1")
# # %%
# float(None)
# ------------------------------------>
# Compare data of different data types
# %%

# 5 < 10
# # %%
#
# "adc" > "bcd"
# # %%
# [1, 2, 3] == [1, 2, 3]
# # %%
# [1, 2, 3] < [2, 3, 1]
# # %%
# [1, 2, 3] < [1, 2, 2]
# # %%
# False < True
# # %%
# False == False
# # %%
# 10 < 10.5
# # %%
# 10.0 > False
# # %%
# 1.5 + True
# # %%
# 1 == "1"
# # %%
# 1 == [1]
# # %%
# 3 + "1"
# # %%
# 4.5 + [1.0]
# # %%
# "1" + ["1"]
# # %%
# 0 == None
# # %%
# "1" * 4
# # %%
# [5] * 4
# ------------------------------------>
#  Practice
# from typing import Any
#
# # У Python модуль typing використовується для анотації типів. Коли ви бачите код from typing import Any,
# # це означає, що ви імпортуєте тип Any з модуля typing.
# # Тип Any вказує на те,  що змінна може мати будь-який тип.
# # Використання цього типу може бути корисним у випадках,
# # коли вам потрібно сказати, що функція чи змінна може приймати або повертати значення будь-якого типу без обмежень.
# def decode_signal(message: Any) -> int:
#     # write your code here
#     return int(bool(message))
#
#
# print(decode_signal("abc"))  # == 1
# print(decode_signal("1"))  # == 1
# print(decode_signal(0))  # == 0
# print(decode_signal(""))  # == 0
# print(decode_signal(None))  # == 0


# %%

# def get_winner(
#         max_solved: str | int, roman_solved: str | int
# ) -> str:
#     # write your code here
#     if int(max_solved) > int(roman_solved):
#         return "Max winner!!!"
#     if int(max_solved) < int(roman_solved):
#         return "Roman winner!!!"
#     if int(max_solved) == int(roman_solved):
#         return "Roman and Maxim are the winners!!!"
#
#
# print(get_winner(45, "42"))  # == "Max winner!!!"
# print(get_winner("34", 35))  # == "Roman winner!!!"
# print(get_winner(24, 28))  # == "Roman winner!!!"
# print(get_winner("13", "11"))  # == "Max winner!!!"
# print(get_winner(15, "15"))  # == "Roman and Maxim are the winners!!!"
