import json
import time

filtered_numbers = []

def is_valid_number(number):
    if len(number) != 10:
        return False

    for char in number:
        if not char.isdigit():
            return False

    if number[0] != "0":
        return False

    if number[0] == "0" and number[1] == "0":
        return False

    if number.count(number[0]) == len(number):
        return False

    return True

def format_number(number):
    formated_number = number

    formated_number = formated_number.replace('.', '').strip().replace('+33', '0')

    return formated_number

with open("signal_arnaques.json") as json_file:
    numbers = json.load(json_file)

    print(f"signal_arnaques : {len(numbers)}")

    for number in numbers:
        formated_number = format_number(number)

        if is_valid_number(formated_number):
            filtered_numbers.append(formated_number)

with open("arnaques_internet.json") as json_file:
    numbers = json.load(json_file)

    print(f"arnaques_internet : {len(numbers)}")

    for number in numbers:
        formated_number = format_number(number)

        if is_valid_number(formated_number):
            filtered_numbers.append(formated_number)

print(f"filtered_numbers : {len(filtered_numbers)}")

with open("./filtered_merge.json", "w+") as out_file:
    json.dump(filtered_numbers, out_file)
