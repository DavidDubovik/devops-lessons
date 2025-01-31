def read_from_file(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        text = file.read()
    return sorted(word.lower() for word in text.split() if word.lower().startswith("w"))


print(read_from_file("text"))
