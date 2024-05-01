from numpy.random import randint

weather_list = ["stormy", "sunny", "rainy", "foggy", "windy", "snowy",
                "cloudy"]

day_time_list = ["morning", "night", "dawn", "dusk"]


def get_weather_modifier():
    weather = weather_list[randint(0, len(weather_list)-1)]
    return weather


def get_day_time_modifier():
    day_time = day_time_list[randint(0, len(day_time_list) - 1)]
    return day_time
