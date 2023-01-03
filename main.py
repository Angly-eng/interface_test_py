# -*- coding = utf-8 -*-
import os
import pytest

if __name__ == '__main__':

    # pytest写测试用例
    # pytest.main(['-v', './test_case', '--alluredir','./result','--clean-alluredir'])
    # os.system("allure serve result")

    # excel写测试用例
    # excel文件地址
    path = r'D:\shanchu\interface_demo\excel_read\testcase_file\test_exce_main.py'
    pytest.main(['-v', '--alluredir' ,'./result', '--clean-alluredir', path])
    os.system("allure serve result")
    os.system("allure generate ./result -o ./report")

    # jenkins运行时输入以下句子(指定需要执行的测试用例范围)
    # python -s test_exce_main.py --alluredir ./allure_report

