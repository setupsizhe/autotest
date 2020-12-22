import pytest
import requests
import json
import yaml
import os
import allure_pytest
import allure
import sys
import allure_commons
from common import request
from duqu.readexcel import ExcelUtil

testdata2= ExcelUtil(excelPath='/Users/liusizhe/PycharmProjects/接口自动化项目/duqu/test.xlsx', sheetName="Sheet1").dict_data()
# sys.path.append('/Users/liusizhe/PycharmProjects/接口自动化项目/duqu/test.xlsx')
@allure.story("登录用例")
@pytest.mark.parametrize('url',testdata2)

def test_dic(url):
    res = request.send_requests(url)
    res_text=res['statuscode']
    print(res_text)
    # print("检查点->：%s"%check)
    check=url['checkpoint']
    print(check)
    # print("返回实际结果->：%s"%res_text)
    # for i in res:
    #     print(res['times'])

    assert check != res_text

# def test_three(token):
#
#     r = requests.get(url='http://221.179.136.72:33200/EPG/interEpg/user/default/authorize',
#                   headers={'Authorization': token}
#                    )
#     print(r.json())
#     assert (r.status_code==20
if __name__=='__main__':
    pytest.main(['-s ','test_login.py'])

