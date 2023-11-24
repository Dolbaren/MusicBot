from django.core.management.base import BaseCommand
import telebot
from music.models import Music

bot = telebot.TeleBot("6708394844:AAF7AmPFxqWuNv2HHsisnuOUKJ4KWgZ2Jb4")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['music'])
def music(message):
    musics = Music.objects.all()
    for music in musics:
        bot.send_message(message.chat.id, f"Song:{music.name}, Artist:{music.artist}")
        
class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.from_user.id, "Введи название песни")
    bot.register_next_step_handler(message, title_handler)

def title_handler(message):
    global title
    title = message.text

    bot.send_message(message.chat.id, "Напишите Исполнителя")
    bot.register_next_step_handler(message, artist_handler)

def artist_handler(message):
    global artist
    artist = message.text
    bot.send_message(message.chat.id, f"Спасибо!")
    new_music = Music.objects.create(name=title, artist=artist)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"help: /start, /music, /add")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
