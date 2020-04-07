from flask import Flask, render_template, request ,jsonify
import requests
import max_reader

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    sensor1 = max_reader.tempreading1()
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

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
