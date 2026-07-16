import telebot;

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google
gscope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
gcredentials = 'creds.json'
gdocument = 'Denta Bot List'

bot = telebot.TeleBot('1360036712:AAFBQ-5ixPjcM3zBKyyUQV5ppg3hdrxBm4w');

name = '';
phone = '';
dName = '';
usluga = '';
date = ' ';

# Doctor Name
keyboardStart = telebot.types.ReplyKeyboardMarkup()
keyboardStart.row('/start')

keyboardDname = telebot.types.ReplyKeyboardMarkup()
keyboardDname.row('Anna')
keyboardDname.row('Merry')
keyboardDname.row('Henry')

keyboardUsluga = telebot.types.ReplyKeyboardMarkup()
keyboardUsluga.row('Лечение зубов')          #1
keyboardUsluga.row('Протезирование зубов')   #2
keyboardUsluga.row('Установка брекетов')     #3
keyboardUsluga.row('Профессиональная чистка')#4
keyboardUsluga.row('Отбеливание зубов')      #5


@bot.message_handler(content_types=['text'])
@bot.message_handler(send_message=['text'])

def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Введите ФИО");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю. Напиши /start для начала регистрации.');


def get_name(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id,'Вы уже начали регистрацию пожалуйста введите свое ФИО')
        bot.register_next_step_handler(message, get_name);
        get_name(message)
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Введите телефон');
    bot.register_next_step_handler(message, get_phone);


def get_phone(message):
    global phone;
    phone = message.text;
    bot.send_message(message.from_user.id, 'Введите имя доктора', reply_markup=keyboardDname);
    bot.register_next_step_handler(message, get_dName);


def get_dName(message):
    global dName;
    dName = message.text;
    bot.send_message(message.from_user.id, 'Введите услугу', reply_markup=keyboardUsluga);
    bot.register_next_step_handler(message, get_usluga);


def get_usluga(message):
    global usluga;
    usluga = message.text;
    bot.send_message(message.from_user.id, 'Введите дату 01.01.20');
    bot.register_next_step_handler(message, get_date);


def get_date(message):
    global date;
    date = message.text
    add_to_gsheet(name, phone, dName, usluga, date)

    bot.send_message(message.from_user.id,
                     'Имя: ' + name + ' Телефон: ' + phone + ' Имя доктора: ' + dName + ' Услуга: ' + usluga + ' Дата: '
                     + date + '.')
    bot.send_message(message.from_user.id, 'Чтобы начать запись введите /start', reply_markup=keyboardStart);


# Запись в Google Sheet
def add_to_gsheet(name, phone, dname, usluga, date):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(gcredentials, gscope)
    gc = gspread.authorize(credentials)
    wks = gc.open(gdocument).sheet1
    wks.append_row(
        [name, phone, dname, usluga, date])


add_to_gsheet(name, phone, dName, usluga, date)

bot.polling(none_stop=False, interval=0)
