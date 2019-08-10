# coding=utf-8
import json
from locust import HttpLocust, TaskSet, task
from Util import Login
from Locust import LocustMach
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
    def QueryMyMachine(self):
        #LocustMach.mach_Info_QueryMyMachine()
        #LocustMach.Pay_SxfMerchant_AddSbMerchantOld()
        pass







class WebsiteUser(HttpLocust):
    task_set = AmsApi
    min_wait = 3000
    max_wait = 6000
    host = "http://ams-api.saas.shj188.com"



if __name__ == "__main__":
    import os
    #os.system("locust -f locustTest.py --host=http://www.baidu.com")
    os.system("locust -f locustTest.py")
    #no-web模式运行
    #os.system("locust -f locustTest.py --no-web -c 1 -r 1 -t 5s")

