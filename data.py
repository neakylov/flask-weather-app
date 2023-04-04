import requests
import datetime
import locale


def get_data(city):
    locale.setlocale(locale.LC_ALL, 'ru')
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=023a658714d84be8bf504915233103&q={city}&days=7&aqi=no&alerts=no&lang=RU').json()
    location_name = response['location']['name']
    location_country = response['location']['country']
    current = response['current']
    current_img = current['condition']['icon']
    current_temperature = current['temp_c']
    current_cloudy = current['condition']['text']
    # --------------------------------------------- localtime
    localtime = response['location']['localtime']
    # --------------------------------------------- forecast
    forecast = response['forecast']['forecastday']
    for day in forecast:
        day['date'] = day['date'][-2:]

    result = {
        'current': {
            'name': location_name,
            'country': location_country,
            'img': current_img,
            'temperature': current_temperature,
            'cloudy': current_cloudy,
            'localtime': localtime
        },
        'forecast': response['forecast']['forecastday'],
    }
    return result


def main():
    get_data('Moscow')


if __name__ == '__main__':
    main()
