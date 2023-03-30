import time
import random
import datetime
import requests
import json

# tạo dữ liệu random để test
def random_data():
    while True:
        hr_test = random.randint(40, 100)
        hr_string = str(hr_test)

        time_string = str(datetime.datetime.now())
        arr_obj_time = time_string.split('.')
        time_string = arr_obj_time[0]

        data_string = hr_string + ',' + str(time_string)
        data_json = {'data': data_string}
        # data_json = json.dumps(data_dict)
        # url = url_for('get_api', data=data_string )
        url = 'http://127.0.0.1:5000/post_api'
        response = requests.post(url, data=data_json)
        print(response.text)
        time.sleep(1)
        
random_data()