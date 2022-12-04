import requests

pos = {
    'lat' :  '23.030357',
    'long' : '72.517845'
}
s  = "https://api.open-meteo.com/v1/forecast?latitude=" + pos['lat'] + "&longitude=" + pos['long'] + "&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
response = requests.get(url=s)
print(response.text)