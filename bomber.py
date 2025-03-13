import telebot
import types
from telebot import types
import datetime
import psycopg2
import random

gif_links = [
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTdlYWQzazI1ZnNuMnFtbGh1c2NtZml4ZTlmcnFueXNraWFnMHB3aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SYQFjIKXTL6f2HoJIh/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGtpaDZsMXMxMjQ4MXB1ZzgxZ3B2czV0djR3dzYxa201NXU1aDZvdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lqai9XFaYXMx2kpqf3/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzU0cGFtczhkeTFyM2Zqd240NW8wamE1dDJkaDU4NGQycXE5ZXczYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EZICHGrSD5QEFCxMiC/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzZrbW15emNrdTY5NGQwdmRtdDdxaGJqd3cyaHM3OWdtMW5sbDcxdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/duNowzaVje6Di3hnOu/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzJ1Mmt3bW1ycGl1OG84Y2VuY3F6Njg2NThndGFsNDQ0cTM2YjU3bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3nbxypT20Ulmo/giphy.gif"
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdG5pdDlidXBzcjV1bnN0aWdpOTJqNWYxOHFxYzI2bjFuZXVtZjd3aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QRMF9aqduXdfY8eOcv/giphy.gif"
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3U2Nno4N2lsZHJtbTZnYmFoNmJxb2YxZXZyN2h4M2VqYW82MHNlbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1MTLxzwvOnvmE/giphy.gif"
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3QwdWFkYmhybDJiZWN6czhkemd2dmJsNzIydGJjMmk5Z20xd2QwNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uwlDAujt3w9mU/giphy.gif"
]





#####Global##############################################################################
vtornics = None
nows = None
today = None
week_number = None
week = None
today =  None
ds = None

tp = telebot.TeleBot('8046394107:AAH0tVcJIBJMeTwku7wSV75LEdZtIWGyYmI');


#конект с бд#################################################################################

conn = psycopg2.connect(dbname="ryzhovvla2",user="ryzhovvla2",password="Vlad5253456",host="pg3.sweb.ru",port="5432")
cur = conn.cursor()
##############################################################################################
# ОПРЕДЕЛЕНИЕ ДНЯ И КОЛ-ВО недели
nows = datetime.datetime.now()
today = datetime.date.today()
week_number = today.isocalendar()[1]
week = int(week_number)
today = datetime.datetime.today().strftime("%A")
print(today, week_number)



##############################################################################################

def mon_task():
    global ds
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT monday FROM iuk2 LIMIT 1 ")
        second = cur.fetchone()[0]
        ds = second
        cur.close()
        conn.close()

    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT monday FROM iuk2 LIMIT 1 OFFSET 1")
        second = cur.fetchone()[0]
        ds = second
        cur.close()
        conn.close()


def tues_task():
    global ds
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT vtornic FROM iuk2 LIMIT 1 ")
        second = cur.fetchone()[0]
        ds = second
        cur.close()
        conn.close()

    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT  vtornic FROM iuk2 LIMIT 1 OFFSET 1")
        second = cur.fetchone()[0]
        ds = second
        cur.close()
        conn.close()

def wed_task():
    global ds
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT sreda FROM iuk2 LIMIT 1 ")
        second = cur.fetchone()
        ds = second[0]
        cur.close()
        conn.close()
    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT sreda FROM iuk2 LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        ds = second[0]
        cur.close()
        conn.close()

def thus_task():
    global ds
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT chetwerg FROM iuk2 LIMIT 1 ")
        second = cur.fetchone()
        ds = second[0]
        cur.close()
        conn.close()
    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT chetwerg FROM iuk2 LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        ds = second[0]
        cur.close()
        conn.close()


def frid_task():
    global ds
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT pitnica FROM iuk2 LIMIT 1 ")
        second = cur.fetchone()
        ds = second[0]
        cur.close()
        conn.close()
    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT pitnica FROM iuk2 LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        ds = second[0]
        cur.close()
        conn.close()






##############################################################################################
#СЛОВАРЬ#####################################################################################

def tuesday_task():
    global vtornics
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT vtornic FROM tele LIMIT 1 ")
        second = cur.fetchone()[0]
        vtornics = second
        cur.close()
        conn.close()

    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT vtornic FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()[0]
        vtornics = second
        cur.close()
        conn.close()

def wednesday_task():
    global vtornics
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT sreda FROM tele LIMIT 1 ")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()
    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT sreda FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()

def thursday_task():
    global vtornics
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT chetwerg FROM tele LIMIT 1 ")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()
    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT chetwerg FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()


def friday_task():
    global vtornics
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT pitnica FROM tele LIMIT 1 ")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()
    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT pitnica FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()

def saturday_task():
    global vtornics
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT subbota FROM tele LIMIT 1 ")
        second = cur.fetchone()
        vtornics = second[0]
        cur.close()
        conn.close()
    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
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

def def_task():
    global ds
    ds = "ВЫХОДНОЙ СЕГОДНЯ"

tasks1 ={
    "Monday": mon_task,
    "Tuesday": tues_task,
    "Wednesday": wed_task,
    "Thursday": thus_task,
    "Friday": frid_task,
    "Saturday": def_task,
    "Sunday": def_task,
      }
tasks1.get(today, default_task)()





##############################################################################################






@tp.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('ИУК3-81Б')
    button2 = types.KeyboardButton('ИУК2-41Б')
    keyboard.add(button1, button2)
    random_gif = random.choice(gif_links)

    tp.send_message(message.chat.id, "Здарова брат! Выбери группу,выведу рассписание😊 P.S Интеликтуальная собственность JsRelaxe",reply_markup=keyboard)
    tp.send_animation(message.chat.id, random_gif)


@tp.message_handler(func=lambda message: message.text in ['ИУК3-81Б', 'ИУК2-41Б'])
def handle_message(message):
  global week_number,today,ds
  today = datetime.date.today()
  week_number = today.isocalendar()[1]
  today = datetime.datetime.today().strftime("%A")
  if message.text == 'ИУК3-81Б':
      random_gif = random.choice(gif_links)
      tp.send_message(message.chat.id, vtornics)
      tp.send_animation(message.chat.id, random_gif)
  elif message.text == 'ИУК2-41Б':
      random_gif = random.choice(gif_links)
      tp.send_message(message.chat.id, ds)
      tp.send_animation(message.chat.id, random_gif)
  else:
         tp.send_message(message.chat.id, "Ошибка обратитесь к администратору")

tp.infinity_polling()