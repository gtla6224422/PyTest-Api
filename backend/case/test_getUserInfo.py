import requests
import json

def test_getUserInfo():
    # 登录接口的 URL
    url = 'https://angelapi.bluemoon.com.cn/portal-admin/repositoryFile/getUserInfo'
    # 构造请求数据
    payload = {
    }
    
    # 发送 POST 请求
    response = requests.post(url, json=payload)
    
    # 检查响应状态码
    assert response.status_code == 200
    
    # 解析 JSON 响应
    data = response.json()
    
    # 检查响应中是否存在 token 字段
    assert 'token' in data
    
    # 提取 token 字段并进行断言
    token = data['token']
    assert isinstance(token, str), "Token should be a string"
    assert len(token) > 0, "Token should not be empty"
    
    # 使用提取的 token 进行其他操作，例如发送另一个请求
    headers = {'Authorization': f'Bearer {token}'}
    response_auth = requests.get('http://example.com/api/protected', headers=headers)
    
    # 检查保护接口的响应
    assert response_auth.status_code == 200