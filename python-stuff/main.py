import telebot
import os
import random

bot = telebot.TeleBot("TOKEN")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Hello, how are you?")

@bot.message_handler(commands=['what'])
def send_test(message):
    bot.reply_to(message, "Go touch some grass loser")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['yo'])
def send_yo(message):
    bot.reply_to(message, "Yo, What's Up!")

@bot.message_handler(commands=['heh'])

def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Commands: /start , /hello , /bye , /what , /mem , /help , /yo , /heh [enter a number] (click any of these to test!)")


@bot.message_handler(commands=['mem'])
def mem(message):
    script_dir = os.path.dirname(__file__)
    img_name = random.choice(os.listdir('images'))  # Случайным образом выбираем изображение
    file_path = os.path.join(script_dir, 'images', img_name)
    with open(file_path, 'rb') as f:
        bot.send_photo(message.chat.id, f)   

bot.polling()


