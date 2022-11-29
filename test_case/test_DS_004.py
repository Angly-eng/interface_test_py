#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

import allure
from VAR import *
from deepdiff import DeepDiff
from intf_keywords.api_key import ApiKey
# DS_004 商品详情-验证输入的商品ID不存在提示用户
# 01 执行登陆获取token
print(DeepDiff(s,a, i))
@allure.title("DS_004 商品详情-验证输入的商品ID不存在提示用户")
def test_01(fix_1):
    with allure.step("01 执行登陆获取token"):
        ak, token = fix_1
        print(token)

# 02 查询商品详情10是有的，101是没有的
    with allure.step("02 查询商品详情10是有的，101是没有的"):
        data = {
            "goods_id": 101
        }
        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }
        api = "api/goods/detail"
        url = URL+"?s="+api
        res = ak.post(url=url, params=params, json=data)
        print(res.text)
if __name__ == '__main__':
    pytest.main(['-sv','./test_DS_004.py'])
