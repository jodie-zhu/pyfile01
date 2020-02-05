from bs4 import BeautifulSoup
import requests
import os

if os.path.exists("./三国演义2") == False :
    os.mkdir("./三国演义2")


headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'
         }
#先获取全页的数据
url_all = 'http://www.shicimingju.com/book/sanguoyanyi.html'
page = requests.get(url=url_all,headers=headers)
print(page.status_code)
with open(file='./bs4.html', mode='w',encoding='utf-8') as fp:
    fp.write(page.text)

#解析出首页的标题及详情页Url
soup = BeautifulSoup(page.text,"html.parser") #定义BeautifulSoup对象差实例化
catalogue = soup.select('.book-mulu >ul>li>a') #查找标签

for i in catalogue:
    title = i.text   #获取每一回的标题
    url_detail="http://www.shicimingju.com"+i["href"]  #获取每一回对应的url
    print(url_detail)
    page_detail = requests.get(url=url_detail,headers=headers)
    soup2=BeautifulSoup(page_detail.text,"html.parser")
    detail_text=soup2.find('div',class_="chapter_content").text

    with open(file="./三国演义2/"+title+".txt", mode='w', encoding='utf-8') as fp:
        fp.write(detail_text)


