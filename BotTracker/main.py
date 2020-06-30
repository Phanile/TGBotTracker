import telebot
import config
import screen

bot = telebot.TeleBot(config.TOKEN)
telebot.apihelper.proxy = {'https' : 'socks5://96.113.176.101:1080'}

@bot.message_handler(commands = ['shot'])
def send_screen(message):
    screen.take_screenshot()
    bot.send_photo(message.chat.id, photo = open(screen.path, 'rb'))

bot.polling(none_stop = True)