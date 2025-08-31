import telebot
import os
import yt_dlp

bot = telebot.TeleBot("8411105955:AAEIJSvG-eZPVB3e0jHZQSkfNlUP5tXG_eg")

@bot.message_handler(commands=['start'])
def bienvenida(message):
    bot.reply_to(message, "¡Hola! Envíame un enlace de YouTube y te descargaré el video.")

@bot.message_handler(func=lambda message: True)
def descargar_video(message):
    video_link = message.text
    ydl_opts = {'outtmpl': '%(id)s.%(ext)s'}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_link, download=True)
            video_path = ydl.prepare_filename(info)
        with open(video_path, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)
        os.remove(video_path)
    except Exception as e:
        bot.reply_to(message, "Oops, algo salió mal descargando el video.")

bot.polling()
