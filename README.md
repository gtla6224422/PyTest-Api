# pytest+fixtures+yaml

执行pytest后，根目录生成对应报告

目录结构：
project/
├── tests/
│   ├── conftest.py
│   ├── test_userinfo.py
│   └── fixtures/
│       └── api_client.py
├── config/
│   ├── test_config.yaml
│   └── test_data.yaml
└── requirements.txt

1、tests/下以test_开头的为测试用例/场景文件，负责业务接口自动化执行
2、fixtures/下的文件管理公共方法，例如调用接口的规则、读取测试数据yaml的规则
3、config下管理测试用例数据、域名
4、conftest负责管理需要导入哪些fixtures（例如api_client）