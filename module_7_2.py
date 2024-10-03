from pprint import pprint as pprint


def custom_write(file_name, strings):
    file = open(file_name, "w", encoding="utf-8")
    string_positions = {}
    string_num = 0
    str_start_byte = file.seek(0)
    for string in strings:
        file.write(string + "\n")
        string_num += 1
        key = (string_num, str_start_byte)
        string_positions[key] = string
        str_start_byte = file.tell()
    file.close()
    return string_positions


info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!",
]

result = custom_write("test.txt", info)
for elem in result.items():
    print(elem)
