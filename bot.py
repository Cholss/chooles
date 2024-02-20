import telebot;
bot = telebot.TeleBot('%ваш токен%')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    @bot.message_handler(content_types=['text', 'document', 'audio'])
