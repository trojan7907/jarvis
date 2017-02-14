#! /usr/bin/env python
#-*-coding:utf-8-*-
import os
import speech_recognition as sr
from xml.dom import minidom
from grab import Grab
import random
import webbrowser

import datetime
import time
import subprocess
from tempfile import mkstemp
from shutil import move
from os import remove, close

r = sr.Recognizer()
ya_uuid = 'f66f1992e86811e6bf01fe55135034f8'
ya_api_key = 'b0da0acd-dcfe-4785-b496-10ac81f56ce9'


#os.system('echo "Ассист+ент зап+ущен" |festival --tts --language russian')




def convert_ya_asr_to_key():
    xmldoc = minidom.parse('./asr_answer.xml')
    itemlist = xmldoc.getElementsByTagName('variant')
    if len(itemlist) > 0:
        return itemlist[0].firstChild.nodeValue
    else:
        return False





def jarvis_say(phrase):
    print('озвучка: ')
    print(phrase)
    os.system('curl "https://tts.voicetech.yandex.net/generate?format=wav&lang=ru-RU&speaker=kostya&emotion=good&speed=1.0&key=' + ya_api_key + '" -G --data-urlencode "text=' + phrase + '" > jarvis_speech.wav')
    global spwd
    spwd = subprocess.Popen('aplay jarvis_speech.wav', shell=True)


def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    remove(file_path)
    move(abs_path, file_path)



"""def jarvis_say_good():
    phrases = ['Готово', 'Сделано', 'Слушаюсь', 'Есть', 'Что-то еще?']
    randitem = random.choice(phrases)
    jarvis_say(randitem)"""



#command_key = 'новости санкт петербурга'
#old_key = 'сериал стрела'






global old_key
check1 = 0

