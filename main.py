from flask import Flask, render_template, request
import json
import webbrowser
from Weather import func_weather
from PyQt5.QtCore import QSettings

app = Flask(__name__, static_folder="static")

settings = QSettings("my_city_name")     

@app.route('/get_forecast', methods=['GET', 'POST'])
def get_forecast():     
    if request.method == 'POST': 
        name_city = request.form['name_city']        
        settings.setValue("my_city_name", str(name_city))                    
        pred = func_weather(name_city) # получение прогноза        
        
        return json.dumps({'pred': pred[0], 'pred2': pred[1], 'pred3': pred[2], 'pred4': pred[3]})
    

@app.route('/start')  
def start():               
    my_city = settings.value("my_city_name")
    return render_template('weatherForecast.html', city=my_city)
    

if __name__ == "__main__":          
    webbrowser.open_new("http://127.0.0.1:5000/start")
    app.run() 
