from flask import Flask,request
from telebot import types, TeleBot
from dotenv import load_dotenv
import subprocess,os 

load_dotenv()
TOKEN = os.environ.get('TOKEN')
bot = TeleBot(TOKEN)
app = Flask(__name__)




def calling_app():

    app = Flask(__name__)
    @app.route("/")
    def index():
        return "hello world from Termux !" 



    @bot.message_handler(commands=['start'])
    def start(message):
        msg = 'for test call from Android Termux send\n /call <phone number> with start 05 Only\n Example:\n /call ' + os.environ.get('PHONE_NUMBER')
        bot.send_message( message.chat.id,msg)
        # user_id = message.chat.id
        # username = message.from_user.username
        # first_name = message.from_user.first_name
        # last_name = message.from_user.last_name
        # if  check_user(int(user_id)) :
        #     add_user(user_id,username,first_name,last_name)

        #     bot.send_message(message.from_user.id,"Welcome " + first_name)
        # else:
        #     bot.send_message(message.from_user.id,"welcome Back " + first_name)
    @bot.message_handler(commands=['call'])
    def call(message):
        number = message.text[str(message.text).index('0'):]
        bot.send_message(message.chat.id,'number to call is: \n'+number)
        init_call = subprocess.call(f'termux-telephony-call '+number,shell=True)
        bot.send_message(message.chat.id,'number to call is: ')

    @app.route('/', methods=['POST'])
    def getMessage():
        json_string = request.get_data().decode('utf-8')
        update = types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200

    @bot.message_handler(commands=['help'])
    def help(message):
        bot.reply_to(message, 'please send /start to see ' + message.from_user.first_name)


    #to set WebHook
    @app.route("/webhook",methods=["POST",'GET'])
    def webhook():
        url_https = str(request.url_root)
        print(url_https)
        bot.remove_webhook()
        bot.set_webhook(url=url_https)
        return url_https
        
        
    return app

