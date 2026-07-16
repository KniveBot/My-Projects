# 01.01.20 12.00
# Врач 'А' время работы с 12:00 до 19:00 прием по 30 мин
import telebot

bot = telebot.TeleBot('1360036712:AAFBQ-5ixPjcM3zBKyyUQV5ppg3hdrxBm4w');

time = ['', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
        '18:00', '18:30']

time1 = '12:00'
time2 = '12:30'
time3 = '13:00'
time4 = '13:30'
time5 = '14:00'
time6 = '14:30'
time7 = '15:00'
time8 = '15:30'
time9 = '16:00'
time10 = '16:30'
time11 = '17:00'
time12 = '17:30'
time13 = '18:00'
time14 = '18:30'

keyboardTime = telebot.types.ReplyKeyboardMarkup()
keyboardTime.row(time[1],time[2],time[3],time4,time[5])
keyboardTime.row(time[6],time[7],time[8],time[9],time[10])
keyboardTime.row(time[11],time[12],time[13],time[14])

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start. Теперь выбери дату 01.01,20', reply_markup=keyboardTime)

day = 1
month = 2
year = 3


bot.polling()
