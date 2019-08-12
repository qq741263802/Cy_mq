
# coding=utf-8
import requests,json,time,uuid
from Util import Login,common

headers = {

    "Content-Type": "application/json; charset=utf-8",
    "Authorization": Login.getauthorization()

}
def mach_Info_QueryMyMachine():
    url = common.host+'/api/mach/Info/QueryMyMachine'
    data = {
        "model": {
            "page": 1,
            "pageSize": 10,
            "filters": [],
            "sorts": [{
                "field": "Created",
                "isAsc": False
            }]
        }
    }

    res=requests.post(url=url,json=data,headers=headers).json()
    common.assertEqual('Message','s操作完成',res)











def Pay_SxfMerchant_AddSbMerchantOld():
    url = common.host+'/api/Pay/SxfMerchant/AddSbMerchantOld'
    data = {
	"Model": {
		"MerchantName": "随行付商户测试",
		"MerchantNo": str(uuid.uuid1()),
		"TaskCode": "123456789kkkkk"
	}
}
    res=requests.post(url=url,json=data,headers=headers).json()





mach_Info_QueryMyMachine()







