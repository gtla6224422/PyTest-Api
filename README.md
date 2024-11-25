# pytest+fixtures+yaml

执行：
pytest --html=report.html     
根目录生成对应报告report.html

目录说明
1、tests/下以test_开头的为测试用例/场景文件，负责业务接口自动化执行
    1.1 测试用例函数包含了assert断言、jsonpath提取字段&处理、mysql查询等断言方式
2、fixtures/下的文件管理公共方法，例如调用接口的规则、读取测试数据yaml的规则
3、config/下管理测试用例数据、域名
    3.1 test_XXX_data.yaml管理用例测试数据，包含入参、期望结果
    3.2 test_config.yaml管理api域名、数据库配置
4、conftest负责管理需要导入哪些公共方法fixtures（例如api_client）

常用命令：
pytest tests/test_userinfo.py   #指定执行某个测试场景/用例

