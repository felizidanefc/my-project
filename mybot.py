import telebot

bot = telebot.TeleBot("635333939:AAHPDBHRhzELzbRBsrG6PfeXHUiXGIZm1xc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Bienvenido shur, al BOT de RotoCoches")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "No te entiendo")
print("El bot se ha ejecutado correctamente")
bot.polling()
