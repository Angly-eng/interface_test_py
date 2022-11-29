# -*- coding = utf-8 -*-
from deepdiff import DeepDiff
import os


file = '\main.py'
path1 = r'C:\ProgramData\Jenkins\.jenkins\workspace\git20221129-Allure'
path2 = r'D:\shanchu\interface_demo'
print(path1+file)
f1 = open(path1+file,'r', encoding='utf-8').read()
f2 = open(path2+file, 'r', encoding='utf-8').read()
a = DeepDiff(f1, f2).pretty()
print(a)