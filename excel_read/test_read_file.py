# -*- coding = utf-8 -*-
import openpyxl
import pytest
from VAR import *
# 读取Excel里的参数
def readExcel(path,sheet):
    file = openpyxl.load_workbook(path)
    _sheet = file[sheet]
    testcase = []
    for i in _sheet.values:
        if isinstance(i[0], int):
            testcase.append(i)
    print(testcase)
    return testcase


# 对Excel的参数进行处理
def makeupData():
    data = readExcel()
    for i in data:
        #PARAMS参数
        if i[5] is not None:
            params = eval(i[5])
        # HEARDS参数
        if i[6] is not None:
            headers = eval(i[6])
        # 请求参数
        if i[7] is not None:
            data = eval(i[7])
    datalist = [params, headers, data]
    return  datalist
if __name__ == '__main__':
    readExcel()