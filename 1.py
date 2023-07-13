# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def see_info(file_name: str):
    with open(file_name, "r", encoding="utf-8") as data: # не забывать для русских букв указывать энкодинг!
        for line in data:
            print(*line.split(";"), end="")

def records(file_name: str):
    with open(file_name, "r+", encoding="utf-8") as data:
        record_id = 0
        for line in data:
            if line != "":
                record_id = line.split(";", 1)[0]
        print("Введите ФИО и номер телефона (через пробел)")
        line = f"{int(record_id) + 1};" + ";".join(input().split()[:4]) + ";\n"
        confirm = proof("добавление записи в список")
        if confirm == "да":
            data.write(line)

def find_char():
    print("Выберите параметр:")
    print("0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти")
    char = input()
    while char not in ("0", "1", "2", "3", "4", "q"):
        print("Введены неверные данные, повторите")
        print("Выберите параметр:")
        print("0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти")
        char = input()
    if char != "q":
        inp = input("Введите требуемое значение\n")
        return char, inp
    else:
        return "q", "q"

def find_info(file_name: str, char, condition):
    if condition != "q":
        printed = False
        with open(file_name, "r", encoding="utf-8") as data:
            for line in data:
                if condition == line.split(";")[int(char)]:
                    print(*line.split(";"))
                    printed = True
        if not printed:
            print("Не найдено, повторите запрос")
        return printed

def check_id_record(file_name: str, text: str):
    decision = input(f"Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n")
    while decision not in ("1", "q"):
        if decision != "2":
            print("Введены неверные данные, повторите запрос")
        else:
            find_info(path, *find_char())
        decision = input(f"Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n")
    if decision == "1":
        record_id = input("Введите id, q - выйти\n")
        while not find_info(file_name, "0", record_id) and record_id != "q":
            record_id = input("Введите id, q - выйти\n")
        return record_id
    return decision

def proof(text: str):
    confirm = input(f"Подтвердите {text} записи: да/нет\n")
    while confirm not in ("да", "нет"):
        print("Введены неверные данные, повторите")
        confirm = input(f"Подтвердите {text} записи: да/нет\n")
    return confirm

def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ""
    with open(file_name, "r", encoding="utf-8") as data:
        for line in data:
            replaced += line
            if record_id == line.split(";", 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, "w", encoding="utf-8") as data:
        data.write(replaced)

def change_info(file_name: str):
    record_id = check_id_record(file_name, "изменить")
    if record_id != "q":
        replaced_line = f"{int(record_id)};" + ";".join(
            input("Введите ФИО и номер телефона (через пробел)\n").split()[:4]) + ";\n"
        confirm = proof("изменение")
        if confirm == "да":
            replace_record_line(file_name, record_id, replaced_line)

def delete_info(file_name: str):
    record_id = check_id_record(file_name, "удалить")
    if record_id != "q":
        confirm = proof("удаление")
        if confirm == "да":
            replace_record_line(file_name, record_id, "")

path = "phone_book.txt"

try: 
    file = open(path, "r")
except IOError:             
    print("Создан новый справочник -> phonebook.txt")
    file = open(path, "w")
finally:                    
    file.close()

actions = {"1": "список",
           "2": "запись",
           "3": "поиск",
           "4": "изменение",
           "5": "удаление",
           "q": "выход"}

action = None
while action != "q":
    print("Какое действие Вы хотите совершить?", *[f"{i} - {actions[i]}" for i in actions])
    action = input()
    while action not in actions:
        print("Какое действие Вы хотите совершить?", *[f"{i} - {actions[i]}" for i in actions])
        action = input()
        if action not in actions:
            print("Введены неверные данные, повторите")
    if action != "q":
        if action == "1":
            see_info(path)
        elif action == "2":
            records(path)
        elif action == "3":
            find_info(path, *find_char())
        elif action == "4":
            change_info(path)
        elif action == "5":
            delete_info(path)