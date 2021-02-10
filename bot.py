import pyowm
import telebot

owm = pyowm.OWM('f70b2868746d0a1f0c27740e7031549a')
bot = telebot.TeleBot("1587685684:AAE4Z9fZMpG337j1Z_pgbE1q5YmiCiKjwwg")

@bot.message_handler(content_types = ['text'])
def send_echo( message ):
    place = message.text
    try:
        observation = owm.weather_at_place( place )
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        detstat =  w.get_detailed_status()
        #temp = 1
        #detstat = "1"
        answer = "В городе " + place + " температура "
        answer += str(temp)
        answer += "C, " + detstat
    except Exception:
        answer = 'Не удалось определить место, '
        answer += 'напишите название города по английски или русски'

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
