str_polz_1 = input("Введите первую строку: ") # Запрос певрой строки от пользователя
str_polz_2 = input("Введите вторую строку: ") # Запрос второй строки от пользователя

str_polz_1 = sorted(str_polz_1.lower()) # Присваивание сортированного значения
str_polz_2 = sorted(str_polz_2.lower()) # Присваивание сортированного значения

if str_polz_1 == str_polz_2: # Сравнение 
    print("Эти строки являются анограммами.") # Вывод результата на экран
else: # Сработает при разных строках
    print("Эти строки не являются анограммами.") # Вывод результата на экран

