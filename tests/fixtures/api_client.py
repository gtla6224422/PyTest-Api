# tests/fixtures/api_client.py
from pymysql.cursors import DictCursor
import pytest
import requests
import yaml
import pymysql


# 创建 API请求公共方法
@pytest.fixture(scope="session")
def api_client():
    with open("config/test_config.yaml", "r") as file:
        config = yaml.safe_load(file)
    base_url = config["base_url"]
    
    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url
        
        def post(self, endpoint, data):
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, json=data)
            return response
    
    return APIClient(base_url)
# 从 YAML 文件中加载用例数据
@pytest.fixture(scope="session")
def load_userinfo_data():
    with open("config/test_userinfo_data.yaml", "r") as file:
        return yaml.safe_load(file)["userinfo_case"]
    
                                            ######mysql操作相关######
# 从 YAML 文件中加载数据库配置信息
def load_mysqlconfig():
    """从 YAML 文件中加载mysql配置信息"""
    with open("config/test_config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config['database']

# 连接数据库公共方法
@pytest.fixture(scope="session")
def db_connection():
    sqlconfig = load_mysqlconfig()
    print(f"Database config is {sqlconfig}")

    """创建并返回数据库连接"""
    conn = pymysql.connect(
        host=sqlconfig['host'],
        user=sqlconfig['user'],
        password=sqlconfig['password'],
        db=sqlconfig['db'],
        charset=sqlconfig['charset'],
        cursorclass=DictCursor  # 直接使用导入的 DictCursor
    )
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def execute_query(db_connection):
    """执行 SQL 查询并返回结果"""
    def _execute_query(query):
        cursor = db_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result
    return _execute_query