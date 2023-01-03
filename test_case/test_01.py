# -*- coding = utf-8 -*-
import allure

from intf_keywords.api_key import ApiKey

@allure.title("登录流程")
def test_login():
    params = {
        "application": "app",
        "application_client_type": "weixin"
    }
    data = {
        "accounts": "zz",
        "pwd": "123456",
        "type": "username"
    }
    ak = ApiKey()
    res = ak.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login", json=data, params=params)
    # print(res.json()["msg"])
    result = ak.get_text(res.text, "$.msg")
    print(result)
if __name__ == '__main__':
    test_login()
