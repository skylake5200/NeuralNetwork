ImportError: No module named bs4错误解决方法
前言：毕业论文打算用Python做爬虫爬一些数据，最近开始入门Python；

在学习的时候遇到一个问题，按照看的文章安装了Python，也配置了相应的环境（使用window系统），使用pycharm编辑器来写Python（此软件运行Python很方便，安装Python需要用的库也很简单）。

在安装requests和BeautifulSoup两个库之后开始爬一个本地html，开头引用了from bs4 import BeautifulSoup但是最后一直报ImportError: No module named bs4错；

查了一些资料之后，顺利解决了此问题；

解决方法：

运行时提示ImportError: No module named bs4错误，意思是未找到名为Beautifulsoup4的模块。

写一下Python如何安装模块：

1.下载BS4模块：

http://www.crummy.com/software/BeautifulSoup/bs4/download/4.3/beautifulsoup4-4.3.2.tar.gz

2.解压到Python安装目录下的根目录中：

3.运行cmd，进入解压缩后的目录（如果Python默认安装在C盘下，打开cmd之后可以使用cd ...语句先返回根目录，再进入Python27\beautifulsoup4-4.3.2）

4.进入Python27\beautifulsoup4-4.3.2之后安装BS4模块：

5、输入：python setup.py install


安装好之后就可以用了