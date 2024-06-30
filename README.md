# Simple Weather API
## Description
Given a lattitude and longitude pair, find the weather forecast for the specific point.\n
The python program p1.py will generate a json file given a lattitude and longitude that is then used by the index.html file to create a webpage of the weather forecast.
This uses the weather.gov api to retrieve it's data.
## Requirements
1. Python which can be downloaded here: https://www.python.org/downloads/
2. An internet connection
## How to Use
1. Download the p1.py and index.html files
2. In a terminal within the same directory as the p1.py and index.html file run '$>python p1.py (lattitude) (longittude)' Replace the parenthesis values with your own.
3. Open the index.html file within your browser. If the data doesn't show, try this: In the same terminal as step 2, run '$>python -m htpp.server'. Then within your webbrowser go to the url: http://localhost:8000/
4. View the weather data as you please. To recieve new weather data, redo steps 2 and 3.
