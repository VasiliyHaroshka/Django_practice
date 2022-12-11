from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)",
}


def get_info(request, zodiak: str):
    discription = zodiac_dict.get(zodiak)
    if discription:
        return HttpResponse(discription)
    else:
        return HttpResponseNotFound(f"{zodiak} - Нет такого знака зодиака")


def get_info_as_number(request, zodiak: int):
    all_zodiaks = list(zodiac_dict)
    if zodiak > len(all_zodiaks):
        return HttpResponseNotFound(f"{zodiak} - Нет такого номера знака зодиака")
    name_zodiak = all_zodiaks[zodiak - 1]
    redirect_url = reverse("horoscope_sign", args=(name_zodiak,))
    return HttpResponseRedirect(redirect_url)
    # for i in zodiac_dict.items():
    #     if name_zodiak == i[0]:
    #         return HttpResponse(f"{i[1]}")