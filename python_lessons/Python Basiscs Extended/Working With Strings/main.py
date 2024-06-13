# def make_upper(text: str, letter: str) -> list:
#     # write your code here
#     count = 0
#     for i in range(len(text)):
#         if text[i] == letter:
#             count += 1
#
#     return [text.replace(letter, letter.upper()), count]
#
#
# make_upper("aaa", "a") #== ["AAA", 3]
# make_upper("bBb", "b") #== ["BBB", 2]
# make_upper("some long text", "e") #== ["somE long tExt", 2]
# make_upper("aaabbabba", "b") #== ["aaaBBaBBa", 4]
# ------------------------------------>
# def calculate_guests(guests_input: str) -> int | str:
#     words = guests_input.replace(".", " ").split()
#     for word in words:
#         """Метод "".join(filter(str.isdigit, word)) використовується для вибору лише цифр з рядка word і об'єднання їх у новий рядок.
#          Давайте розглянемо його крок за кроком:
#
#       filter(str.isdigit, word) - цей фільтр приймає функцію str.isdigit і рядок word.
#        Він застосовує функцію str.isdigit до кожного символу у рядку word і повертає лише ті символи, для яких функція str.isdigit повертає True.
#        Це означає, що лише цифри залишаються після фільтрації.
#
#       "".join(...) - цей метод приймає ітерабельний об'єкт (у нашому випадку, результат фільтрації) і об'єднує його елементи в один рядок. В нашому випадку, це об'єднує всі відфільтровані цифри в один рядок.
#       Таким чином, "".join(filter(str.isdigit, word)) видаляє всі символи, які не є цифрами, з рядка word і повертає лише цифри у вигляді рядка. це залупа а не задача """
#         digits = ''.join(filter(str.isdigit, word))
#         if digits == "0":
#             return "not a number"
#         if digits.isdigit():
#             return int(digits)
#     return "not a number"
#
# #
# print(calculate_guests("I think 5 guests"))  # == 5
# print(calculate_guests("Big company of 15 dudes"))  # == 15
# print(calculate_guests("5"))  # == 5
# print(calculate_guests("alone"))  # == "not a number"
# print(calculate_guests("0"))  # == "not a number"
# print(calculate_guests("Hello, 9.75 people"))  # == 9
# print(calculate_guests("There will be 7 or 9 guys"))  # == 7
# print(calculate_guests("hello cat walks on my keyboard ksadjfhskaj12.34kasdfhsjk"))  # == 12

# ------------------------------------>

# def is_alphabet(letters: str) -> bool:
#     # write your code here
#     for i in range(len(letters)):
#         print(not (ord(letters.lower()[i]) - ord("a") + 1) + 1 >= (ord(letters.lower()[i]) - ord("a") + 1))
#         # if not i + 1 >= ord(letters.lower()[i]) - ord("a") + 1:
#         #     return False

# def is_alphabet(letters: str) -> bool:
#     # write your code here
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     return letters.lower() in alphabet
#

# print(is_alphabet("abc"))  # is True
# print(is_alphabet("aBc"))  # is True
# print(is_alphabet("abd"))  # is False - після b йде c
# print(is_alphabet("a"))  # is True
# print(is_alphabet("abcdefghjiklmnopqrstuvwxyz"))  # is False - j йде після i
# print(is_alphabet("tuvwxyz"))  # is True
# print(is_alphabet("XYZ"))  # is True
# print(is_alphabet("mnoprqst"))  # is False - q йде перед r
# ------------------------------------>
# def extract_names(message: str) -> list:
#     # write your code here
#     new_txt = message.strip()
#     names_list = []
#     for txt in new_txt.split(","):
#         # names_list.append(txt.strip())
#
#     return names_list
#
#
# print(extract_names("Oleg"))  # == ["Oleg"]
# print(extract_names("Ivan,  Mark,  Sergey"))  # ==  ["Ivan", "Mark", "Sergey"]
# print(extract_names("Ivan,Mark,Sergey"))  # ==  ["Ivan", "Mark", "Sergey"]
# print(extract_names("Catelyn Stark,Samwell Tarly, Bronn"))  # =["Catelyn Stark","Samwell Tarly","Bronn"]
# ------------------------------------>
def make_variable_name(words: str, number_of_words: int) -> str:
    # write your code here
    if number_of_words == 0:
        return ""
    list_change = words.replace(" ", "_", number_of_words - 1).split(" ")
    return list_change[0]


print(make_variable_name("a b", 0))  # == "x"
print(make_variable_name("a plus b problem", 3))  # == "a_plus_b"
print(make_variable_name("my favorite variable name is x", 3))  # == "my_favorite_variable"
