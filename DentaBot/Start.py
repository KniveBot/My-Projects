print("Здравствуйте напишите Запись, чтобы начать")
vvod = str(input())
if vvod == "Запись":
    print("Введите имя")
    name = str(input())
    if name != 0:
        print("Введите телефон")
        phoneN = str(input())
        if phoneN != 0:
            print("Введите имя доктора")
            dName = str(input())
            if dName != 0:
                print("Введите услугу")
                usluga = str(input())
                if usluga != 0:
                    print("Введите дату и время(01.01.10 11.00)")
                    date = str(input())
        
a = [0,0,0,0,0]
a[0] = name
a[1] = phoneN
a[2] = dName
a[3] = usluga
a[4] = date

if date != 0:
    print("Для просмотра введенной информации напишите График, а если вам это не требуется напишите Завершить")
    vvod = str(input())
    if vvod == "График":
        print(a)
    elif vvod == "Завершить":
        print("Ваша запись будет одобрена в ближайшее время.Спаибо, что выбрали нас.")
    else:
        print("Повторите ввод")