#try:
while True:



                #os.system('arecord -B --buffer-time=1000000 -f dat -r 16000 -d 2.4 -D plug:default send.wav')

                with sr.Microphone() as source:
                    print("Say something!")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)

                # recognize speech using Sphinx
                try:
                    # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
                    print("Sphinx thinks you said " + r.recognize_google(audio,language = "ru-RU"))

                    if (r.recognize_google(audio,language = "ru-RU") == "Привет"):

                        os.system('aplay on3.wav')
                        os.system('arecord -B --buffer-time=1000000 -f dat -r 16000 -d 3 -D plug:default send.wav')
                        print('Отправляется запрос на сервер')
                        os.system('curl -X POST -H "Content-Type: audio/x-wav" --data-binary "@send.wav" "https://asr.yandex.net/asr_xml?uuid=' + ya_uuid + '&key=' + ya_api_key + '&topic=queries" > asr_answer.xml')
                        print('Запрос на сервер')
                        command_key = convert_ya_asr_to_key()

                        if (command_key):


                            if ("стоп" in command_key):
                                print('СТОП')
                                jarvis_say('.')
                                #spwd.kill()
                                #time.sleep(1)
                                continue



                            #if (command_key in ['какой сегодня день', 'какой день','сегодня что', 'что сегодня']):
                            if (" день" in command_key) or (" сегодня" in command_key):
                                days = {0: u"Понедельник", 1: u"Вторник", 2: u"Среда", 3: u"Четревг", 4: u"Пятница", 5: u"Суббота", 6: u"Воскресенье"}
                                time.sleep(1)
                                jarvis_say(days[datetime.date.today().weekday()])
                                continue

                            #if ("музыка" in command_key):
                            if ("включи" in command_key) and ("музык" in command_key):
                                webbrowser.open('https://radio.yandex.ru/user/tretyakov-files')
                                #time.sleep(10)
                                #os.system('xdotool key space')
                                jarvis_say('Уже включаю')
                                continue

                            if ("дальше" in command_key) or ("следующий" in command_key) or ( "переключи" in command_key)or ( "переключить" in command_key):

                                time.sleep(1)
                                os.system('xdotool key L')
                                jarvis_say('Выполнено')
                                continue


                            #if (command_key in ['сколько время', 'сколько времени', 'который час']):
                            if ("время" in command_key) or (" час" in command_key):
                                g = Grab(log_file='out.html')
                                g.go('https://www.google.ru/search?q=время')

                                time.sleep(1)
                                if g.doc.select('//*[@id="rso"]/div[1]/div/div/div/div[1]').exists():
                                    #print(g.doc.select('//*[@id="rso"]/div[1]/div/div/div/div[1]').text())
                                    jarvis_say(g.doc.select('//*[@id="rso"]/div[1]/div/div/div/div[1]').text())
                                else:
                                    print('Not found')

                                continue

                            #if (command_key in ['какая погода', 'сколько градусов','сколько на улице']):
                            if ("погода" in command_key) or (" градус" in command_key)or (" температура" in command_key):
                                g = Grab(log_file='out2.html')
                                g.go('https://yandex.ru/pogoda/yekaterinburg?lat=56.83174&lon=60.535361&name=улица+Рабочих%2C+Екатеринбург&kind=street')

                                time.sleep(1)
                                if g.doc.select('/html/body/div[2]/div[1]/div[3]/span[1]').exists():
                                    str = g.doc.select('/html/body/div[2]/div[1]/div[3]/span[1]').text()
                                    say1 = str.replace('−', ' минус ')
                                    jarvis_say(say1)
                                else:
                                    print('Not found')

                                continue


                            if ("спасибо" in command_key):
                                jarvis_say('Всё для вас')
                                continue


                            if  ("как" in command_key) and ("рейтинг" in command_key):
                                if check1 == 1:
                                    g = Grab(log_file='out4.html')
                                    g.go('https://www.google.ru/search?q=рейтинг {}'.format(old_key))
                                    time.sleep(1)
                                    if g.doc.select('//*[@id="rso"]/div/div/div[1]/div/div/div/div[2]').exists():  # поиск фильмов (сблк с лева)
                                        ser1 = g.doc.select('//*[@id="rso"]/div/div/div[1]/div/div/div/div[2]').text()
                                        say1 = ser1.replace('/', ' из ')
                                        index = 20
                                        say1 = say1[:index]
                                        rate = 'По оценке кинопоиска: '
                                        jarvis_say(rate + say1)
                                        check1 = 0

                                    else:
                                        jarvis_say('К сожалению: мне не удалось найти рейтинг этого фильма.')
                                        check1 = 0

                                    continue
                                elif jarvis_say('Какой еще рейтинг?'):
                                    continue


                            if ("запиши" in command_key):
                                my_file = open('list.txt', 'a+')
                                str = command_key
                                zapis = str.replace('запиши', '')
                                my_file.write(zapis + '\n')
                                my_file.close()
                                jarvis_say('Записала: '+zapis)
                                continue


                            if ("список" in command_key):
                                my_file = open("list.txt")
                                my_string = my_file.read()
                                my_file.close()
                                jarvis_say('Вот все записи: '+my_string)
                                continue

                            if ("удали" in command_key):
                                str = command_key
                                remove1 = str.replace('удали', '')
                                replace('list.txt', remove1, '')
                                jarvis_say('Хорошо: '+remove1+' Удалено!')
                                continue

                            if (command_key in [command_key]):
                                g = Grab(log_file='out4.html')
                                g.go('https://www.google.ru/search?q={}'.format(command_key))


                                time.sleep(1)
                                if g.doc.select('//*[@id="rhs_block"]/div[1]/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div/span').exists():  # поиск фильмов (сблк с лева)
                                    os.system('aplay search.wav')
                                    print(g.doc.select('//*[@id="rhs_block"]/div[1]/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div/span').text())
                                    jarvis_say(g.doc.select('//*[@id="rhs_block"]/div[1]/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div/span').text())
                                    old_key = command_key
                                    if check1 == 1:
                                        check1 = 0

                                    check1 = 1

                                else:
                                    print('Not found 1')
                                    if g.doc.select(
                                            '//*[@id="rhs_block"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/span[1]').exists():  # поиск фильмов2, людей (сблк с лева2)
                                        os.system('aplay search.wav')
                                        print(g.doc.select(
                                            '//*[@id="rhs_block"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/span[1]').text())
                                        jarvis_say(g.doc.select(
                                            '//*[@id="rhs_block"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/span[1]').text())
                                    else:
                                        print('Not found 2')
                                        if g.doc.select('//*[@id="cwos"]').exists():  # поиск хз
                                            os.system('aplay search.wav')
                                            print(g.doc.select('//*[@id="cwos"]').text())
                                            jarvis_say(g.doc.select('//*[@id="cwos"]').text())
                                        else:
                                            print('Not found 3')
                                            if g.doc.select(
                                                    '//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/span').exists():  # поиск определений с сайтов + калькулятор
                                                os.system('aplay search.wav')
                                                print(g.doc.select(
                                                    '//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/span').text())
                                                jarvis_say(g.doc.select(
                                                    '//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/span').text())
                                            else:
                                                print('Not found 4')
                                                if g.doc.select(
                                                        '//*[@id="uid_0"]/div[1]/div/div[1]/div[2]/div/ol/li/div/div/div/div/div/span').exists():  # поиск определений с википедии
                                                    os.system('aplay search.wav')
                                                    print(g.doc.select(
                                                        '//*[@id="uid_0"]/div[1]/div/div[1]/div[2]/div/ol/li/div/div/div/div/div/span').text())
                                                    jarvis_say(g.doc.select(
                                                        '//*[@id="uid_0"]/div[1]/div/div[1]/div[2]/div/ol/li/div/div/div/div/div/span').text())
                                                else:
                                                    print('Not found 5')
                                                    if g.doc.select(
                                                            '//*[@id="uid_0"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/span[1]').exists():  # поиск исполнителей (окс, баста)
                                                        os.system('aplay search.wav')
                                                        print(g.doc.select(
                                                            '//*[@id="uid_0"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/span[1]').text())
                                                        jarvis_say(g.doc.select(
                                                            '//*[@id="uid_0"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/span[1]').text())
                                                    else:
                                                        print('Not found 6')
                                                        if g.doc.select( #новости
                                                                '//*[@id="rso"]/div[1]/div/g-section-with-header/g-card-grid/ul/li[1]/g-inner-card/div/a/div[2]/div').exists() and g.doc.select(
                                                                '//*[@id="rso"]/div[1]/div/g-section-with-header/g-card-grid/ul/li[2]/g-inner-card/div/a/div[2]/div').exists() and g.doc.select(
                                                                '//*[@id="rso"]/div[1]/div/g-section-with-header/g-card-grid/ul/li[3]/g-inner-card/div/a/div[2]/div').exists():  # поиск исполнителей (окс, баста)
                                                            os.system('aplay search.wav')

                                                            news1 = g.doc.select(
                                                                '//*[@id="rso"]/div[1]/div/g-section-with-header/g-card-grid/ul/li[1]/g-inner-card/div/a/div[2]/div').text()
                                                            say2 = news1.replace('\"', ' ')
                                                            jarvis_say(say2)

                                                            time1 = len(news1)
                                                            time.sleep(time1 / 15 + 1)

                                                            news2 = g.doc.select('//*[@id="rso"]/div[1]/div/g-section-with-header/g-card-grid/ul/li[2]/g-inner-card/div/a/div[2]/div').text()
                                                            say2 = news2.replace('\"', ' ')
                                                            jarvis_say(say2)

                                                            time2 = len(g.doc.select(
                                                                '//*[@id="rso"]/div[1]/div/g-section-with-header/g-card-grid/ul/li[2]/g-inner-card/div/a/div[2]/div').text())
                                                            time.sleep(time2 / 15 + 1)

                                                            news3 = g.doc.select(
                                                                '//*[@id="rso"]/div[1]/div/g-section-with-header/g-card-grid/ul/li[3]/g-inner-card/div/a/div[2]/div').text()
                                                            say2 = news3.replace('\"', ' ')
                                                            jarvis_say(say2)

                                                        else:
                                                            print('Not found 7')


                                continue




                except sr.UnknownValueError:
                    print("Sphinx could not understand audio")
                except sr.RequestError as e:
                    print("Sphinx error; {0}".format(e))


#except Exception:
#  jarvis_say('Что-то пошло не так')

#input("\n\nНажмите Enter чтобы выйти .")