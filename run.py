#-*-coding:utf-8 -*-
#@Time:2026-02-1116:44
#@Auth:Mark
#@File:run.py

import sys
import pytest

# 原来的代码可能有这样的结构：
# env_name = sys.argv[1]  # 这行会报错

# 修改为：
if len(sys.argv) > 1:
    env_name = sys.argv[1]
else:
    # 如果没有参数，使用默认值
    env_name = "test"  # 或者 "dev"、"prod"等，根据你的需要
    print(f"未指定环境参数，使用默认环境: {env_name}")

# 继续你的其他代码...
# 例如根据环境加载不同配置
if env_name == "test":
    # 加载测试环境配置
    pass
elif env_name == "prod":
    # 加载生产环境配置
    pass

# 运行pytest测试
pytest.main()