# -*- coding: utf-8 -*-
import requests,time,json,uuid,datetime,re
from SQLdb import DbContext,Message
t=int(time.time())
url='http://mobile-api.saas.shj188.com/api/M30944/HOrder/GetHaiOrderAwardRes'
headers={

"uuid":"e0cdc6c5dd3440e4b788415c36afd2d8"


}
data={
		"Model": {
			"OrderCode": "HOD3531",
			"HuodaoId": ""
		}
	}



id = uuid.uuid1()
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
old = requests.post(url=url, json=data,headers=headers)
#d = json.loads(old.text).replace('\'', '')
list = Message.Test_message(id=str(uuid.uuid1()),
                            message='yyyyy',
                            created=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            )



	

#
# db= DbContext.dbSession(list.db)
# db.add(list)
# db.commit()
# db.close()


