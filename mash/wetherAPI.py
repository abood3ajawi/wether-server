import requests

def fahrenheit_to_celsius(temperature):
    return round((temperature - 32) * 5 / 9)


def temperature():
    url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
    api_key = "fcccea595c6853ebd16d158382e021519ac0b067de2bec494d43d17e8ec7ea87"  


    headers = {
        "x-api-key": api_key,
        "Content-type": "application/json"
    }

    params = {
        "lat": 31.9539,
        "lng": 35.9106
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == requests.codes.ok:
            unit = "°C"
            data = response.json()
            temperature = fahrenheit_to_celsius(data['data']['temperature'])
            humidity = data['data']['humidity']
            TemperatureData = "Temperature: " + str(temperature) + 'C' +  "  Humidity: " + str(humidity) + "%"
            TemperatureData_bytes = TemperatureData.encode('utf-8')
            print(TemperatureData_bytes)
            return TemperatureData_bytes
        else:
            print("Request to API endpoint failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error occurred while making a request:", str(e))

temperature()