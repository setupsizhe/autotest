import pytest
import requests
import json
import yaml
import os
from common import request

cur_path=os.path.dirname(os.path.realpath(__file__))
yaml_path=os.path.join(cur_path,'D://untitled6//conf//canshu')
datas2=open(yaml_path,'r',encoding='UTF-8')
testdata2=yaml.load(datas2,Loader=yaml.FullLoader)


@pytest.mark.parametrize('url',testdata2)
# def test_yy(url):
#     print(type(url),'\n{}\n'.format(url))
def test_dic(url):
    s = requests.session()
    res = request.send_requests(s,url)
    res_text=res['text']
    print(res_text)
    # print("检查点->：%s"%check)
    check=url['checkpoint']
    # print("返回实际结果->：%s"%res_text)
    # for i in res:
    #     print(res['times'])
    if not res_text:
        assert check in res_text

def test_three(token):

    r = requests.get(url='http://221.179.136.72:33200/EPG/interEpg/user/default/authorize',
                  headers={'Authorization': token}
                   )
    print(r.json())
    assert (r.status_code==200)
if __name__=='__main__':
    pytest.main(['-s ','test_class.py'])

