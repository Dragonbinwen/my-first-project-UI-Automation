# 存储项目的配置信息，项目地址、用户名、密码...
# 项目环境名 -> 项目的配置信息 ？ 这种数据通过python的什么类型来存储
# key -> value  字典嵌套字典
env_dict = {
    'test':{
        'url':'http://mall.lemonban.com:3344/',
        'username':'lemonban001',
        'password':'lemon123456'
    },
    'dev':{
        'url':'http://dev.lemonban.com:3344/',
        'username':'lemonban002',
        'password':'lemon123456'
    },
    'pre':{
        'url': 'http://pre.lemonban.com:3344/',
        'username': 'lemonban003',
        'password': 'lemon123456'
    }
}
print(env_dict['test']['url'])
