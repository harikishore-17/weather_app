# forecast/views.py
import requests
from django.shortcuts import render
from decouple import config
def weather_forecast(request):
    city = None
    temperature = None
    description = None

    if request.method == 'POST':
        city = request.POST.get('city_name')
        access_key = config('WEATHERSTACK_API_KEY')
        url = f'http://api.weatherstack.com/current?access_key={access_key}&query={city}'

        response = requests.get(url)
        data = response.json()

        temperature = data['current']['temperature']
        description = data['current']['weather_descriptions'][0]

    context = {
        'city': city,
        'temperature': temperature,
        'description': description,
    }
    return render(request, 'weather_form.html', context)
