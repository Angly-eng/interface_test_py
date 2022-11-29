#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests
import allure

from intf_keywords.api_key import ApiKey

@allure.title("DS_025 验证输入错误的用户名提示用户")
def test_03():
# DS_025 验证输入错误的用户名提示用户
    ak = ApiKey()
    with allure.step("DS_025 验证输入错误的用户名提示用户"):
        data = {
            "accounts": "!@#$%^&*(",
            "pwd": "123456",
            "type": "username"
        }
        params = {
            "application": "app",
            "application_client_type": "weixin"
        }
        res = ak.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/reg", json=data, params=params)
        print(res.text)