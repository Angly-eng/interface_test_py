# -*- coding = utf-8 -*-
import pytest
import allure
from intf_keywords.api_key import ApiKey
from excel_read.test_read_file import readExcel
from VAR import *
# 读取文件信息

def setup_module():
    global ak, excel_data, all_values
    # 初始化工具类
    ak = ApiKey()
    # 设置字典保存接口关联信息
    all_values = {}

# 读取并执行测试用例
# 接受Excel读取的数据，参数化执行测试用例
@pytest.mark.parametrize('data',readExcel(PATH, SHEET))
def test_01(data):
    # 用例名
    allure.dynamic.title(data[11])
    # 小模块
    if data[16] is not None:
        allure.dynamic.story(data[16])
    # 大模块
    if data[17] is not None:
        allure.dynamic.feature(data[17])
    # 备注
    if data[18] is not None:
        allure.dynamic.description(data[18])
    # 用例级别
    if data[19] is not None:
        allure.dynamic.severity(data[19])
    # 参数拼接
    ak = ApiKey()
    # PARAMS参数
    if data[4] is not None:
        param = eval(data[4])
        print(param)
        print(type(param))
    # HEARDS参数
    if data[5] is not None:
        header = eval(data[5])
        print(header)
        print(type(header))
    # 请求参数
    if data[6] is not None:
        jdata = eval(data[6])
        print(jdata)
        print(type(jdata))

    # 返回报文详情
    try:
        res = getattr(ak, data[3])(url=data[1]+data[2], params=param, json=jdata, headers=header)
    except Exception as e:
        print("==================请求参数有误===================")
        print(e)
    finally:
        print(res.text)


    # 结果校验:实际结果==预期结果
    expected = data[9]
    reality = ak.get_text(res.text, data[8])
    assert expected != reality, "返回结果与预期结果不符"

    # 接口关联信息获取
    temp_dict = ak.joinlist(data[12], data[13])
    all_values.update(temp_dict)


if __name__ == '__main__':
    if __name__ == '__main__':
        pytest.main(['-vs','./test_exce_main.py'])
