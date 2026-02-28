# ==========项目运行主入口文件============
import sys

import pytest
from loguru import logger

# 日志保存到本地的文件中（持久化存储），将其放到run.py主运行文件中，这样的运行run.py的时候就能够加载这些日志的初始化配置
logger.add(sink="my.log",
           encoding="utf8",
           level="INFO",
           rotation="10MB",
           retention=20)

if len(sys.argv) > 1:
    env_name = sys.argv[1]
else:
    env_name = 'test' # 默认环境为test
# --clean-alluredir 清理上次执行用例产生的Allure报告数据，避免报告的数据的重叠
pytest.main(['-s','-v','--alluredir=output/allure-results','--clean-alluredir',f'--env={env_name}'])