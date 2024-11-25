# tests/test_userinfo.py
import pytest
import allure
import jsonpath_ng
import pymysql

class TestUserInfo:

    global con_username
    @allure.feature("UserInfo API")
    @allure.story("UserInfo-正常返回200")
    def test_userinfo_normal(self, api_client, load_userinfo_data,execute_query):
        #定义一些全局变量，用于不同函数直接参数传递

        # 找到指定的测试用例出入参数据组
        test_case = next((case for case in load_userinfo_data if case['name'] == "Valid role"), None)  
        if not test_case:
            pytest.fail("Test case 'Missing role' not found in test data")

        #开始执行用例函数
        for test_case in load_userinfo_data:
            if test_case["expected"]["status_code"] == 200:
                # 准备测试数据
                data = test_case["input"]
                # 发送请求
                response = api_client.post("/UserInfo", data)
                response_data = response.json()
                #print(f"response_data:{response_data}")

                # 断言
                assert response.status_code == test_case["expected"]["status_code"]

                if "role" in test_case["expected"]:
                    # 使用 any 函数检查是否存在指定的 code
                    assert any(item.get("role") == test_case["expected"]["role"] for item in response_data), \
                    f"No item with code {test_case['expected']['role']} found in response"

                if "data_length" in test_case["expected"]:
                    assert len(response_data) > test_case["expected"]["data_length"]
                

    @allure.feature("UserInfo API")
    @allure.story("UserInfo-jsonpath提取字段与mysql查询字段做对比")
    def test_userinfo_json(self, api_client, load_userinfo_data,execute_query):

        # 找到指定的测试用例出入参数据组
        test_case = next((case for case in load_userinfo_data if case['name'] == "Valid role"), None)  
        if not test_case:
            pytest.fail("Test case 'Missing role' not found in test data")

        #开始执行用例函数
        for test_case in load_userinfo_data:
            if test_case["expected"]["status_code"] == 200:
                # 准备测试数据
                data = test_case["input"]
                # 发送请求
                response = api_client.post("/UserInfo", data)
                response_data = response.json()
                #print(f"response_data:{response_data}")

                # 定义 JSONPath 表达式
                json_path = jsonpath_ng.parse('$.[*].id')
                # 提取所有 id 字段
                ids = [match.value for match in json_path.find(response_data)]
                # 检查是否存在 id 等于 7 的记录（指定值是否存在于jsonpath表达式返回体中）
                assert 7 in ids, "No item with id 1 found in response data"

                # 提取 id 为 7 的结构体中的 role 字段（列表推导式）
                matching_items = [item for item in response_data if item.get("id") == 7]
                # 检查是否找到匹配的 role 字段
                if matching_items:
                # 提取 username 字段
                    con_username = matching_items[0].get("username")
                    con_id = matching_items[0].get("id")
                    print(f"Extracted role: {con_username}")
                else:
                    pytest.fail("No item with id 7 found in response data")

                # 执行 SQL 查询
                sql = "SELECT x.* FROM web_demo.user_tbl x WHERE id = 7 LIMIT 1"
                result = execute_query(sql)

                # 检查查询结果是否存在
                if result:
                # 提取 username 字段，并判断接口返回的结构中con_username是否等于数据库表查询结果的username
                    db_username = result.get("username")
                    # 检查是否找到匹配的结构体
                    assert con_username == db_username, f"API username {con_id} does not match database username {db_username}"

                else:
                    pytest.fail("No record with id 7 found in the database")
                

    @allure.feature("UserInfo API")
    @allure.story("Get user info by role - Error Response")
    def test_get_user_info_by_role_error(self, api_client, load_userinfo_data):
        for test_case in load_userinfo_data:
            if test_case["expected"]["status_code"] != 200:
                # 准备测试数据
                data = test_case["input"]

                # 发送请求
                response = api_client.post("UserInfo", data)

                # 打印响应数据以调试
                print(f"Response data: {response.json()}")

                # 断言
                response_data = response.json()
                try:
                    if isinstance(response_data, list):
                        assert any(item.get("error") for item in response_data), \
                               f"No item with non-empty error field found in response data"
                    else:
                        assert response_data.get("error"), f"Error field is empty in response data: {response_data}"
                except AttributeError as e:
                    pytest.fail(f"Unexpected response data format: {e}")