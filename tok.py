import telebot
import types
from telebot import types
import datetime
import psycopg2
import random


gif_links = [
    "https://media2.giphy.com/media/SYQFjIKXTL6f2HoJIh/giphy.gif",
    "https://media3.giphy.com/media/Lqai9XFaYXMx2kpqf3/giphy.gif",
    "https://media4.giphy.com/media/EZICHGrSD5QEFCxMiC/giphy.gif",
    "https://media1.giphy.com/media/duNowzaVje6Di3hnOu/giphy.gif",
    "https://media2.giphy.com/media/3nbxypT20Ulmo/giphy.gif",
    "https://media0.giphy.com/media/QRMF9aqduXdfY8eOcv/giphy.gif",
    "https://media0.giphy.com/media/1MTLxzwvOnvmE/giphy.gif",
    "https://media4.giphy.com/media/uwlDAujt3w9mU/giphy.gif",
    "https://media1.giphy.com/media/l0HlvwkgrT6NHEG4c/giphy.gif",
    "https://media2.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
    "https://media0.giphy.com/media/xT1XGPQMP1uP5aG1Is/giphy.gif",
    "https://media3.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
    "https://media4.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif",
    "https://media2.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif",
    "https://media0.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
    "https://media4.giphy.com/media/xT1R9zUWlMdxk4j3sI/giphy.gif",
    "https://media0.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif",
    "https://media1.giphy.com/media/d2Z9QYzA2aidiWn6/giphy.gif",
    "https://media4.giphy.com/media/xT9KVDE2qKxOniLShm/giphy.gif",
    "https://media2.giphy.com/media/3orieRU9E8KLzC3diM/giphy.gif",
    "https://media1.giphy.com/media/l4FGmWm6zVKfQohL6/giphy.gif",
    "https://media3.giphy.com/media/3oz8xSjBmD1ZyELqW4/giphy.gif",
    "https://media4.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif",
    "https://media0.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
    "https://media1.giphy.com/media/xT5LMWSuYT6nM4JkFG/giphy.gif",
    "https://media2.giphy.com/media/5xtDarIN81W3TL6gOuk/giphy.gif",
    "https://media3.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif",
    "https://media4.giphy.com/media/l3q2z6rf2PjwVjhkc/giphy.gif",
    "https://media0.giphy.com/media/5xtDarmwsuR3xE1zLa8/giphy.gif",
    "https://media3.giphy.com/media/3o7TKSjRrfIPjeiVyQ/giphy.gif",
    "https://media4.giphy.com/media/l0HU7jj0ivVjI3lXq/giphy.gif",
    "https://media0.giphy.com/media/xT9DPhONSR0LZWxfsc/giphy.gif",
    "https://media1.giphy.com/media/3ohhwMHaRjkb9a60f6/giphy.gif",
    "https://media2.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
    "https://media3.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif",
    "https://media4.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif",
    "https://media0.giphy.com/media/5xtDarnMgHHyknINXzi/giphy.gif",
    "https://media1.giphy.com/media/3o7TKPVg0W4Wm4JlJe/giphy.gif",
    "https://media2.giphy.com/media/3o7TKJnLYdAz6oRxVC/giphy.gif",
    "https://media3.giphy.com/media/3oz8xWpV7q9WQGhUmQ/giphy.gif",
    "https://media4.giphy.com/media/3oz8xAFtqoOUUrOWVI/giphy.gif",
    "https://media0.giphy.com/media/3o7TKPD8zFjh4omMdy/giphy.gif",
    "https://media1.giphy.com/media/3oz8xARhxjdi03cp8U/giphy.gif",
    "https://media2.giphy.com/media/3oz8xDjjREh7b87J1m/giphy.gif",
    "https://media3.giphy.com/media/3oz8xYZBv3sVHi2sZC/giphy.gif",
    "https://media4.giphy.com/media/3oz8xBoHUABsDq8cM0/giphy.gif",
    "https://media0.giphy.com/media/3oz8xC8o7XSkx08m9y/giphy.gif",
    "https://media1.giphy.com/media/3oz8xCJXXdF3c66vEc/giphy.gif",
    "https://media2.giphy.com/media/3oz8xEeUhd3XVjW4Le/giphy.gif",
    "https://media3.giphy.com/media/3oz8xEqT0fs4H25p5K/giphy.gif",
    "https://media4.giphy.com/media/3oz8xFSXYqkJ8cNVCU/giphy.gif",
    "https://media0.giphy.com/media/3oz8xGh81N9Q4hP1HG/giphy.gif",
    "https://media1.giphy.com/media/3oz8xI2BM4B9DXsIT6/giphy.gif",
    "https://media2.giphy.com/media/3oz8xJzGyeWc3x43lC/giphy.gif",
    "https://media3.giphy.com/media/3oz8xKqPyHLXYYnICo/giphy.gif",
    "https://media4.giphy.com/media/3oz8xL9jBl9pPRKb3e/giphy.gif",
    "https://media0.giphy.com/media/3oz8xMEHjKOAcZ1TFu/giphy.gif",
    "https://media1.giphy.com/media/3oz8xNEMuo3vnKaMbK/giphy.gif",
    "https://media2.giphy.com/media/3oz8xOBH6J5sPqfNck/giphy.gif",
    "https://media3.giphy.com/media/3oz8xPG9OjJc7NrcCm/giphy.gif",
    "https://media4.giphy.com/media/3oz8xQGwibygYzv4YI/giphy.gif"
]







