# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup # 网页解析
import urllib                             # 资源下载
import urllib2                          # 网页读取
import re                                 # 正则匹配所需要
import os                                # 系统库
import time                             # 时间库
i = 0                         # 表示下载的时第几张图片
def getHtml(url):
                                                          # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0)Gecko/20100101 Firefox/23.0'} #伪造HTTP报头
                                                          # 针对很多网站，为了防止爬虫，会拒绝爬虫请求，这时候就需要我们去伪造http中的Header项了
                                                          # Header不会写的可以上网上找一个，一般是可以用的
    send_headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Connection':'keep-alive'
    }
    urls = urllib2.Request(url,headers=send_headers)
    html = urllib2.urlopen(urls)                          # urllib.urlopen实际上返回一个类似文件的对象
    if html.getcode() == 200:
        print ("已捕获"),url,"目标站数据..."
        return html
    else:
        print ("访问出现错误...错误代码："),html.getcode()
        return None

def callBackFunc(block_Num,block_Size,total_Size):
    """
    回调函数
    @block_Num: 已经下载的数据块
    @block_Size: 数据块的大小
    @total_Size: 远程文件的大小
    """
    download_Percent = 100.0 * block_Num * block_Size / total_Size
    if download_Percent > 100:
        download_Percent = 100
    print ("正在下载第"),i,("张图片,已下载                    %"),download_Percent
    
if __name__ == '__main__':                                # 主函数
  
                                                          # 先将所有的目录创建，与此同时保存她们的URL指向
                                                          # 入口URL：https://www.mmonly.cc/gqbz/fjbz/ #唯一图库之风景壁纸
                                                          # 目录URL格式：（https://www.mmonly.cc/gqbz/fjbz/129331.html）
                                                          # https://www.mmonly.cc/gqbz/fjbz/129268.html
    
  """<a target="_blank" href="https://www.mmonly.cc/gqbz/fjbz/129331.html">
    <img width="234" alt="风景桌面壁纸高清电脑图片" src="https://t1.mmonly.cc/uploads/tu/201612/23/25.png"
    original="https://t1.mmonly.cc/uploads/tu/201612/23/25.png">
  </a>
  """
  gate_URL = "https://www.mmonly.cc/gqbz/fjbz/"           # 入口URL
  html =  getHtml(gate_URL)                               # 获得目标网页
  html_Doc = html.read()
  
  if html != None:
      """https://www.zhihu.com/question/19696249
                                                ----知乎 如何解决用 Beautiful Soup 抓取网页却得到乱码的问题？
      """
      soupHtml = BeautifulSoup(html_Doc,"lxml",from_encoding = "gb18030") #解析html，返回html的解析对象,编码问题，卧槽！！！
                                                          # <div class="item_list infinite_scroll masonry" id="infinite_scroll">
                                                          # <img width="234" alt="电脑桌面壁纸高清风景图片" src="https://t1.mmonly.cc/uploads/tu/201612/47/47.png"
                                                          # original="https://t1.mmonly.cc/uploads/tu/201612/47/47.png">
      divs = soupHtml.findAll('div', class_="ABox")
      flag = 1
      for div in divs:
          #找到所有的div标签后
          div_Doc = str(div)
          soupDiv = BeautifulSoup(div_Doc,"lxml",from_encoding = "gb18030")
          if soupDiv.find('img') != None:                 # 从中筛选出我们需要的数据信息
              tag_img = soupDiv.find('img')
              #filename = tag_img['alt']                  # 指定文件夹名称,乱码问题，真心难倒我啦，，，，换个名字吧
              filename = "Background"+str(time.time())
              tag_a = soupDiv.find('a')
              img_direction_url = tag_a['href']
              os.mkdir(filename)                          # 创建目录
              print ("已创建目录")
              print (filename)
              print ("开始下载资源...")
              img_Html = getHtml(img_direction_url)       # 进入图片目录下
              img_Doc = img_Html.read()
              #<li id="nl"><a href="130130_3.html">下一页</a></li>
              while True:            
                 i = i + 1
                 soup_Img_Doc = BeautifulSoup(img_Doc,"lxml",from_encoding = "gb18030")
                 #<li class="pic-down h-pic-down"><a target="_blank" class="down-btn"
                 #href="https://t1.mmonly.cc/uploads/tu/201612/47/1-160320194503.jpg">查看原图</a></li>
                 download_btn = soup_Img_Doc.find('a',class_="down-btn")
                 img_url = download_btn['href']
                 print ("需要下载的图片URL"),img_url
                 _path_ = os.path.abspath(filename)       # 指定创建的文件夹路径
                 path = os.path.join(_path_,img_url[-6:]) # 图片的完整路径
                 urllib.urlretrieve(img_url,path,callBackFunc)
                 if i == 3:                               # 如过下载完毕，就返回
                     break
                 else:
                     #https://www.mmonly.cc/gqbz/fjbz/130130.html
                     img_Tag_a = soup_Img_Doc.find('a',href=re.compile(r"\d_?.html"))
                     #print "img_Tag_a的内容：",img_Tag_a
                     #print "img_Tag_a的href属性值为： ",img_Tag_a['href']
                     img_direction_url = "https://www.mmonly.cc/gqbz/fjbz/"+img_Tag_a['href']
                     img_Html = getHtml(img_direction_url)
                     img_Doc = img_Html.read()
                 
          i = 0
            
  else:
      print ("获取失败...")





    
    
       
    
    
  
  
  

