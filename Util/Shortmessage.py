
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError


# 短信应用 SDK AppID
appid = 1400254386
# 短信应用 SDK AppKey
appkey = "bafc76f7b6ce3d91acc82825f3b5dfd7"
# 需要发送短信的手机号码
phone_numbers = ["13535485194"]
# 短信模板ID，需要在短信控制台中申请
template_id = 7839
# 签名
sms_sign = "腾讯云"


sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
ssender = SmsSingleSender(appid, appkey)
try:
  result = ssender.send(sms_type, 86, phone_numbers[0],
      "【腾讯云】您的验证码是: 5678", extend="", ext="")
except HTTPError as e:
  print(e)
except Exception as e:
  print(e)

print(result)

