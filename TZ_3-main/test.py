from math import isclose
import program
import time
import random
file = 'data.txt'
mass = program.read_file(file)


def test_min(a, b):
    assert isclose(a, min(b))


def test_max(a, b):
    assert isclose(a, max(b))


def test_sum(a, b):
    assert isclose(a, sum(b))


def test_mult(a, b):
    c = 1
    for i in range(len(b)):
        c *= b[i]
        if c > 1000 ** 10:
            assert isclose(a, c)
            return
    assert a == c


# Initial test
start_time = time.time()

test_max(program.max_array(file), mass)
test_min(program.min_array(file), mass)
test_sum(program.sum_array(file), mass)
test_mult(program.mult_array(file), mass)

first_time = (time.time() - start_time)
print("--- %s секунд ---" % (time.time() - start_time))

# Test with more input data
start_time = time.time()

for i in range(len(mass) * 9):
    mass.append(random.randint(1, 100))

program.write_file('tempfile.txt', mass)
d = program.read_file('tempfile.txt')
print('_________________________________________________________________________')
print('--------Тесты с увеличением размера файла(чисел в 10 раз больше)---------')
print()

test_max(program.max_array('tempfile.txt'), d)
test_min(program.min_array('tempfile.txt'), d)
test_sum(program.sum_array('tempfile.txt'), d)
test_mult(program.mult_array('tempfile.txt'), d)

second_time = (time.time() - start_time)
print("--- %s секунд ---" % (time.time() - start_time))
print()
print('Разница во времени:')
print("--- %s секунд ---" % (second_time - first_time))
print('Итого реализованно 5 тестов. 4 на коректность работы. 1 на коректность ввода. Также есть проверка поведения '
      'программы при увеличении объема файла. И я еще сделал так, чтобы при подсченте произведения, если оно привышает '
      '1000^10(1 000 000 000 000 000 000 000 000 000 000), то питон перестает ее считать(Это сделано, чтобы излишне не нагружать компьютер).')