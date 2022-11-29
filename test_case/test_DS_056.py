#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests
import allure
from intf_keywords.api_key import ApiKey


@allure.title("DS_056 删除购物车-能删除当前用户对应的购物车数据（多个）")
def test_04(fix_1):
# DS_056 删除购物车-能删除当前用户对应的购物车数据（多个）
# 01 执行登陆获取token
    with allure.step("01 执行登陆获取token"):
        ak, token = fix_1
        print(token)

# 02 加入一个商品到购物车
    with allure.step("# 02 加入一个商品到购物车"):
        data = {
            "goods_id":"10",
            "spec": "",
            "stock": 1
        }

        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }

        res = ak.post(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/save", params=params, json=data)
        print(res.json())

# 03 加入第二个商品到购物车
    with allure.step("03 加入第二个商品到购物车"):
        data = {
            "goods_id":"12",
            "spec": "",
            "stock": 1
        }

        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }

        res = ak.post(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/save", params=params, json=data)
        print(res.json())

# 03 查询购物车
    with allure.step("03 查询购物车"):
        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }
        res = ak.get(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/index", params=params, json=data)
        print(res.text)
        id_list = ak.get_text(res.text,'$..id')
        # id_list = jsonpath.jsonpath(res.json(),'$..id')
        id1 = id_list[0]
        id2 = id_list[1]
        print(id1)
        print(id2)

# 04 删除购物车
    with allure.step("04 删除购物车"):
        data = {
            "id": f"{id1},{id2}"
        }

        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }
        res = ak.get(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/delete", params=params, json=data)
        print(res.text)