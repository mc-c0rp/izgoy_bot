
import telebot
from btrjsn import *
bot_token = '6980862082:AAHd5KK6o9UesZmcasSQ1xHlY0h_0Uv3QC4'
bot = telebot.TeleBot(bot_token)
iZVgoida = -1002156202800

STATE = {}

GBOGA = 'gboga'

def chatBypass(message):
    chat_type = message.chat.type
    usid = message.chat.id  
    if chat_type in ['group', 'supergroup']:
        return
    if message.chat.id == 749205535:
        ban_tmplate = '''
Вы забанены по причине:
покупка, установка, продажа, распространение ЦП
чтоб разбаниться, напишите нашей тех поддержке @Wnansjzjjkl

+ ограничение по весу: 60кг(разраб функции АНТИНИКИТА исключение)
'''
        bot.send_message(749205535, ban_tmplate)
        return
   
markupp = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
button0 = telebot.types.KeyboardButton(text="Подать объявление")
button1 = telebot.types.KeyboardButton(text="Пополнить баланс")
button2 = telebot.types.KeyboardButton(text="Очко Аллаха")
button3 = telebot.types.KeyboardButton(text="Випка")
markupp.add(button0)
markupp.add(button1, button3)
markupp.add(button2)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chatBypass(message)
    usid = message.chat.id 
    user_example = {
        "balance" : 0,
        "verified" : False,
        "vip" : False
    }
    btr_createuserprofile(usid, user_example)
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_phone = telebot.types.KeyboardButton(text="Подтвердить аккаунт", request_contact=True)
    markup.add(button_phone)
    if btr_readuserstat(usid, "verified") == False:
        bot.send_message(message.chat.id, "Чтобы зарегаться, ебашь сюда свой номер(данные не сохраняются)", reply_markup=markup)
    else:
        bot.send_message(usid, "дарова", reply_markup=markupp)

@bot.message_handler(content_types=['contact'])
def receive_contact(message):
    chatBypass(message)
    phone_number = message.contact.phone_number
    chat_id = message.chat.id
    bog_example = {
        "number" : phone_number,
        "userid" : chat_id,
        "username" : message.from_user.username,
        "username1" : message.from_user.first_name
    }
    btr_createbogprofile(phone_number, bog_example)
    btr_createbogprofile(chat_id, bog_example)
    btr_createbogprofile(message.from_user.username, bog_example)
    btr_changeuserstat(chat_id, "verified", True)
    bot.send_message(chat_id, "Авторизован ебать", reply_markup=markupp)

    

@bot.message_handler(func=lambda message: message.text == "Очко Аллаха")
def handle_input1(message):
    chatBypass(message)
    usid = message.chat.id
    bot.send_message(usid, "Введи юзерайди/номер с плюсом/юзернейм без @:")
    STATE[usid] = GBOGA 

@bot.message_handler(func=lambda message: message.chat.id in STATE)
def handle_text_input(message):
    
    user_id = message.chat.id
    state = STATE.get(user_id)

    if state == GBOGA:
        try:
            zapros = message.text 
            if btr_readuserstat(user_id, "vip") == False:
                del STATE[message.chat.id]
                return
            
            template = f'''
номер: {btr_readbogstat(zapros, "number")}
юзерайди: {btr_readbogstat(zapros, "userid")}
юзернейм: {btr_readbogstat(zapros, "username")}
юзернейм1: {btr_readbogstat(zapros, "username1")}
'''
            bot.send_message(message.chat.id, template)
            del STATE[message.chat.id]
            
                
        except Exception:
            bot.send_message(message.chat.id, "нихуя не найдено")
            del STATE[message.chat.id]
            return
        
        


if __name__ == "__main__":
    bot.polling(none_stop=True)