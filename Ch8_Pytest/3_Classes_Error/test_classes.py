from main import Weather
import pytest

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

def test_divide():
    w= Weather()

    assert w.divide(10,2)  == 5
    assert w.divide(9,3) == 3
    # assert w.divide(9,0) == 3
    with pytest.raises(ValueError, match = "Cannot divide by 0"):
        w.divide(10,0)

# if __name__ == "__main__":
#     test_weather_check()
#     test_rain_check()
#     test_divide()
#     print("All tests passed!")