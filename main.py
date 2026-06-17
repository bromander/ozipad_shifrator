import os
import random
import sys

isxod = {
    "с": "8(",
    "г": "8Г",
    "о": "80",
    "д": "8D",
    "б": "8B",
    "ы": "8Ы",
    "у": "8У",
    "и": "8I",
    "ж": "8Ж",
    "т": "8Т",
    "ц": "8Ц",
    "п": "8P",
    "а": "84",
    "х": "8Х",
    "м": "8М",
    "з": "83",
    "в": "8)",
    "э": "8-)",
    "к": "8)К",
    ",": ";",
    "л": "/\\",
    "ф": "8(|)",
    "й": "8и́"
}


def fuck_that_shit(orig_letter: str):
    if orig_letter == "\n":
        return orig_letter

    if orig_letter == " ":
        if random.random() > 0.9:
            return "_"

    match reshimost:
        case 3:
            letter = isxod.get(orig_letter, orig_letter)

            if random.random() < 0.01:
                rand = random.random()
                if rand > 0.4:
                    letter += orig_letter
                else:
                    letter += orig_letter.upper()

            rand = random.random()
            if rand > 0.55:
                letter.upper()
            elif rand > 0.35:
                letter.lower()
            elif rand < 0.05 and not letter.startswith(")") and not letter.startswith("("):
                letter = letter + random.choice(("(", ")", " ", "8"))
            elif rand > 0.05 and not letter.startswith(")") and not letter.startswith("("):
                letter = random.choice(("(", ")", " ", "8")) + letter

        case 2:
            if random.random() > 0.4:
                letter = isxod.get(orig_letter, orig_letter)
            else:
                letter = orig_letter

            if random.random() < 0.015:
                rand = random.random()
                if rand > 0.4:
                    letter += orig_letter
                else:
                    letter += orig_letter.upper()

            rand = random.random()
            if rand > 0.45:
                letter.upper()
            elif rand > 0.35:
                letter.lower()
            elif rand < 0.04 and not letter.startswith(")") and not letter.startswith("("):
                letter = letter + random.choice((")", " ", "8"))
            elif rand > 0.04 and rand < 0.08 and not letter.startswith(")") and not letter.startswith("("):
                letter = random.choice((")", " ", "8")) + letter

        case 1:
            if random.random() < 0.05:
                letter = isxod.get(orig_letter, orig_letter)
            else:
                letter = orig_letter

            if random.random() < 0.01:
                rand = random.random()
                if rand > 0.4:
                    letter += orig_letter
                else:
                    letter += orig_letter.upper()

            rand = random.random()
            if rand > 0.6:
                letter.upper()
            elif rand > 0.3:
                letter.lower()
            elif rand < 0.04 and not letter.startswith(")") and not letter.startswith("("):
                letter = letter + random.choice((")", "8"))
            elif rand > 0.04 and rand < 0.08 and not letter.startswith(")") and not letter.startswith("("):
                letter = random.choice((")", "8")) + letter

    return letter

def get_input():

    if os.path.exists("./input.txt"):
        with open("input.txt", "r", encoding="UTF-8") as file:
            input_data = file.read()
    else:
        print("Файл с текстом не найден!")
        print("Чтобы применить эту ужасную шифровку, создайте файл 'input.txt' в тойже директории и вставьте в него нужный текст.")
        input()
        sys.exit(1)



    print("Введите силу шифрования:")
    print("1 - Слабо, 2 - нормально так, 3 - это нереально прочитать")

    while True:
        reshimost = int(input("> "))

        if reshimost not in (1, 2, 3):
            print("Значение должно быть от 1 до 3 включительно!")
        else:
            break

    return input_data, reshimost

while True:

    input_data, reshimost = get_input()

    coded = [fuck_that_shit(letter) for letter in list(input_data)]

    text = "".join(coded)

    print("Зашифрованные данные были записаны в файл output.txt!")
    print("\nРезультат:\n",text)

    with open("./output.txt", "w", encoding="UTF-8") as output:
        output.write(text)

    print()
    print("="*15)
    print("Нажмите enter, чтобы заново повторить")
    input("")
    print("\n\n")