import telebot
import random
import qrcode
from gtts import gTTS
from telebot import types
from email.mime import message

bot = telebot.TeleBot("5173449174:AAHqmOa_HuI0LQSvTg2CnteEn0XRbsXLjqE")

#/start
@bot.message_handler(commands=['start','Start'])
def send_welcome(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"سلام {myname}به بات من خوش اومدی❤")

#/help
@bot.message_handler(commands=['help','Help'])
def send_welcome(message):
    bot.reply_to(message,"""چه کمکی از دست من برمیاد؟!
    /Age
    /Fal
    /Game
    /Qrcode
    /Voice
    /Armax
    """)

#/age
@bot.message_handler(commands =['age','Age'])
def send_age(message):
    age_reply= bot.send_message(message.chat.id,f"سال تولد خود را وارد کنید.")
    bot.register_next_step_handler(age_reply,echo )
def echo(message):
     year = int(message.text)
     now = 1401 - year
     bot.send_message(message.chat.id,f"تواکنون {now} ساله هستی.")


#/fal
@bot.message_handler(commands =['fal','Fal'])
def send_welcome(message):
    fal_list =['در امتحانات نمره خوبی کسب خواهی کرد',
        'منتظر خبری هستی','به زودی پولی به دست شما میرسد','هوشیار و آگاه باش',
        'خطری از شما رفع خواهدشد','از موضوعی دلگیر هستی','به مهمانی دعوت خواهی شد',
        'یک خبرخوش میشنوی','به فنا خواهی رفت','به دیدار معشوق خواهی رفت']
    fal = random.choice(fal_list)
    bot.reply_to(message, fal)

#/game
@bot.message_handler(commands=['game','Game'])
def gaming(message):
    game_play = bot.send_message(message,"انتخاب کن یه عدد بین 1 تا 50 :")  
    bot.register_next_step_handler(game_play, p_game)
    
def p_game(message):
    rdm = random.randint(0,50)
    a = int(message.text)
    if rdm == a:
        bot.reply_to(message,'آفرین درست گفتی!😊 ')
    elif a < rdm:
        bot.reply_to(message,'عدد بزرگتر وارد کنید.')
    elif a > rdm:
        bot.reply_to(message,'عدد کوچکتر وارد کنید')

#/qrcode
@bot.message_handler(commands=['qrcode','Qrcode'])
def send_qr_string(message):
    qrcode = bot.send_message(message.chat.id, 'متن مورد نظر برای تبدیل را تایپ کنید.')
    bot.register_next_step_handler(qrcode, sendqr)
def sendqr(message):
    qrcode_img =  qrcode.make("message.text")
    qrcode_img.save('qr.png')
    photo = open('qr.png','rb')
    bot.send_photo(message.chat.id, photo)    


#/armax
@bot.message_handler(commands=['armax','Armax'])
def send_m(message):
    bot.reply_to(message, f"اعداد مورد نظر را وارد کنید.(در یک خط و با استفاده از <<,>> اعداد را جدا کنید)")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        array = message.text.split(",")
        arraynum = []
        for i in range(len(array)):
            arraynum.append(int(array[i]))
        MAX = max(arraynum)
        index_max = 0
        for i in range(len(arraynum)):
            if MAX == arraynum[i]:
                indexmax = i
        bot.send_message(message.chat.id,indexmax)

#/voice
@bot.message_handler(commands =['voice','Voice'])
def send_m(message):
    reply = bot.send_message(message.chat.id,".متن مورد نظر برای تبدیل را تایپ کنید")
    bot.register_next_step_handler(reply, send_voice)
def send_voice(message):
     voice = gTTS(message.text , slow=False)
     voice.save('voice.mp3')
     voice = open('voice.mp3', 'rb')
     bot.send_voice(message.chat.id, voice)





     

bot.infinity_polling()
