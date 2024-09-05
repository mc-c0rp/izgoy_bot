
import telebot
from telebot.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from btrjsn import * # я не ебу что за хуйню ты написал
import data # вот это тема
import random
bot_token = '6616286894:AAFsF7jQRmcKP4DSPnk9glZtM0-A4pHJuJg' # 6980862082:AAHd5KK6o9UesZmcasSQ1xHlY0h_0Uv3QC4
bot = telebot.TeleBot(bot_token)
iZVgoida = [-1002212678084] #-1002156202800 изгои

MAX_PHOTO = 5 # ЛЁША НЕ ТРОГАЙ НАХУЙ УБЬЮ

state = {}

GBOGA = 'gboga'

JIRNIY_ID = 749205535

odmins = [1729435753] # сюда впиши ещё свой айди и якуба

bids = {
    "example": {
        "userid": 123123123,
        "photo_path": ['/temp/asdasd.png'],
        "caption": "asdasdasdasdasdas",
        "verif": "no"
    }
}

bids = data.load('bid', debug=True)

def chatBypass(message):
    chat_type = message.chat.type
    usid = message.chat.id  
    if chat_type in ['group', 'supergroup']:
        return
    if message.from_user.id == JIRNIY_ID:
        print('АААААААААА БЛЯТЬ ЖИРНЫЙ В БОТА ЗАШЁЛ СПАСАЙТЕСЬ КТО МОЖЕТ НАХУЙАААААААААААААААА БЛЯТЬ')
        ban_tmplate = 'перевес, сервер не выдерживает нагрузки'
        with open('nahui ee.MP4', 'rb') as video_file:
            bot.send_video(message.chat.id, video_file, caption=ban_tmplate)
        return 'no'
    else:
        return 'ok'
   
markupp = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
button0 = telebot.types.KeyboardButton(text="Подать заявку")
button1 = telebot.types.KeyboardButton(text="Пополнить баланс")
button2 = telebot.types.KeyboardButton(text="Очко Аллаха")
button3 = telebot.types.KeyboardButton(text="Випка")
markupp.add(button0)
markupp.add(button1, button3)
markupp.add(button2)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if chatBypass(message) == 'ok':
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
    if chatBypass(message) == 'ok':
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

# объявление
@bot.message_handler(func=lambda message: message.text == "Подать заявку")
def add(message):
    bot.send_message(message.chat.id, f"Окей, скинь фото (максимум {MAX_PHOTO}) и текст под фото (одним сообщением).")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    global bids
    if chatBypass(message) == 'ok':
        num_photos = len(message.photo)
        if num_photos == MAX_PHOTO:
            if message.caption:
                cap = message.caption
                photos = message.photo
                photo_path = []

                for index, img in enumerate(photos):
                    if index != 0:
                        if (index + 1) % 3 == 0:
                            temp_id = random.randint(0, 9999999999)
                            temp_path = img.file_id
                            print(f'{temp_path}.png успешно загружен')

                            photo_path.append(temp_path)
                    else:
                        temp_id = random.randint(0, 9999999999)
                        temp_path = img.file_id
                        print(f'{temp_path}.png успешно загружен')

                        photo_path.append(temp_path)

                while True:
                    bid_id = str(random.randint(0, 123123))
                    if bid_id in bids:
                        bid_id = str(random.randint(0, 123123))
                    else:
                        break

                bids[bid_id] = {
                    "userid": message.from_user.id,
                    "caption": cap,
                    "photo": photo_path,
                    "verif": 'no'
                }

                last = ''

                for photo in bids[bid_id]["photo"]:
                    if last != photo:
                        last = photo
                    else:
                        bids[bid_id]["photo"].remove(last)

                data.save('bid', bids, debug=True)

                markup = InlineKeyboardMarkup()
                button1 = InlineKeyboardButton("✅", callback_data=f"accept {bid_id}")
                button2 = InlineKeyboardButton("❌", callback_data=f"decline {bid_id}")
                button3 = InlineKeyboardButton("иди наху эээ", callback_data=f"ban {bid_id}")
                markup.add(button1, button2, button3)

                for adm in odmins:
                    bot.send_message(adm, f"Куку, ёпта.\nНовая заявка от {message.from_user.username}.")
                    for photo_id in bids[bid_id]["photo"]:
                        file_info = bot.get_file(photo_id)
                        file_path = file_info.file_path
                        bot.send_photo(adm, f'https://api.telegram.org/file/bot{bot_token}/{file_path}', caption=bids[bid_id]["caption"])
                    bot.send_message(adm, f"Что делаем?", reply_markup=markup)
            else:
                bot.reply_to(message, f"Ты забыл(а) написать текст под фото.")
        else:
            bot.reply_to(message, f"Слишком много фото, максимум {MAX_PHOTO}!")


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if 'accept' in call.data or 'decline' in call.data or 'ban' in call.data:
        dat = call.data
        dat = dat.replace('accept ', '')

        if dat in bids:
            for channel in iZVgoida:
                photo = bids[dat]['photo']
                bot.send_photo(channel, photo, caption=bids[dat]["caption"])
                bids[dat]['verif'] = 'yes'
        else:
            print(f'{bids}***\n{dat}')
            bot.answer_callback_query(call.id, "Поздно...")
        bot.answer_callback_query(call.id, "ok")
    elif 'decline' in call.data:
        dat = call.data
        dat = dat.replace('decline ', '')
        if dat in bids:
            bids[dat]['verif'] = 'yes'
            bot.answer_callback_query(call.id, "ok")


@bot.message_handler(func=lambda message: message.text == "Очко Аллаха")
def handle_input1(message):
    if chatBypass(message) == 'ok':
        usid = message.chat.id
        bot.send_message(usid, "Введи юзерайди/номер с плюсом/юзернейм без @:")
        state[usid] = GBOGA 

@bot.message_handler(func=lambda message: message.chat.id in state)
def handle_text_input(message):
    
    user_id = message.chat.id
    state = state.get(user_id)

    if state == GBOGA:
        try:
            zapros = message.text 
            if btr_readuserstat(user_id, "vip") == False:
                del state[message.chat.id]
                return
            
            template = f'''
номер: {btr_readbogstat(zapros, "number")}
юзерайди: {btr_readbogstat(zapros, "userid")}
юзернейм: {btr_readbogstat(zapros, "username")}
юзернейм1: {btr_readbogstat(zapros, "username1")}
'''
            bot.send_message(message.chat.id, template)
            del state[message.chat.id]
            
                
        except Exception:
            bot.send_message(message.chat.id, "нихуя не найдено")
            del state[message.chat.id]
            return
        
        


if __name__ == "__main__":
    bot.polling(none_stop=True)