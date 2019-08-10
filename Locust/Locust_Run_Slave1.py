# coding=utf-8
import requests,json
from locust import HttpLocust, TaskSet, task
from random import randint
from Util import Login
# 定义用户行为
class AmsApi(TaskSet):
    # def on_start(self):
    #     url = "/api/login/UserLogin"
    #     headers = {
    #
    #         "Content-Type":"application/json; charset=utf-8"
    #
    #     }
    #     data=json.dumps({
    #             "Model": {
    #                 "loginName": "fza",
    #                 "password": "123456"
    #             }
    #         }
    #         )
    #
    #     self.client.post(url,data,headers=headers)
    @task
    def getmachinid(self):
        url='/api/mach/Info/QueryMyMachine'
        token=Login.getauthorization()
        headers = {

            "Content-Type":"application/json; charset=utf-8",
            "Authorization": token

        }
        data=json.dumps({
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
        )

        res=self.client.post(url,data,headers=headers)














class WebsiteUser(HttpLocust):
    task_set = AmsApi
    min_wait = 3000
    max_wait = 6000
    host = "http://ams-api.saas.shj188.com"
    #host = "http://localhost:8081"



if __name__ == "__main__":
    import os
    os.system('locust -f Locust_Run_Slave1.py --slave')

