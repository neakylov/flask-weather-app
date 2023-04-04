import requests

from flask import Flask, render_template, request
from data import get_data

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world() -> str:
    if request.method == 'POST':
        city = request.form.get('city')
        result = get_data(city)
        forecast = result['forecast']
        for day in forecast:
            day['date'] = day['date'][-2:]
        return render_template('index.html', current=result['current'], forecast=forecast)

    return render_template('index.html')


@app.route('/<date>')
def date(date) -> str:
    return render_template('date.html')