from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

import requests
def index(request):
    result = None
    city = request.GET.get('city')
    if 'city' in request.GET:
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

        querystring = {"q":f"{city}","days":"1"}

        headers = {
            'x-rapidapi-key': "8770f6244dmsh1bd7a026e257ea8p1632dbjsned987d24e059",
            'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        response=response.content
        # print(type(response))
        import ast
        byte_str =response
        dict_str = byte_str.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        # print(repr(mydata))
        result = dict()
        # extract region
        result['region'] = mydata['location']['name']
        # extract temperature now
        result['temp_now'] = mydata['current']['temp_c']
        # get the day and hour now
        result['dayhour'] = mydata['location']['localtime']
        # get the actual weather
        result['weather_now'] = mydata['current']['condition']['text']
        print(result)
    return render(request, 'audio.html', {'result':result})