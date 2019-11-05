import pyowm

city = input("Какой город Вас интересует? ")
owm = pyowm.OWM('92f6eb4059ac8c7fff670b70ff5a2e24')

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print("В городе " + city + " сейчас температура: " + str(temperature) + " по Цельсию.")
print("Также, в укзанно городе " + w.get_detailed_status())