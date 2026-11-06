from main import Weather

def test_weather_check():
    w = Weather()
    assert w.weather_check(-5) == "Freezing"
    assert w.weather_check(9) == "Cold"
    assert w.weather_check(19) == "Cool"
    assert w.weather_check(29) == "Warm"


def test_rain_check():

    w = Weather()

    assert w.rain_check(0.8) == "It's likely to rain. Dont forget your umbrella"
    assert w.rain_check(0.5) == "Theres a chance of rain. You might want to carry an umbrella"
    assert w.rain_check(0.2) == "Its unlikely to rain today"


if __name__ == "__main__":
    test_weather_check()
    test_rain_check()
    print("All tests passed!")