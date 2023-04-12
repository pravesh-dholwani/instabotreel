from instascrape import Reel
import telebot
import requests
import os
import re
import instaloader


bot = telebot.TeleBot("6264361604:AAFTop0Ofs3Oq00yltdfA-8Mngcm8rdSpm8")

@bot.message_handler(['start' , 'hello'])
def send_welcome_message(message):
    print(message.from_user.username)
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id , text ="Welcome\nNow you can download reel through this bot only.\nJust paste the link (only public accounts)\n")
    # bot.reply_to(message , "Welcome\n Now you can download reel through this bot only.\n Just paste the link (only public accounts)\n")
    bot.send_message(chat_id = chat_id , text ="Reel ke Shaukeens")

@bot.message_handler(func=lambda msg:True)
def send_to_sender(message):
    print(message.from_user.username)
    try:
        # reel_url = 'https://www.instagram.com/reel/Cccgd2MFCs4/'
        reel_url = message.text
    # Create an instance of the Instaloader class
        L = instaloader.Instaloader()

    # Download the Reel video
        post = instaloader.Post.from_shortcode(L.context, reel_url.split('/')[-2])
        video_file = post.video_url
        response = requests.get(video_file)
        reel_bytes = response.content
        bot.reply_to(message , "Hi " + message.from_user.first_name + " Sending reel wait for 2 mins")
        # print("sending file")

        bot.send_video(chat_id=message.chat.id , video=reel_bytes , timeout=300)
    except Exception as e:
        bot.reply_to(message , "Either your message is not a reel link or it is private")
    # with open(video_file, 'rb') as f:
    #     reel_bytes = f.read()
    #     bot.send_video(chat_id=message.chat.id , video=reel_bytes)



try:
    bot.infinity_polling()
except Exception as e:
    print("BOT ALREADY STARTED")
# print("bot started")

