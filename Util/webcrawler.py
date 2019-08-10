from requests_html import HTMLSession
from SQLdb import DbContext,Message
from Util import common
import requests
session = HTMLSession()

# 获取页面上的所有链接，以绝对路径的方式。
def getwww(url):
    r = session.get(url)
    all_absolute_links = r.html.absolute_links
    return all_absolute_links
    #dbseesion = DbContext.dbSession(Message.Test_message.db)
    # for res in all_absolute_links:
    #     message = Message.Test_message(id=common.getguid(), message=res, created=common.getnowtime())
    #     dbseesion.add(message)
    # dbseesion.commit()
    # dbseesion.close()


def getblog(url,css):
    r = session.get(url)
    # 通过CSS找到标签
    news = r.html.find(css)
    for new in news:
        print(new.text)  # 获得标题
        print(new.absolute_links)  # 获得链接



def getpage(url):
    r = session.get(url)

    images = r.html.find('ul.clearfix > li > a')  # 获取到网页上所有a标签url

    def save_Image(url, title):  # 定义一个函数，用于保存图片到指定目录下
        html_response = requests.get(url)
        with open('E:/bg/' + title + '.jpg', 'wb') as file:
            file.write(html_response.content)

    # 查找页面中背景图，找到链接，访问查看大图，并获取大图地址
    for image in images:
        image_url = image.attrs['href']  # 获取到每张图片属性值为href的url
        if '/wallpaper_detail' in image_url:
            r = session.get(image_url)
            item_url = r.html.find('img.pic-large', first=True)  # 获取到href下的src的url
            url = item_url.attrs['src']
            title = item_url.attrs['title']
            print(url + title)
            save_Image(url, title)



#
# k2=getwww('http://www.win4000.com/')
# for ser in k2:
#     try:
#         getpage(ser)
#
#     except Exception as e:
#         print(e)







