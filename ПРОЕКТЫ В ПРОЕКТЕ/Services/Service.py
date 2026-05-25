keys = ["I232S-2DJ32-3ISJM-33MAK-MAKS",
        "I2VGH-W72HK-3HJKK-TELEG-DJ2K",
        "3JHJJ-2T8AS-23BJK-2YDSA-28UH",
        "FJWLT-SJ2AS-DJ2LD-ALWV1-PYTH"]

# ввод ключа
key = input("Введите ключ активации >>> ")

if key in keys:
    print("Ключ активации верный!")
    print("Открытие...")
    print(" ")
    print("Service")
    print(" ")
    print("1. Ответы в тесте")
    print("0. Выход")
    print("Введите число в мод меню")

    while True:
        a = int(input(">>> "))

        if a == 1:
            print("1. Ответ 4")
            print("2. Кровь")
            print("3. Дядюшка конгрегейшн или дядюшка конгредион")

        elif a == 0:
            break
else:
    print("Ключ активации неправильный!")