# -*- coding: utf-8 -*-
import requests, time, json, uuid, datetime, re
from SQLdb import DbContext, Message,Huodao,Info
from Util import Login
url1 = 'http://ams-api.saas.shj188.com/api/mach/Huodao/AddHuodaoModel'
url2 = 'http://ams-api.saas.shj188.com/api/item/goods/HuodaoGoodsSave'



def FuDai():
    headers = Login.gettoken()
    info = Info.Machine_info
    db = DbContext.dbSession(info.db).query(info).filter(info.MachineCode == 'M31023')
    for i in db:
        MachineID = i.Code
    i = 1
    while i < 9:
        if i < 10:
            SerialPort = "01-0" + str(i)
        else:
            SerialPort = "01-" + str(i)

        data = {
            "Model": {
                "SerialPort": SerialPort,
                "HuodaoNumber": 5,
                "Sort": i,
                "MachineID": MachineID
            }
        }
        resone = requests.post(url=url1, json=data, headers=headers)

        hd = Huodao.Machine_huodao
        db = DbContext.dbSession(hd.db).query(hd).filter(hd.MachineId == MachineID, hd.SerialPort == SerialPort)
        for k in db:
            HuodaoCode = k.Code

        data2 = {
            "Model": {
                "MachineID": MachineID,
                "SerialPort": SerialPort,
                "HuodaoCode": HuodaoCode,
                "ProductCode": None,
                "Title": "幸运福袋",
                "SalePrice": "0.1",
                "Cost": "0.05",
                "HuodaoNumber": 5,
                "Inventory": 5,
                "Sort": i,
                "PicCode": "f6a0e0bc874941a9ac47803bfd0f889e",
                "PicUrl": "https://img.saas.shj188.com/AAEAAQAAAAAAAAAAAAAAJDJjYzIzN2NkLTY5MzUtNDFlOC1hMjZmLWJhMDE1MDM0OTY0OQ",
                "PicUrlHttp": "https://img.saas.shj188.com/AAEAAQAAAAAAAAAAAAAAJDJjYzIzN2NkLTY5MzUtNDFlOC1hMjZmLWJhMDE1MDM0OTY0OQ",
                "CateName": "测试类目",
                "SaleType": 0,
                "HuodaoType": 0,
                "CertPhotoCO": {
                    "1562211457535": {
                        "id": "f6a0e0bc874941a9ac47803bfd0f889e",
                        "url": "/AAEAAQAAAAAAAAAAAAAAJDJjYzIzN2NkLTY5MzUtNDFlOC1hMjZmLWJhMDE1MDM0OTY0OQ",
                        "oldname": "微信截图_20190507150154.png"
                    }
                }
            }
        }
        dare = requests.post(url=url2, json=data2, headers=headers)
        i += 1

def Gezi():
    headers=Login.gettoken()
    info = Info.Machine_info
    db = DbContext.dbSession(info.db).query(info).filter(info.MachineCode == 'M31030')
    for i in db:
        MachineID = i.Code
    i = 1
    Sort = 0
    while i < 50:
        j=1
        while j<=3:
            Sort+=1
            if i<10:
                SerialPort = "0" + str(i) + "-0" + str(j)
            else:
                SerialPort =str(i) + "-0" + str(j)
            data = {
                "Model": {
                    "SerialPort": SerialPort,
                    "HuodaoNumber": 5,
                    "Sort": Sort,
                    "MachineID": MachineID
                }
            }
            resone = requests.post(url=url1, json=data, headers=headers)

            hd = Huodao.Machine_huodao
            db = DbContext.dbSession(hd.db).query(hd).filter(hd.MachineId == MachineID, hd.SerialPort == SerialPort)
            for k in db:
                HuodaoCode = k.Code

            data2 = {
                "Model": {
                    "MachineID": MachineID,
                    "SerialPort": SerialPort,
                    "HuodaoCode": HuodaoCode,
                    "ProductCode": None,
                    "Title": "幸运福袋",
                    "SalePrice": "0.1",
                    "Cost": "0.05",
                    "HuodaoNumber": 5,
                    "Inventory": 5,
                    "Sort": Sort,
                    "PicCode": "f6a0e0bc874941a9ac47803bfd0f889e",
                    "PicUrl": "https://img.saas.shj188.com/AAEAAQAAAAAAAAAAAAAAJDJjYzIzN2NkLTY5MzUtNDFlOC1hMjZmLWJhMDE1MDM0OTY0OQ",
                    "PicUrlHttp": "https://img.saas.shj188.com/AAEAAQAAAAAAAAAAAAAAJDJjYzIzN2NkLTY5MzUtNDFlOC1hMjZmLWJhMDE1MDM0OTY0OQ",
                    "CateName": "测试类目",
                    "SaleType": 0,
                    "HuodaoType": 0,
                    "CertPhotoCO": {
                        "1562211457535": {
                            "id": "f6a0e0bc874941a9ac47803bfd0f889e",
                            "url": "/AAEAAQAAAAAAAAAAAAAAJDJjYzIzN2NkLTY5MzUtNDFlOC1hMjZmLWJhMDE1MDM0OTY0OQ",
                            "oldname": "微信截图_20190507150154.png"
                        }
                    }
                }
            }
            res = requests.post(url=url2, json=data2, headers=headers)
            j+=1


        i += 1



Gezi()
