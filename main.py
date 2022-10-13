import pymysql as pymysql
from aiogram import Bot, Dispatcher, executor, types
import csv, datetime

API_TOKEN = '5524534758:AAHuCh971dzwVHy6hZbJ01fRKPh64YUF_cU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Привет!")
    statistics(message.chat.id, message.text, message.from_user.username)
    stat(message.chat.id, message.text)


def stat(user_id, command):
    connection = pymysql.connect(host='sql.freedb.tech', user='freedb_Dorina', password='v$uPXrfzM75c!c@', database='freedb_BotStat')
    cursor = connection.cursor()
    data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    cursor.execute("INSERT INTO BotStat(user_id, user_command, date) VALUES ('%s', '%s', '%s')" % (user_id, command, data))
    connection.commit()
    cursor.close()


def statistics(user_id, command, username):
    data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=';')
        wr.writerow([data, user_id, command])


if __name__ == '__main__':
    executor.start_polling(dp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
