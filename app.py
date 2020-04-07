from flask import Flask, render_template, request ,jsonify
import requests
import max_reader
#from bs4 import BeautifulSoup


app = Flask(__name__)

#sensor1 = max_reader.pt1000()
#temp = sensor1.Temp()


@app.route('/',methods = ['POST', 'GET'])
def index():
    sensor1 = max_reader.tempreading1()
    #temp = sensor1.Temp()
    #text = temp 
    text = jsonify(sensor1) 
    num = jsonify(sensor1)
    tempVal1 =  sensor1
    return render_template('index.html', **locals())


@app.route('/suggestions',methods = ['POST', 'GET'])
def suggestions():
    sensor1 = max_reader.tempreading1()
    sensor2 = max_reader.tempreading2()
    text1 = jsonify(sensor1) 
    text2 = jsonify(sensor2) 
    num1 = jsonify(sensor2)
    num2 = jsonify(sensor1) 
    tempVal1 =  sensor1
    tempVal2 =  sensor2
    return render_template('suggestions.html', **locals())
    #return render_template('suggestions.html', suggestions=suggestions_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
