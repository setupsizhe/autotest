# coding:utf-8
import unittest
import ddt
import requests
import os
import logging

import yaml
import sys

cur_path=os.path.dirname(os.path.realpath(__file__))
yaml_path=os.path.join(cur_path,'D://untitled6//conf//canshu')
datas2=open(yaml_path,'r',encoding='UTF-8')
testdata2=yaml.load(datas2,Loader=yaml.FullLoader)
print(testdata2)