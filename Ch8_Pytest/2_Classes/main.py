class Weather:
    def __init__(self):
        pass

    
    def weather_check(self,temp:float)-> str:

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


    def rain_check(Self, rain_chance:float)-> str:
        if rain_chance> 0.7:
            return "It's likely to rain. Dont forget your umbrella"
        elif rain_chance> 0.3:
            return "Theres a chance of rain. You might want to carry an umbrella"
        else:
            return "Its unlikely to rain today"

        
    

    