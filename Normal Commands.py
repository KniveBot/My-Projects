
date = '01.01.20 16:30'
date += ' '
k = ''

day = 0
month = 0
year = 0
hour = 0
minute = 0

count = 0

for i in date:
    if i.isdigit():
        k = k + str(i)
    else:
        if count == 0:
            day = k

        if count == 1:
            month = k

        if count == 2:
            year = k

        if count == 3:
            hour = k

        if count == 4:
            minute = k

        count += 1
        k = ''
count = 0

print('День:', day, 'Месяц:', month, 'Год:', year, 'Час:', hour, 'Минута:', minute)

time = ['12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']

vvk = ''
vvCount = 0

vvHour = 0
vvMinute = 0

for i in range(len(time)):
    time[i] += ' '
    for j in time[i]:
        if j.isdigit():
            vvk = vvk + str(j)
        else:
            if vvCount == 0:
                vvHour = vvk

            if vvCount == 1:
                vvMinute = vvk

            vvCount += 1
            vvk = ''
    vvCount = 0

    if hour == vvHour and minute == vvMinute:
        time[i] = ' - '

print('Час:', vvHour, 'Минута:', vvMinute)
print(time)





