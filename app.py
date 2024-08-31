from flask import Flask, request, render_template
import requests
import os

# Create a Flask app instance
app = Flask(__name__)

# Function to fetch weather data for a given location
def get_weather_data(location):
    API_KEY = 'd075fd0533e317a6d6e7e7fc4aeef611'
    BASE_URL = 'http://api.weatherstack.com/current'
    response = requests.get(BASE_URL, params={
        'access_key': API_KEY,
        'query': location
    })
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        data = get_weather_data(location)
        return render_template('weather.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(debug=True,port=8080)
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)