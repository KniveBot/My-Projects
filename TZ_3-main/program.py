def read_file(input):
    a = []
    with open(input, 'r') as f:
        for line in f.readlines():
            try:
                a += list(map(int, line.split()))
            except ValueError:
                exit('Найдены непонятные символы в файле. Работа программы аварийно прекращена.')
                return ValueError
    return a


def sum_array(input):
    s = 0
    arr = read_file(input)
    for i in range(len(arr)):
        s += arr[i]
    print("В файле:")
    print(*arr)
    print("Сумма:", s)
    print()
    return s


def mult_array(input):
    arr = read_file(input)
    mult = 1
    for i in arr:
        mult *= i
        if mult > 1000 ** 10:
            print("В файле:")
            print(*arr)
            print("Произведение привышает 1000^10. Процесс остановлен.")
            print()
            return mult
    print("В файле:")
    print(*arr)
    print("Произведение:", mult)
    print()
    return mult


def min_array(input):
    arr = read_file(input)
    mi = arr[0]
    for i in range(len(arr)):
        if arr[i] < mi:
            mi = arr[i]
    print("В файле:")
    print(*arr)
    print("Минимальное: ", mi)
    print()
    return mi


def max_array(input):
    arr = read_file(input)
    ma = arr[0]
    for i in range(len(arr)):
        if arr[i] > ma:
            ma = arr[i]
    print("В файле:")
    print(*arr)
    print("Максимальное: ", ma)
    print()
    return ma


def write_file(input, arr):
    with open(input, 'w') as f:
        for i in arr:
            f.write(str(i) + " ")


def write_file(input, arr):
    with open(input, 'w') as f:
        for i in arr:
            f.write(str(i) + " ")
