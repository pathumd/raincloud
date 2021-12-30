from django.shortcuts import render

# Create your views here.
import urllib.request
import json


def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=a1bc251a2f71000b9b9aed417795a57d').read()

        # Holds all the data that we are requesting for a specific city
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(int(list_of_data['main']['temp'])),
            'description': str(list_of_data['weather'][0]['description']),
            "pressure": str(list_of_data['main']['pressure']) + ' hPa',
            "humidity": str(list_of_data['main']['humidity']) + '%',
            "feel_temp": str(int(list_of_data['main']['feels_like'])) + ' °C',
            "min_temp": str(int(list_of_data['main']['temp_min'])) + ' °C',
            "max_temp": str(int(list_of_data['main']['temp_max'])) + ' °C',
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
