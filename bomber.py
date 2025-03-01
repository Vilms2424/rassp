import telebot
import sqlite3
import types
from telebot import types
import psycopg2
import json
import datetime

tp = telebot.TeleBot('8046394107:AAH0tVcJIBJMeTwku7wSV75LEdZtIWGyYmI');

#ОПРЕДЕЛЕНИЕ ДНЯ И КОЛ-ВО недели
nows = datetime.datetime.now()
today = datetime.date.today()
print(nows)
print(nows.isoweekday())

week_number = today.isocalendar()[1]
print({week_number})
chet = (week_number %2 == 0)

week = int(week_number)

#список
den = {
    1: {True: "🔥 Понедельник (Числитель): Выходной (Поспи)" ,
        False: "💪 Понедельник (Знаменатель): Выходной (Спи блять)"},

    2: {True: ("🎉 (Числитель) Время:10-20 УАК 2-2.18 СХЕМОТЕХНИЧ.ПРОЕКТИРОВАНИЕ.ЭС (ЛАБА) ЛЫКОВ (ВТОРНИК)"
               " \n💪  Время 12:10 СИСТЕМЫ УПРАВЛЕНИЯ БД (ЛЕКЦИЯ) АКИМЕНКО (ВТОРНИК)"),

        False: "🤓Время:10-20 УАК 3-3.08 НЕЛИНЕЙНЫЕ УПРАВЛЯЮЩИЕ СИСТЕМЫ (ЛЕКЦИЯ) (ФИНОШИН) (ВТОРНИК)"
               "💪 \n(Знаменатель) Время 12:10 УАК 2-2.05 СОВРЕМЕННЫЕ ИНФОРМАЦ. ТЕХНОЛОГИИ АВТОМАТ.(ЛЕКЦИЯ) (МАКАРЕНКО) (ВТОРНИК)"},

    3: {True: "🎉 Среда (чётная неделя): Время 10-20 УАК 2-2.30 СХЕМОТИЧН.ПРОЕКТ.ЭС (ЛЕКЦИЯ) (ЛОСКУТОВ) "
              "\nВремя 12:10 УАК 2-3.09 МЕТОДЫ ГЕН.ПРОГР. (ЛЕКЦИЯ) (КОРЛЯКОВА)"
              "\nВремя 14:15 УАК 2-3.06 МЕТОДЫ ГЕН.ПРОГР. (ЛАБА) (КОРЛЯКОВА)",

        False: "🍻 Среда (нечётная неделя): Среда (чётная неделя): Время 10-20 УАК 2-2.30 СХЕМОТИЧН.ПРОЕКТ.ЭС (ЛЕКЦИЯ) (ЛОСКУТОВ) "
              "\nВремя 12:10 УАК 2-3.09 МЕТОДЫ ГЕН.ПРОГР. (ЛЕКЦИЯ) (КОРЛЯКОВА)"},

    4: {True: "🌞 Четверг (чётная неделя): Время 10-20 УАК 2-3.10 МЕТОДЫ.ГЕНЕТ.ПРОГ (УПРАВЛ) (КОРЛЯКОВА) "
              "\nВремя 12:10 УАК 2-3.09 СОВРЕМЕНН.ИНФОР.ТЕХНОЛОГ (ЛАБА) (МАКАРЕНКОВ)"
              "\nВремя 14:15 УАК 2-3.06 МЕТОДЫ ГЕН.ПРОГР. (ЛАБА) (КОРЛЯКОВА)"
              "\nВремя 16:20 УАК 2-3.03 НЕЛИНЕЙНЫЕ УПРАВЛЯЮЩИЕ СИСТЕМЫ (ФИНОШИН) (ЛАБА)",

        False: "🎮 Четверг (нечётная неделя):Время 12:10 УАК 2-3.38 ТЕХНИЧ.СРЕДСТВ.УПРАВ (ЛАБА) (КОНОВАЛОВ)"
              "\nВремя 14:15 УАК 2-3.06 МЕТОДЫ ГЕН.ПРОГР. (ЛАБА) (КОРЛЯКОВА)"},

    5: {True: "🌞 Пятница (чётная неделя):Время 10:20 УАК 2-2.09 ТЕХНИЧ.СРЕДСТВ.УПРАВ (ЛАБА) (КОНОВАЛОВ)"
              "\nВремя 12:10 УАК 2-2.05 СИСТЕМЫ УПРА БД (ЛЕКЦИЯ) (АКИМЕНКО)",

        False: "🎮 Пятница (нечётная неделя): Время 10:20 УАК 2-2.09 ТЕХНИЧ.СРЕДСТВ.УПРАВ (ЛАБА) (КОНОВАЛОВ)"
              "\nВремя 12:10 УАК 2-2.05 СИСТЕМЫ УПРА БД (ЛЕКЦИЯ) (АКИМЕНКО)"
               "\nВремя 14:15 УАК 2-3.61  СИСТЕМЫ УПРА БД (ЛАБА) (АКИМЕНКО"},

    6: {True: "🌞 Суббота (чётная неделя): Время 10:20 УАК 1-4.03 ОСНОВЫ ЗАЩИТ ИНФОРМАЦИИ (ЛЕКЦИЯ) (БУРМИСТРОВ)",

            False: "🎮 Суббота (нечётная неделя): Время 10:20 УАК 1-4.03 ОСНОВЫ ЗАЩИТ ИНФОРМАЦИИ (ЛЕКЦИЯ) (БУРМИСТРОВ)"
                   " \nВремя 12:10 УАК 2-4.06 ОСНОВЫ ЗАЩИТ ИНФОРМАЦИИ (ЛАБА) (КОРНЕЕВ)"},
    7: {True: "🌞 Воскресенье (чётная неделя): Отдыхаем с пользой!",
            False: "\n🎮 Воскресенье (нечётная неделя): Играем и отдыхаем!"}
}

dayss = nows.isoweekday()



# if dayss in den:
#     print(den[dayss][chet])

# #конект с бд
#
# conn = psycopg2.connect(
#     dbname="ryzhovvla2",
#     user="ryzhovvla2",
#     password="Vlad5253456",
#     host="pg3.sweb.ru",
#     port="5432"
# )
# cur = conn.cursor()
#
# #вторники
# cur.execute("SELECT vtornic FROM tele LIMIT 1 ")
# rows = cur.fetchone()
# vtornic =(rows[0])
# # print(vtornic)
# cur.execute("SELECT vtornic FROM tele LIMIT 1 OFFSET 1")
# second = cur.fetchone()
# vtornics = second[0]
# # print(vtornics)
# #среды
#
# cur.close()
# conn.close()











@tp.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('ИУК3-81Б')
    button2 = types.KeyboardButton('ИУК3-82Б')
    keyboard.add(button1, button2)

    tp.reply_to(message,'Здарова брат! Выбери группу,выведу рассписание',reply_markup=keyboard)


@tp.message_handler(func=lambda message: True)
def handle_message(message):

  if message.text == 'ИУК3-81Б':
        tp.reply_to(message, den[dayss][chet])
        tp.send_animation(message.chat.id, "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
  else:
         tp.reply_to(message, "k")

tp.infinity_polling()