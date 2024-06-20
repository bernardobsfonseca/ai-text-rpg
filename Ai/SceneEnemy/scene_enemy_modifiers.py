from numpy.random import randint

weather_list = ["stormy", "sunny", "rainy", "foggy", "windy", "snowy",
                "cloudy"]

mode_list = ["furious", "huge", "fast", "small", "frightening"]


def get_weather_modifier():
    weather = weather_list[randint(0, len(weather_list)-1)]
    return weather


def get_mode_modifier():
    mode = mode_list[randint(0, len(mode_list)-1)]
    return mode
