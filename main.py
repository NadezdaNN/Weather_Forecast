from flask import Flask, render_template, request
import json
import webbrowser
from Weather import func_weather
from PyQt5.QtCore import QSettings


app = Flask(__name__, static_folder="static")
settings = QSettings()


@app.route('/count/<name_city>', methods=['POST'])
def count(name_city): # получить кол-во обращений по названию города 
    if request.method == 'POST':        
        city_dict = settings.value("city_name_for_api")                    
        try:            
            return json.dumps({str(name_city): city_dict[name_city]}), 200
        except:            
            return json.dumps({"Нет такого города": 0}), 200
    

@app.route('/get_forecast', methods=['GET', 'POST'])
def get_forecast():     
    if request.method == 'POST': 
        name_city = request.form['name_city']        
        settings.setValue("my_city_name", str(name_city))        
        city_dict = settings.value("city_name_for_api") 
        
        try: 
            city_dict[name_city] = city_dict[name_city] + 1            
        except:     
            if city_dict==None:
                city_dict = {}      
            city_dict[name_city] = 1          
        finally:                      
            settings.setValue("city_name_for_api", city_dict)            
            pred = func_weather(name_city) # получение прогноза               
            return json.dumps({'pred': pred[0], 'pred2': pred[1], 'pred3': pred[2], 'pred4': pred[3]})
    

@app.route('/')  
def start():               
    my_city = settings.value("my_city_name")
    return render_template('weatherForecast.html', city=my_city)
    

if __name__ == "__main__": 
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run() # debug=True host='0.0.0.0', port=5000
