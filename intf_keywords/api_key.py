# -*- coding = utf-8 -*-
import allure
import requests
import json
import jsonpath
import pymysql

class ApiKey:

    @allure.step("发送get请求")
    def get(self, url, json, params, **kwargs):
        return requests.get(url=url, json=json, params=params, **kwargs)

    @allure.step("发红POST请求")
    def post(self, url, json, params, **kwargs):
        return requests.post(url=url, json=json, params=params, **kwargs)

    @allure.step("获取返回的结果")
    def get_text(self,response, path):
        """
        :param response: 返回的响应信息，默认为json格式
        :param jsonpath: jsonpath提取
        :return:

        """
        dict_data = json.loads(response)
        return jsonpath.jsonpath(dict_data, path)


    @allure.step("获取需获取的接口关联信息（keys和values）")
    def joinlist(self,list1, list2):
        '''
        :param list1: json键值名列表
        :param list2: json values列表
        :return:        {键值: values}
        '''
        if list1:
        # 分割Key值
            varKey = list1.split(';')
        else:
            return {}
        if list2:
        # 分割Values
            varValues = list2.split(';')
        # 组装成新字典并返回
            return {i: j for i in varKey for j in varValues}

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


if __name__ == '__main__':
    ak = ApiKey()
    # params = {
    #     "application": "app",
    #     "application_client_type": "weixin"
    # }
    # data = {
    #     "accounts": "zz",
    #     "pwd": "123456",
    #     "type": "username"
    # }
    # res = ak.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",json=data,params=params)
    # #print(res.json()["msg"])
    # result = ak.get_text(res.text, "$.msg")
    # print(result)
    result = ak.sqlCheck("select * from sxo_power")
    print(result)

