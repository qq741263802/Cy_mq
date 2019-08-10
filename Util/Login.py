#coding:utf-8
import requests,json

url = 'http://ams-api.saas.shj188.com/api/login/UserLogin'
data = {
	"Model": {
		"loginName": "cxh",
		"password": "123456"
	}
}
def amslogin():
    ld=requests.post(url=url,json=data).json()
    return  ld['Data']['token']


def getauthorization():
	token = amslogin()
	authorization = "Bearer " + token
	return authorization




def gettoken():
    token = amslogin()
    headers = {

        "Authorization": "Bearer " + token

    }
    return headers





