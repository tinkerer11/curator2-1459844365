from telebot import TeleBot

bot = TeleBot("7606947435:AAHHeLytPWPr8jOQ52lQ4HB2V-YDF8QQxe8")

#Начало-старт
@bot.message_handler(commands=["start"])
def botic(message):
    bot.send_message(message.chat.id,"Привет! Давай приступим к работе.")

#Узнать контакты
@bot.message_handler(commands=["contact"])
def boti(message):
    bot.send_message(message.chat.id,"По всем интересущим вопросам обращайтесь к @hl0z3k_manager")

#Просто предложка
@bot.message_handler(commands=["predloshka"])
def bot1(message):
    bot.send_message(message.chat.id,"Пожалуйста, отправьте фото или текст, которые будут опубликованы после проверки модератором")

#Жалоба и предложение
@bot.message_handler(commands=["shaloba"])
def bot2(message):
    bot.send_message(message.chat.id,"Пожалуйста, напишите подробный и обоснованный текст о том, как улучшить контент. Благодарю за обратную связь!")

#Анонимный вопрос
@bot.message_handler(commands=["anonim"])
def bogkf(message):
    bot.send_message(message.chat.id,"Задайте вопрос, и в ближайшее время я на него отвечу. Не переживайте, ваш вопрос останется анонимным.")

bot.infinity_polling()