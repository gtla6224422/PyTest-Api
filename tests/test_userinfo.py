# tests/test_userinfo.py
import pytest
import allure

class TestUserInfo:

    @allure.feature("UserInfo API")
    @allure.story("Get user info by role - Normal Response")
    def test_get_user_info_by_role_normal(self, api_client, test_data):

        # 找到指定的测试用例出入参数据组
        test_case = next((case for case in test_data if case['name'] == "Valid role"), None)  
        if not test_case:
            pytest.fail("Test case 'Missing role' not found in test data")

        #开始执行用例函数
        for test_case in test_data:
            if test_case["expected"]["status_code"] == 200:
                # 准备测试数据
                data = test_case["input"]

                # 发送请求
                response = api_client.post("/UserInfo", data)

                # 断言
                assert response.status_code == test_case["expected"]["status_code"]
                response_data = response.json()
                #print(f"response_data:{response_data}")

                if "role" in test_case["expected"]:
                    # 使用 any 函数检查是否存在指定的 code
                    assert any(item.get("role") == test_case["expected"]["role"] for item in response_data), \
                    f"No item with code {test_case['expected']['role']} found in response"

                if "data_length" in test_case["expected"]:
                    assert len(response_data) > test_case["expected"]["data_length"]

    @allure.feature("UserInfo API")
    @allure.story("Get user info by role - Error Response")
    def test_get_user_info_by_role_error(self, api_client, test_data):
        for test_case in test_data:
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