from flask import Flask, jsonify, render_template, request, session
import mysql.connector
import random
import time
import datetime
import requests

app = Flask(__name__)
app.secret_key = 'secret_key'

# ket noi csdl mysql bang python
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pbl5"
)
mycursor = mydb.cursor()
hr_session = 0
# -----------------

# url root
@app.route('/')
def main():
    test = {'name': 'John', 'age': 30}
    return render_template('index.html', context=test)

@app.route('/show_chart')
def show_chart():
    return render_template('show_chart.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    value = 0
    value = hr_session
    return jsonify(value = value) 

@app.route('/post_api', methods=['POST'])
def post_api():
    str_data = request.form.get('data')
    print(str_data)
    arr_obj = str_data.split(',')
    hr = float(arr_obj[0])
    posting_time = datetime.datetime.strptime(arr_obj[1], '%Y-%m-%d %H:%M:%S')
    
    sql = "SELECT id FROM api ORDER BY id DESC LIMIT 1"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    print(myresult)
    if myresult == None:
        id = 0
    else:
        id = myresult[0] + 1
    print(id)
    sql = "INSERT INTO api (id, hr_value, posting_time) VALUES ("+str(id)+", "+arr_obj[0]+", '"+arr_obj[1]+"');"
    mycursor.execute(sql)
    mydb.commit()
    
    # neu > 300 record thi xoa het de lam lai
    if id > 300:
        sql = "DELETE FROM api"
        mycursor.execute(sql)
        mydb.commit()

    # khong dung dc session vi api dc goi tu cho khac
    global hr_session
    hr_session = hr

    # print(session['hr'])
    print(posting_time)
    return jsonify(value= hr)

if __name__ == "__main__":
    app.run(debug=True)
    
