# scrapy-
用于毕业论文

scrapy教程
=========
时间 2019-1-13

### 创建了一个教程项目 

使用以下命令行创建scrapy项目
<pre><code>
scrapy startproject tutorial
</code></pre>
生成的文件夹结构
scrapy.cfg  #scrapy部署时的配置文件
tutorial    #项目的模块，需要从这里引入
__init__.py
items.py    #Items的定义，定义爬去的数据结构
middlewares.py   #Middlewares的定义，定义爬取时的中间件
pipelines.py     #pipelines的定义，定义数据管道
settings.py      #项目配置文件
spiders        #放置spiders的文件夹

### 创建spider
<pre><code>
cd tutorial
scrapy genspider example example.com
</code></pre>

自动生成的spider有三个属性
<li>name ,spider的名字</li>
<li>allowed_domains ,允许爬取的域名，如果初始或后续的请求链接不是在这个域名下的，则请求链接会被过滤掉</li>
<li>start_urls,它包含了spider在启动时爬取的url列表，初始请求是由它来定义的</li>
<li>parse,它是spider的方法。默认情况下，被调用时start_urls里面的链接构成的请求完成下载执行后，返回的响应就会作为唯一的参数传递给这个函数。该方法负责解析返回相应，提取数据或者进一步生成要处理的请求。




### 创建item
item是保存爬去数据的容器，与字典类似，但是相对与字典而言，item拥有额外的保护机制可以避免拼写错误或者定义字段错误
item需要继承scrapy.item类，并且定义scrapy.field的字段
修改items.py