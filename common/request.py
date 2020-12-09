# coding:utf-8
import requests
import os
from duqu.readexcel import ExcelUtil

def send_requests(testdata):
    '''封装requests请求'''
    method = testdata["method"]
    url = testdata["url"]
    # url后面的params参数
    try:
        params = testdata["params"]
    except:
        params = None
# 请求头部headers
    header=eval(testdata["headers"])

    test_nub = testdata['ID']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)
    print("请求headers: %s"%header)


    # try:
    #     bodydata = testdata["body"]
    # except:
    #     bodydata = {}
    #
    # # 判断传data数据还是json
    # if type == "data":
    #     body = bodydata
    # elif type == "json":
    #     body = json.dumps(bodydata)
    # else:
    #     body = bodydata
    # if method == "post": print("请求body类型为：post" )

    # verify = False
    res = {}   # 接受返回数据
    # if method=='GET'

    r = requests.request(method=method,
                  url=url,
                  params=params,
                  headers=header
                   )
    print("页面返回信息：%s" % r.content.decode("utf-8"))
    res['id'] = testdata['ID']
    res['rowNum'] = testdata['rowNum']


    res["statuscode"] = str(r.status_code)  # 状态码转成str
    res["text"] = r.content.decode("utf-8")
    # print(res["text"])
    res["times"] = str(r.elapsed.total_seconds())
    # 接口请求时间转str
    if res["statuscode"] != "200":
        res["error"] = res["text"]
        print(res["text"])
    else:
        res["error"] = ""
        # print(res["text"])
    res["msg"] = ""
    if testdata["checkpoint"] in res["text"]:
        res["result"] = "pass"
        print("用例测试结果:   %s---->%s" % (test_nub, res["result"])+'\n\n')
    else:
        res["result"] = "fail"
        print("用例测试结果:   %s---->%s" % (test_nub, res["result"]) + '\n\n')
    return res

if __name__ == "__main__":
    data = ExcelUtil(excelPath='test.xlsx', sheetName="Sheet1").dict_data()
    send_requests(data[0])
    print(os.path.abspath(os.path.realpath(__file__)))