#####Global##############################################################################
today = None
week_number = None
tomorow_name = None
today_name=None
days = None
days1 = None

tomor2 =None
tomor1 = None

nex1= None
nex2=None

tp = telebot.TeleBot('8046394107:AAH0tVcJIBJMeTwku7wSV75LEdZtIWGyYmI');


#конект с бд#################################################################################

conn = psycopg2.connect(dbname="ryzhovvla2",user="ryzhovvla2",password="Vlad5253456",host="pg3.sweb.ru",port="5432")
cur = conn.cursor()
##############################################################################################
# ОПРЕДЕЛЕНИЕ ДНЯ И КОЛ-ВО недели

def check():
    global nows, today, week_number, week, tomorrow_name,days,days1
    nows = datetime.datetime.now()  # Текущее время
    today = datetime.date.today()  # Текущая дата
    week_number = today.isocalendar()[1]  # Номер недели

    today_name = today.strftime("%A")  # День недели в строковом формате
    tomorrow = today + datetime.timedelta(days=1)  # Завтрашняя дата
    tomorrow_name = tomorrow.strftime('%A')  # Завтрашний день недели в строковом формате
    days1 = tomorrow_name.lower()
    days = today_name.lower()
    print(f"Сегодня: {today_name}, Номер недели: {week_number}, Завтра: {tomorrow_name}")





##############################################################################################

def iuk2():
    global tomor2
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        query = f"SELECT \"{days}\" FROM iuk2 LIMIT 1"  # Оборачиваем в кавычки
        cur.execute(query)
        second = cur.fetchone()[0]
        tomor2 = second
        cur.close()
        conn.close()

    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute(f"SELECT  \"{days}\" FROM iuk2 LIMIT 1 OFFSET 1")
        second = cur.fetchone()[0]
        tomor2 = second
        cur.close()
        conn.close()

