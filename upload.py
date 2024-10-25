import requests

login_url = 'http://localhost:6061/uam/user/loginByPhone'
login_headers = {'Content-Type': 'application/json'}
login_data = {'phone': '13112345678', 'password': 'admin1'}  # phone + password
login_response = requests.post(login_url, headers=login_headers, json=login_data)  # 发送post请求
login_response_json = login_response.json()

url = 'http://localhost:6061/uam/terminal/uploadLog'  # 上传文件的URL
filename = 'D:/error.log'  # 待上传的文件

# headers = {'accessToken':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IjE4MzkxNDkwNDI1NjM2ODIzMDQiLCJ1c2VyQmlkIjoiMSIsInN1YiI6IjEiLCJleHAiOjE3Mjk5MzI0MzMsIm5iZiI6MTcyOTg0NjAzM30.Rg1NIztTGA8sHzq6a-lYEcRpjDIVAZIYs_h4TTTJmaM'}  # 设置请求头
headers = {'accessToken':login_response_json['data']['accessToken']}  # 设置请求头

data = {'terminalBid': '1711387127163523072'}  # 终端bid

files = {'file': open(filename, 'rb')}  # 设置文件数据

response = requests.post(url, files=files, data=data, headers=headers)  # 发送post请求

print(response.text)  # 打印服务器返回的响应内容
