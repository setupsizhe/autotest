import pytest
import requests
import json

def login():
    print('请输入账号密码：')
    yield
    print('关闭浏览器')

#获取token#
@pytest.fixture(scope="module")
def token():
    re=requests.get(url='http://221.179.136.72:33200/EPG/oauth/v2/token?authinfo=D655860FBD5D574F98C460238C14DCFA4564E56940ED0D774B97CDB3B20D7C8F9451DDE255317720D407D05A6F2824C40207AF8C300A10C6E55EF1896B0F45F6362A97DB7BDBE3955399FCB063D58B48EF7AC40A9295033E875D2CE5075FDF4F7B64534809674F22D0085048F85CDBF7A4C5A223E8C242A0FAAE617C2445155E8ABA7EFD625BAFF7&UserID=54C57AE64D78&DeviceVersion=002.323.003&client_id=android&DeviceType=CM201-2&grant_type=EncryToken').json()

    return re['access_token']

