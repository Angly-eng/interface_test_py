# -*- coding = utf-8 -*-
from deepdiff import DeepDiff
import os


path1 = r'C:\ProgramData\Jenkins\.jenkins\workspace\git20221129-Allure\main.py'
path2 = r'D:\shanchu\interface_demo\main.py'
f1 = open(path1, 'r', encoding='utf-8').read()
f2 = open(path2, 'r', encoding='utf-8').read()
a = DeepDiff(f1, f2).pretty()
print(a)