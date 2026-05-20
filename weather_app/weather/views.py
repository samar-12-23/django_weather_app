from django.shortcuts import render
from django.conf import settings
import json
import urllib.request


api_key = settings.OPENWEATHER_API_KEY  # fetched from .env

def index(request):
    city = ''
    data = {}
    
    if request.method == 'POST':
        city = request.POST.get('city', '')
        if city:
            res = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city +
                '&appid' + api_key
            ).read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' +
                              str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'k',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }

    return render(request, 'index.html', {'city': city, 'data': data})