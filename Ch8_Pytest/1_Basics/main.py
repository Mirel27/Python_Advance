def weather_check(temp:float)-> str:
    if temp < 0:
        return "Freezing"
    elif 0 <= temp < 10:
        return "Cold"
    elif 10 <= temp < 20:
        return "Cool"
    elif 20 <= temp < 30:
        return "Warm"
    else:
        return "Hot"

print(weather_check(-5))  # Output: Freezing