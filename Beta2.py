#! /usr/bin/env python
#-*-coding:utf-8-*-


import time
from grab import Grab
import telebot
from telebot import types
import threading
import random
import feedparser
import re

import requests
import random  as  random_number
import urllib.request, urllib.parse,urllib
import urllib.request



from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


token = '376121237:AAEa4q5bt9PKh32Cb6JAtXRy5It7XGD-8Oo'
#token = '345342479:AAGc-uFkYtrsUHYgzBbG8uNdHof8m2evGF0'

bot = telebot.TeleBot(token)

bot2 = ChatBot(name="Robby",
                    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                    filters=["chatterbot.filters.RepetitiveResponseFilter"],
                    database="./database.json"
                    )



#bot2.set_trainer(ChatterBotCorpusTrainer)
#bot2.train("corpus", "chatterbot.corpus.russian")
print("Обучение завершено")

news_rss = feedparser.parse('https://meduza.io/rss/all')




@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False) # False - исчезновение клавы после нажатия
        user_markup.row('Погода','Новости')
        user_markup.row('Записки')
        bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=user_markup)









ttime = int(time.strftime('%H'))

#str = 'поставь таймер на 5 минут'








@bot.message_handler(content_types=['text'])
def handle_text(message):
        message.text  = message.text.lower()



        if "привет" in  message.text:

            if ttime == 6 or ttime == 7 or ttime == 8 or ttime == 9 or ttime == 10 or ttime == 11:
                print('Доброе утро')
                bot.send_message(message.chat.id, 'Доброе утро')
            elif ttime == 12 or ttime == 13 or ttime == 14 or ttime == 15 or ttime == 16 or ttime == 17:
                print('Добрый день')
                bot.send_message(message.chat.id, 'Добрый день')
            elif ttime == 18 or ttime == 19 or ttime == 20 or ttime == 21 or ttime == 22:
                print('Добрый вечер')
                bot.send_message(message.chat.id, 'Добрый вечер')



        if "как дела" in  message.text:
            print('Спасибо всё хорошо а у вас? — очень приятно-до свидания')
            bot.send_message(message.chat.id, 'Спасибо всё хорошо а у вас? — очень приятно-до свидания')

        if "ты как" in  message.text:
            print('Как Скрудж Макдак')
            bot.send_message(message.chat.id, 'Как Скрудж Макдак')


        if "привет" in  message.text or "здарова" in  message.text:
            print(time.strftime('%H:%M:%S'))


        if "анекдот" in  message.text:
                g = Grab()
                g.go('http://eku.ru/category/aforism/')
                time.sleep(0.5)
                rand = random.randint(1, 22)
                print(rand)
                if g.doc.select('//*[@id="content"]/div[3]/div[1]/div[{}]/div[2]/p[2]'.format(rand)).exists():
                    Check1 = g.doc.select('//*[@id="content"]/div[3]/div[1]/div[{}]/div[2]/p[2]'.format(rand)).text()
                    print(Check1)
                    bot.send_message(message.chat.id, '{}'.format(Check1))
                else:
                    print('Not Found')



        if "когда" in  message.text or "сколько" in  message.text and "закат" in  message.text:
                g = Grab()
                g.go('https://www.google.ru/search?q=когда закат в екатеринбурге')
                time.sleep(0.5)
                if g.doc.select('//*[@id="rso"]/div[1]/div/div/div/div/div[1]').exists():
                    Check1 = g.doc.select('//*[@id="rso"]/div[1]/div/div/div/div/div[1]').text()
                    print(Check1)
                    bot.send_message(message.chat.id, '{}'.format(Check1))

                else:
                    print('Not Found')

        if "когда" in  message.text or "сколько" in  message.text and "восход" in  message.text:
                g = Grab()
                g.go('https://www.google.ru/search?q=когда восход в екатеринбурге')
                time.sleep(0.5)
                if g.doc.select('//*[@id="rso"]/div[1]/div/div/div/div/div[1]').exists():
                    Check1 = g.doc.select('//*[@id="rso"]/div[1]/div/div/div/div/div[1]').text()
                    print(Check1)
                    bot.send_message(message.chat.id, '{}'.format(Check1))
                else:
                    print('Not Found')


        if "спой" in  message.text and "песню" in  message.text:
            print('Давайте петь вместе, вы вслух, а я про себя')
            bot.send_message(message.chat.id, 'Давайте петь вместе, вы вслух, а я про себя')




        if "таймер" in  message.text:
            id = ''.join(filter(lambda x: x.isdigit(), "{}".format( message.text)))
            print(id)

            if "секунд" in  message.text:
                msg = 'Прошло {} секунд'.format(id)
                ids = message.chat.id
                timer1 = threading.Timer(int(id), count, args=[msg,ids])
                timer1.start()
            if "минут" in  message.text:
                msg = 'Прошло {} минут'.format(id)
                ids = message.chat.id
                timer1 = threading.Timer(int(id)*60, count, args=[msg,ids])
                timer1.start()
            if "час" in  message.text:
                print('таймер можно установить только на секунды или минуты')


        if "крым" in  message.text:
            print('крым наш')
            bot.send_message(message.chat.id, 'крым наш')


        if "кто ты" in  message.text:
            print('я, искусственный интелект Jarvis')
            bot.send_message(message.chat.id, 'я, искусственный интелект Jarvis')

        if "В чем смысл жизни" in  message.text:
            print('В жизни')
            print('Смысл жизни.. в шоколаде. ну или жизнь в шоколаде')
            bot.send_message(message.chat.id, 'В жизни')


        if "кто тебя" in  message.text:
            print('Меня создал.. великий человек.. мудрец, филантроп, про геймер, тащер, секси')
            bot.send_message(message.chat.id, 'Меня создал.. великий человек.. мудрец, филантроп, про геймер, тащер, секси')

        if "фото" in  message.text:

            ids = message.chat.id
            msg = message.text
            pic(ids,msg,rand = 1)



        if "видео" in  message.text:

            ids = message.chat.id
            msg = message.text
            video(ids,msg,rand = 1)




        if "как" in  message.text and "думаешь" in  message.text:
            print('Я не думаю.')
            bot.send_message(message.chat.id, 'Я не думаю..')

        if "кто такой" in message.text or "кто такая" in message.text or "что такое" in message.text or "фильм" in message.text or "сериал" in message.text:


            ids = message.chat.id
            say0 = message.text.replace('кто такой', '')
            pic(ids, say0, rand=0)
            time.sleep(0.2)

            g = Grab(log_file='out2.html')
            #g = Grab()
            g.go('https://yandex.ru/search/?lr=54&text={}'.format(message.text))

            time.sleep(0.5)

            if g.doc.select('//span[@class="cut2__visible"]').exists():  # кто такой
                sms1 = g.doc.select('//span[@class="cut2__visible"]').text()

                bot.send_message(message.chat.id, sms1)

                if g.doc.select('//tr[@class="table__row"]').exists():  # кто такой
                    sms1 = g.doc.select('//tr[@class="table__row"]').text()
                    print(sms1)
                    bot.send_message(message.chat.id, sms1)

                g = Grab()
                g.go('https://www.google.ru/search?q={}'.format(message.text))
                time.sleep(0.2)
                if g.doc.select('//cite[@class="_Rm"]').exists():  # кто такой
                    sms1 = g.doc.select('//cite[@class="_Rm"]').text()
                    print(sms1)

                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="Трейлер", callback_data="tryler")
                callback_button2 = types.InlineKeyboardButton(text="Смотреть онлайн", url=sms1)
                keyboard.add(callback_button)
                keyboard.add(callback_button2)
                bot.send_message(message.chat.id, "{}".format(message.text), reply_markup=keyboard)


            else:
                print('Not found')
                if g.doc.select('//span[@class="text-cut2 typo typo_text_m typo_line_m"]').exists():  # кто такой
                    sms1 = g.doc.select('//span[@class="text-cut2 typo typo_text_m typo_line_m"]').text()
                    #say1 = sms1.replace('Википедия Читать дальше', ' Википедия')
                    bot.send_message(message.chat.id, sms1)

                else:
                    print('Not found chto')
                    if g.doc.select('//div[@class="fact__description"]').exists():  # кто такой
                        sms1 = g.doc.select('//div[@class="fact__description"]').text()
                        print(sms1)
                        #    new = re.sub(r'[A-z\d]+', r'', "{}".format(sms1)).strip()
                        bot.send_message(message.chat.id, sms1)
                    else:
                        print('Not found chto')
                        if g.doc.select('//div[@class="fact-answer fact-answer_size_m fact__answer"]').exists():  # кто такой
                            sms1 = g.doc.select('//div[@class="fact-answer fact-answer_size_m fact__answer"]').text()
                            print(sms1)
                            #   new = re.sub(r'[A-z\d]+', r'', "{}".format(sms1)).strip()
                            bot.send_message(message.chat.id, sms1)
                        else:
                            print('Not found chto')
                            if g.doc.select('//div[@class="fact-answer fact-answer_size_s fact__answer"]').exists():  # кто такой
                                sms1 = g.doc.select('//div[@class="fact-answer fact-answer_size_s fact__answer"]').text()
                                print(sms1)
                                # new = re.sub(r'[A-z\d]+', r'', "{}".format(sms1)).strip()
                                bot.send_message(message.chat.id, sms1)
                            else:
                                print('Not found chto')
                                if g.doc.select('.//h1').exists():  # кто такой
                                    sms1 = g.doc.select('.//h1').text()
                                    if ('ой…' in sms1):
                                        print('Captcha!')
                                        bot.send_message(message.chat.id, 'Captcha!')
                                        if g.doc.select('//img/@src').exists():  # кто такой
                                            sms1 = g.doc.select('//img/@src').text()
                                            print(sms1)

        if "капча" in message.text:
            say1 = message.text.replace('… ', '...')


            g = Grab(log_file='captcha.html')
            g.go('https://yandex.ru/search/?lr=54&msid=1490110913.97055.20941.7765&text=hello')
            if g.doc.select('.//h1').exists():  # кто такой
                sms1 = g.doc.select('.//h1').text()
                if ('ой…' in sms1):
                    print('Captcha!')
                    bot.send_message(message.chat.id, 'Captcha!')
                    if g.doc.select('//img/@src').exists():  # кто такой
                        sms1 = g.doc.select('//img/@src').text()
                        print(sms1)



                        print(say1)


                        g.doc.set_input_by_id('rep', '{}'.format(say1))
                        g.doc.submit()

        if "погода" in message.text:
            g = Grab()
            g.go('https://yandex.ru/pogoda/yekaterinburg/details?lat=56.83174&lon=60.535361&name=улица+Рабочих%2C+Екатеринбург&kind=street')
            time.sleep(0.5)

            if "завтра" in message.text:
                if g.doc.select('/html/body/div[2]/div[2]/div[2]/div[2]/dl/dd[1]/table/tbody/tr[1]/td[1]/div[2]').exists() or g.doc.select('/html/body/div[2]/div[2]/div[2]/div[2]/dl/dd[1]/table/tbody/tr[1]/td[1]/div[2]').exists():
                    str = g.doc.select('/html/body/div[2]/div[2]/div[2]/div[2]/dl/dd[1]/table/tbody/tr[1]/td[1]/div[2]').text()
                    str2 = g.doc.select('/html/body/div[2]/div[2]/div[2]/div[2]/dl/dd[1]/table/tbody/tr[1]/td[3]').text()
                    say1 = str.replace('… ', '...')
                    bot.send_message(message.chat.id, '\U00002601 Погода завтра: ' + str2 + ':   ' + say1+' °C')

            elif g.doc.select('/html/body/div[2]/div[1]/div[3]/span[1]').exists():
                str = g.doc.select('/html/body/div[2]/div[1]/div[3]/span[1]').text()
                say1 = str.replace('−', ' −')

                bot.send_message(message.chat.id, '\U00002601 Погода: ' + say1)

            else:
                print('Not found')


        if "новости" in message.text:

            i = 0
            while i < 4:
                e = news_rss.entries[i]
                print("News: " + e.title)
                send = e.title
                time.sleep(0.5)
                bot.send_message(message.chat.id, 'News: ' + send)
                i = i + 1




        if "сохрани" in message.text:
            bot2.trainer.export_for_training('corpus/last_session_corpus.json')
            print('ОК')

      #  statement = message.text

       # answer = make_answer(statement)


        #print("Вы сказали: {}".format(statement))
        #print("{} сказал: {}".format(bot2.name, answer))

       # bot.send_message(message.chat.id, '{}'.format(answer))


