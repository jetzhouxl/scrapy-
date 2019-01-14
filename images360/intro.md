项目简介
======

## 目的
这个项目是为了熟悉item pipeline而创建，主要是了解如何通过item pipeline来下载文件，并存储到mysql数据库中。

## 项目爬取网站
https://image.so.com

## 抓取分析
对网页请求做相应的分析

## 新建项目
<pre><code>
scrapy startproject images360
</code></pre>
接下来进入项目创建spider
<pre><code>
scrapy genspider images images.so.com
</code></pre>

## 构造请求
首先我们在setting.py中定义一个变量MAX_PAGE，然后重写start_requests()方法，用来完成50次请求。