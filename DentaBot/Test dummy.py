import telebot

bot = telebot.TeleBot('1360036712:AAFBQ-5ixPjcM3zBKyyUQV5ppg3hdrxBm4w');
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет')
keyboard1.row('Пока')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Почему')
keyboard2.row('Лень')

vvod = 0

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message, vvod):
    if message.text.lower() == 'привет':
        vvod += 1
        bot.send_message(message.chat.id, 'Привет, мой создатель', reply_markup=keyboard2)
    elif message.text.lower() == 'пока':
        vvod += 2
        bot.send_message(message.chat.id, 'Прощай, создатель', reply_markup=keyboard2)




def send_exxuse(message, vvod):
    if message.text.lower() == 'почему':
        bot.send_message(message.chat.id, 'Захотелось')
        vvod += 1
    elif message.text.lower() == 'Лень':
        bot.send_message(message.chat.id, 'Одна из 7 смертных....')
        vvod += 2

def exit_text(message, vvod):
    bot.send_message(message.chat.id, vvod)


bot.polling()