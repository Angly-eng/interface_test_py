#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import jsonpath
import requests

# DS_010 用户名为不超过7位，注册成功
from intf_keywords.api_key import ApiKey


@allure.title("DS_010 用户名为不超过7位，注册成功")
def test_02():
    ak = ApiKey()
    data = {
        "accounts": "JOJO001",
        "pwd": "123456",
        "type": "username"
    }
    params = {
        "application": "app",
        "application_client_type": "weixin"
    }
    res = ak.get(url="http://shop-xo.hctestedu.com/index.php?s=api/user/reg", json=data, params=params)
    print(res.text)