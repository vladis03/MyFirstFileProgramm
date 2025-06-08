def file_work_system():
    file_name=input("Имя файла:")

    while True: # Полная система режимов
        mode=input("Выберете один из трех режимов:\n" + 
              "a - Новый текст файла.\n" +
              "b - Добавление дополнительного текста в файл.\n" +
              "c - Для читания текста.\n" +
              "d - Выход из программы.\n" +
              "Вариант: ").lower().strip()
        
        if mode == "a":
            file = open(file_name, "w")
            file.write(input("Введите новый текст: "))
            file.close()

        elif mode == "b":
            file = open(file_name, "a")
            text = input("Дополнительный текст: ")

            while True: # Цикл для добавления пробела или перевода на новую строку перед текстом
                text_start_mode= input("Хотите отделить текст пробелом или переводом на новую строку?\n" +
                "a - Пробел\n" +
                "b - Перевод на новую строку\n" +
                "c - Ничего не делать\n" +
                "Вариант: ")

                if text_start_mode == "a":
                    text_start = " "
                    break

                if text_start_mode == "b":
                    text_start = "\n"
                    break

                if text_start_mode == "c":
                    text_start = ""
                    break

                else:
                    print("ОШИБКА:\n" +
                "Допустимы только 'a', 'b' или 'c'.\n" +
                "Попробуйте снова.")
                    continue

            full_text = text_start + text
            file.write(full_text)
            file.close()

        elif mode == "c":
            file = open(file_name, "r")
            print("Ваш полный текст:\n" +
                  file.read())
            
        elif mode == "d":
            break

        else:
            print("ОШИБКА:\n" +
            "Допустимы только 'a', 'b' 'c' или 'd'.\n" +
            "Попробуйте снова.")
            continue
    return 0

file_work_system() # Запуск программы
