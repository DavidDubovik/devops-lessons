# # %%
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# # %%
# add(1, 2)
# #%%
# add(1)
# #%%
# add()
#
#
# #%%
# def add(a: int = 0, b: int = 0) -> int:
#     return a + b
#
#
# #%%
# add(1)
# #%%
# add(1, 2)
# #%%
# add()
# ------------------------------------>
# Named arguments

# def calc(a: int, b: int, c: int) -> float:
#     return (a + b) / c
#
#
# #%%
# calc(1, 0, 2)
# #%%
# calc(1, 2, 0)
# #%%
# calc(c=2, a=1, b=0)
# calc(c=2, 1, 0)
# ------------------------------------------>
# *args and **kwargs

# def cals(a: int, b: int, c: int) -> int:
#     return a + b + c
#
#
# #%%
# cals(1, 2, 3)
# #%%
# cals(1, 2, 3, 4, 5, 6)
#
#
# # %%
# def cals(*args: int) -> int:
#     print(f"{type(args)} {args}") \
#             return sum(args)
#
#
# #%%
# cals(1, 2, 3)
# #%%
# cals(1, 2, 3, 4, 5, 6)
# -----------
# def cals(**kwargs: int):
#     print(f"{type(kwargs)} {kwargs}")
#
#
# #%%
# cals(a=1, b=2, c=3)
# #%%
# cals(a=1, b=2, c=3, d=4, e=5)
# ------------------------------------------>
# Lambda function
# def add(a: int, b: int) -> int:
#     """ Add two integers number and return sum """
#     return a + b
#
#
# #%%
# add(1, 2)
# #%%
# num1 = 1
# num2 = 2
# another_name = add
# another_name(num1, num2)
#
# #%%
# anonymous_func1 = lambda a, b: a + b
# anonymous_func2 = lambda a, b: a + b
#
# #%%
# add.__name__  # визначаємо ім'я функції
# #%%
# another_name.__name__
# #%%
# print(f"""
# {anonymous_func1.__name__ =} {id(anonymous_func1)}
# {anonymous_func2.__name__ =} {id(anonymous_func2)}
# """)

# ------------------------------------------>
# greeter = lambda name: f"Hello, {name}!"
#
# print(greeter("Mate")) #== "Hello, Mate!"
# print(greeter("Aristotle")) #== "Hello, Aristotle!"
# ------------------------------------------>
# triple_it = lambda txt: txt * 3
#
#
# print(triple_it("") )#== ""
# print(triple_it("a")) #== "aaa"
# print(triple_it("a b")) #== "a ba ba b"
# ------------------------------------------>

# def multiply_numbers(a: int = 1, b: int = 1, *args, **kwargs) -> int:
#     return a * b
#
#
# print(multiply_numbers())  # == 1
# print(multiply_numbers(2, 3))  # == 6
# print(multiply_numbers(b=5))  # == 5
# print(multiply_numbers(4, 3, "string", []))  # == 12
# print(multiply_numbers(1, 3, "string", k=22))  # == 3
# ------------------------------------------>

# def print_message(username: str = "John", message: str = "I like coding!") -> str:
#     print(f"Message from {username}:")
#     print(message)
#
#
# print_message(username="John", message="I like coding!")
# ------------------------------------------>