import requests
import json
import sys
module_path = './backend/config/header'
if module_path not in sys.path:
    sys.path.append(module_path)
from headers_config import GetUserInfo_Header

def test_getUserInfo():
    # 登录接口的 URL
    url = 'https://angelapi.bluemoon.com.cn/portal-admin/repositoryFile/getUserInfo'

    # 构造请求数据
    payload = {}
    
    # 发送 POST 请求
    response = requests.post(url, json=payload,headers=GetUserInfo_Header)
    
    # 检查响应状态码
    assert response.status_code == 200
    
    # 解析 JSON 响应
    response_json = response.json()
    #print(response_json)
    token = response_json.get('token')
    print(token)
    
    # 打印请求信息
    #print(f"Request URL: {response.request.url}")
    #print(f"Request Headers: {response.request.headers}")
    #print(f"Request Body: {response.request.body}")

    # 打印响应信息
    #print(f"Response Status Code: {response.status_code}")
    #print(f"Response Headers: {response.headers}")
    #print(f"Response Content: {response_content}")

if __name__ == "__main__":
    #临时调试单函数用
    test_getUserInfo()