"""
except (KeyboardInterrupt, EOFError, SystemExit):
    # Сохраняем данные для следующей сессии
    bot2.trainer.export_for_training('corpus/last_session_corpus.json')
    print("Пока!")"""


threading.Thread(target=bot.polling).start()


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "tryler":

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Трейлер:")

            ids = call.message.chat.id
            msg = call.message.text
            if ("фильм" in call.message.text):
                msg = call.message.text.replace('фильм', 'трейлер')
            if ("сериал" in call.message.text):
                msg = call.message.text.replace('сериал', 'трейлер')

            print(msg)
            time.sleep(0.3)
            video(ids, msg, rand=0)




def make_answer( statement):
    return bot2.get_response(statement)

def count(msg,ids):

    print(msg)
    bot.send_message(ids, '{}'.format(msg))

def pic(ids, msg,rand):
    ss = requests.Session()
    r = ss.get('https://yandex.ru/images/search?text=' + msg)
    p = 'div.class\=\"serp-item.*?url\"\:\"(.*?)\"'
    response = r.text
    w = re.findall(p, response)
    #
    if len(w) > 0:
        # Первые 30 фото
        w = w[0:29:1]


        if (rand == 0):
            link = w[0]
        else:
            link = random_number.choice(w)


        bot.send_photo(ids, photo=link)
        print(link)
    else:
        bot.send_message(ids, 'Ничего не найдено')


def video(ids,msg,rand):
    link = urllib.parse.urlencode({"search_query" : msg})
    content = urllib.request.urlopen("https://www.youtube.com/results?" + link)
    search_results = re.findall('href=\"\/watch\?v=(.*?)\"', content.read().decode())
    if len(search_results)>0:
        # Первые 10 результатов
        search_results = search_results[0:9:1]

        if(rand == 0):
            link2 = search_results[0]
        else:
            link2 = random_number.choice(search_results)

        yt_link = "https://www.youtube.com/watch?v="+link2
        bot.send_message(ids, text=yt_link, parse_mode="Markdown")
    else:
        bot.send_message(ids, text='Ничего не найдено.')


"""
    phrases = [txt1,txt2,txt3,txt4,txt5]
    randitem = random.choice(phrases)
    jarvis_say(randitem)



   phrases = ['Готово', 'Сделано', 'Слушаюсь', 'Есть', 'Что-то еще?']
            randitem = random.choice(phrases)
            jarvis_say(randitem)

        #print(time.strftime('%a %b %d %H:%M:%S %Y')) полная дата\время"""
