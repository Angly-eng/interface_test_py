# -*- coding = utf-8 -*-
import allure
import pytest
from VAR import *
from intf_keywords.api_key import ApiKey


#@pytest.fixture(scope="session")
def fix_1():
    params = {
        "application": "app",
        "application_client_type": "weixin"
    }
    data = {
        "accounts": USRNAME,
        "pwd": PWD,
        "type": "username"
    }
    ak = ApiKey()
    api = "s=api/user/login"
    with allure.step(f"登录账户:{USRNAME}"):
        res = ak.post(url=URL+"?"+api, json=data, params=params)
    # print(res.json()["msg"])
    with allure.step(f"获取{USRNAME}账户的token"):
        token = ak.get_text(res.text, "$..token")[0]
    # 正则匹配
    # ak.regular_assert(res.text, r'"token":"(.*?)"')
    print(res.text)
    print(token)
    return ak, token

if __name__ == '__main__':
    fix_1()