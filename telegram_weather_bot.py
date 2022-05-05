# import config
# import telebot
# import requests
# from telebot import types
# from bs4 import BeautifulSoup as BS

token = '5140464978:AAEzdjCz_2a_M-yFtRpH95mMJ6E44A9oivs'
bot = telebot.TeleBot(token)

# Privatbank API
url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

response = requests.get(url).json()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🌤Погода')
    itembtn2 = types.KeyboardButton('💲Курс долара')
    markup.add(itembtn1, itembtn2)

    msg = bot.send_message(message.chat.id, "Выберите:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_step)

def process_select_step(message):
    try:
        if (message.text == '💲Курс долара'):
            coins(message)
        elif (message.text == '🌤Погода'):
            weather(message)
        else:
            send_welcome(message)

    except Exception as e:
       bot.reply_to(message, 'ooops!')

# Погода
def weather(message):
    r = requests.get('https://sinoptik.ua/одесса')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    # убрать клавиатуру
    markup = types.ReplyKeyboardRemove(selective=False)

    bot.send_message(message.chat.id, "Привет, погода на сегодня:\n" +
        t_min + ', ' + t_max + '\n' + text, reply_markup=markup)

# Курсы валют
def coins(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('USD')
    itembtn2 = types.KeyboardButton('EUR')
    markup.add(itembtn1, itembtn2)

    msg = bot.send_message(message.chat.id,
                    "Узнать наличный курс ПриватБанка (в отделениях)", reply_markup=markup)
    bot.register_next_step_handler(msg, process_coin_step)

def process_coin_step(message):
    try:
       # убрать клавиатуру
       markup = types.ReplyKeyboardRemove(selective=False)

       for coin in response:
           if (message.text == coin['ccy']):
              bot.send_message(message.chat.id, printCoin(coin['buy'], coin['sale']), 
                               reply_markup=markup, parse_mode="Markdown")

    except Exception as e:
       bot.reply_to(message, 'ooops!')

def printCoin(buy, sale):
    '''Вывод курса пользователю'''
    return "💰 *Курс покупки:* " + str(buy) + "грн" + "\n💰 *Курс продажи:* " + str(sale) + "грн"

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)