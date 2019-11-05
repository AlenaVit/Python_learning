try:
    pogoda = "Bad"
    if pogoda == "Bad":
        raise TypeError
except TypeError:
    print("Поймано исключение!")