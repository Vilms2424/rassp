from asyncio import tasks

import telebot
import types
from telebot import types
import datetime
import psycopg2

#####Global##############################################################################
vtornics = None

tp = telebot.TeleBot('8046394107:AAH0tVcJIBJMeTwku7wSV75LEdZtIWGyYmI');


#конект с бд#################################################################################

conn = psycopg2.connect(
    dbname="ryzhovvla2",
    user="ryzhovvla2",
    password="Vlad5253456",
    host="pg3.sweb.ru",
    port="5432"
)
cur = conn.cursor()
##############################################################################################
#ОПРЕДЕЛЕНИЕ ДНЯ И КОЛ-ВО недели
nows = datetime.datetime.now()
today = datetime.date.today()


week_number = today.isocalendar()[1]



week = int(week_number)
today = datetime.datetime.today().strftime("%A")
##############################################################################################
#СЛОВАРЬ#####################################################################################

def tuesday_task():
    global vtornics
    if (week_number % 2) == 0:
        cur.execute("SELECT vtornic FROM tele LIMIT 1 ")
        second = cur.fetchone()[0]
        vtornics = second
        cur.close()
        conn.close()

    else:
        cur.execute("SELECT vtornic FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()[0]
        vtornics = second
        cur.close()
        conn.close()

def wednesday_task():
    global vtornics
    if (week_number % 2) == 0:
        cur.execute("SELECT sreda FROM tele LIMIT 1 ")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()
    else:
        cur.execute("SELECT sreda FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()

def thursday_task():
    global vtornics
    if (week_number % 2) == 0:
        cur.execute("SELECT chetwerg FROM tele LIMIT 1 ")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()
    else:
        cur.execute("SELECT chetwerg FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()


def friday_task():
    global vtornics
    if (week_number % 2) == 0:
        cur.execute("SELECT pitnica FROM tele LIMIT 1 ")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()
    else:
        cur.execute("SELECT pitnica FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()

def saturday_task():
    global vtornics
    if (week_number % 2) == 0:
        cur.execute("SELECT subbota FROM tele LIMIT 1 ")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()
    else:
        cur.execute("SELECT subbota FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()

def default_task():
    vtornics = "ВЫХОДНОЙ СЕГОДНЯ"

tasks ={
    "Monday": default_task(),
    "Tuesday": tuesday_task,
    "Wednesday": wednesday_task,
    "Thursday": thursday_task,
    "Friday": friday_task,
    "Saturday": saturday_task,
    "Sunday": default_task,
      }
tasks.get(today, default_task)()

##############################################################################################






@tp.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('ИУК3-81Б')
    button2 = types.KeyboardButton('ИУК3-82Б')
    keyboard.add(button1, button2)

    tp.send_message(message.chat.id, "Здарова брат! Выбери группу,выведу рассписание😊",reply_markup=keyboard)



@tp.message_handler(func=lambda message: True)
def handle_message(message):
  if message.text == 'ИУК3-81Б':
        tp.send_message(message.chat.id, vtornics)
        tp.send_animation(message.chat.id, "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
  else:
         tp.send_message(message, "k")

tp.infinity_polling()