from time import strftime
import requests
import datetime
from pprint import pprint
from config import p_t


def get_weather (city, p_t):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={p_t}&units=metric"
        )
        data = r.json()
        #pprint (data)
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        speed = data["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        print(f":{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
             f"Погода в городе:  {city}\nТемпература: {cur_weather}C°\n"
             f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст\nСкорость ветра: {speed}м.с\n"
             f"Восход солнца: {sunrise_time}\n"
             f"Закат: {sunset_time}\n"
             f"Хорошего дня!")
    except Exception as ex:
        pprint(ex)
        pprint("Проверьте правильность названия города")


def main():
    city = input("Введите город: ")
    get_weather(city, p_t)
if __name__=='__main__':
    main()

        
