import json

import requests
import json

url = 'http://localhost:6061/uam/user/loginByPhone'  # 上传文件的URL
headers = {'Content-Type': 'application/json'}
data = {'phone': '13112345678', 'password': 'admin1'}  # phone + password

response = requests.post(url, headers=headers, json=data)  # 发送post请求

print(response.text)  # 打印服务器返回的响应内容

response_json = response.json()
print(response_json['data']['accessToken'])