def iuk3():
    global tomor1
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute(f"SELECT \"{days}\" FROM tele LIMIT 1 ")
        second = cur.fetchone()[0]
        print(second)
        tomor1 = second
        print(tomor1)
        cur.close()
        conn.close()

    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute(f"SELECT \"{days}\" FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()[0]
        print(second)
        tomor1 = second
        cur.close()
        conn.close()

#############################################################ЗАВТРА

def iuk22():
    global nex2
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        query = f"SELECT \"{days1}\" FROM iuk2 LIMIT 1"  # Оборачиваем в кавычки
        cur.execute(query)
        second = cur.fetchone()[0]
        nex2 = second
        cur.close()
        conn.close()

    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute(f"SELECT  \"{days1}\" FROM iuk2 LIMIT 1 OFFSET 1")
        second = cur.fetchone()[0]
        nex2 = second
        cur.close()
        conn.close()

def iuk33():
    global nex1
    if (week_number % 2) == 0:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute(f"SELECT \"{days1}\" FROM tele LIMIT 1 ")
        second = cur.fetchone()[0]
        nex1 = second
        cur.close()
        conn.close()

    else:
        conn = psycopg2.connect(dbname="ryzhovvla2", user="ryzhovvla2", password="Vlad5253456", host="pg3.sweb.ru",
                                port="5432")
        cur = conn.cursor()
        cur.execute(f"SELECT \"{days1}\" FROM tele LIMIT 1 OFFSET 1")
        second = cur.fetchone()[0]
        print(second)
        nex1 = second
        cur.close()
        conn.close()

#######################################################################################################################################


# Обработчик команд
@tp.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('ИУК3-81Б')
    button2 = types.KeyboardButton('ИУК2-41Б')
    button3 = types.KeyboardButton('ИУК3-81Б(Завтра)')
    button4 = types.KeyboardButton('ИУК2-41Б(Завтра)')
    keyboard.add(button1,button3,button2,button4)

    random_gif = random.choice(gif_links)
    tp.send_message(message.chat.id,
                    "Здарова брат! Выбери группу,выведу рассписание😊 P.S Интеликтуальная собственность JsRelaxe",
                    reply_markup=keyboard)
    tp.send_animation(message.chat.id, random_gif)


@tp.message_handler(func=lambda message: message.text in ['ИУК3-81Б', 'ИУК2-41Б', 'ИУК3-81Б(Завтра)', 'ИУК2-41Б(Завтра)'])
def handle_message(message):
        check()  # Обновляем глобальные переменные
        # Расписание для ИУК3-81Б (сегодня)
        if message.text == 'ИУК3-81Б':
                iuk3()
                random_gif = random.choice(gif_links)
                tp.send_message(message.chat.id, tomor1)
                tp.send_animation(message.chat.id, random_gif)


        # Расписание для ИУК2-41Б (сегодня)
        elif message.text == 'ИУК2-41Б':
                iuk2()
                random_gif = random.choice(gif_links)
                tp.send_message(message.chat.id, tomor2)
                tp.send_animation(message.chat.id, random_gif)
        elif message.text == 'ИУК3-81Б(Завтра)':
                iuk33()
                random_gif = random.choice(gif_links)
                tp.send_message(message.chat.id, nex1)
                tp.send_animation(message.chat.id, random_gif)
        elif message.text == 'ИУК2-41Б(Завтра)':
            iuk22()
            random_gif = random.choice(gif_links)
            tp.send_message(message.chat.id, nex2)
            tp.send_animation(message.chat.id, random_gif)
        else:
            tp.send_message(message.chat.id, "Ошибка обратитесь к разработчику")




#######################################################################ОШИБКИ#####################################

ADMIN_CHAT_ID = 1061678178

def send_error_to_admin(error_text):
    try:
        tp.send_message(ADMIN_CHAT_ID, f"⚠️ Ошибка в боте:\n{error_text}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения админу: {e}")

def send_admin_notification(status):
    """Отправляет сообщение админу о состоянии бота"""
    try:
        tp.send_message(ADMIN_CHAT_ID, f"🔹 Статус бота: {status}")
    except Exception as e:
        print(f"Ошибка при отправке уведомления админу: {e}")


if __name__ == "__main__":
    try:
        send_admin_notification("✅ Бот работает штатно!")
        tp.polling(none_stop=True)
    except Exception as e:
        send_admin_notification(f"❌ Ошибка: {e}")

tp.infinity_polling()
