# -*- coding = utf-8 -*-
import allure
import requests
import json
import jsonpath
import pymysql
import hashlib
import re
import warnings
#warnings.filterwarnings('ignore')
class ApiKey:

    # GET请求
    @allure.step("发送get请求")
    def get(self, url, json, params, **kwargs):
        return requests.get(url=url, json=json, params=params, **kwargs)

    # POST请求
    @allure.step("发红POST请求")
    def post(self, url, json, params, **kwargs):
        return requests.post(url=url, json=json, params=params, **kwargs)

    # json提取器
    @allure.step("获取返回的结果")
    def get_text(self,response, path):
        """
        :param response: 返回的响应信息，默认为json格式
        :param jsonpath: jsonpath提取
        :return:语法正确时以列表形式返回内容，错误时返回False

        """
        dict_data = json.loads(response)
        return jsonpath.jsonpath(dict_data, path)

    # reg提取器
    @allure.step("进行正则匹配")
    def regular_assert(self, txt, pattern):
        result = re.search(pattern, txt)
        print(f"正则匹配结果为{result.group(1)}")

    # 提取excel中的所需的关联信息
    @allure.step("获取需获取的接口关联信息（keys和values）")
    def joinlist(self, txt, list1, list2):
        '''
        :param list1: json键值名列表
        :param list2: json values列表
        :return:        {键值: values}
        '''
        var = []
        if list1:
            # 分割Key值
            varKey = list1.split(';')
        else:
            return {}
        if list2:
            # 分割Values
            varValues = list2.split(';')
            print('varValues值为',varValues)
        # 获取报文中varValues对应的json值，并赋值到varKey
        for varValue in varValues:
            result = self.get_text(txt, varValue)
            print(result[0])
            var.append(result[0])
            print('var=', var)
        # 组装成新字典并返回{varKey[i]:var[i]}
        if len(varKey) != len(var):
            raise IndexError("变量名与变量值个数不相等，请检查修改")
        else:
            return {varKey[i]:var[i] for i in range(len(varKey))}

    # 数据库校验
    @allure.step("数据库检查")
    def sqlCheck(self, sql, n=1):
        conn = pymysql.connect(
            host='shop-xo.hctestedu.com',
            port=3306,
            user='api_test',
            password='Aa9999!',
            database='shopxo_hctested',
            charset='utf8'
        )
        # 设置游标对象
        cmd = conn.cursor()

        # 执行sql语句
        cmd.execute(sql)
        # 返回执行结果
        return cmd.fetchmany(n)

    # MD5加密 不可逆
    @allure.step("MD5单向加密")
    def get_md5(self, str, salt=''):
        obj = hashlib.md5(salt.encode('utf-8'))
        obj.update(str.encode('utf-8'))
        result = obj.hexdigest()
        return result

    # DES加密
    @allure.step("des加密")
    def get_md5(self, str, salt=''):
        


if __name__ == '__main__':
    ak = ApiKey()
    # 调试：json提取器
    params = {
        "application": "app",
        "application_client_type": "weixin"
    }
    data = {
        "accounts": "zz",
        "pwd": "123456",
        "type": "username"
    }
    res = ak.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",json=data,params=params)
    #print(res.json()["msg"])
    result = ak.get_text(res.text, "$.msg")
    print(result[0])

    # 调试：数据库检核
    # result = ak.sqlCheck("select * from sxo_power")

    # 调试：md5加密
    #result = ak.get_md5("测试")
    #print(result)

