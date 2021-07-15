## `Requests`的认识

- 1、定义:在前面的章节中我们介绍了使用`Requests`建立连续性爬虫(我们爬取一页数据需要重新发送一个请求的时候触发的),这个类需要传递一些参数,

- 2、导包方式

  ```python
  from scrapy.http import Request
  ```

   Request其实在`scrapy.http.request`里

- 3、使用方式

  ```py
  yield Request(url='', callback=''...)
  ```

- 4、关于`Request`的主要参数介绍

  ```py
  class Request(object_ref):
  
      def __init__(self, url, callback=None, method='GET', headers=None, body=None,
                   cookies=None, meta=None, encoding='utf-8', priority=0,
                   dont_filter=False, errback=None, flags=None):
  ```

  - `url`: 字符串类型`url`地址
  - `callback`:回调函数名称
  - `method`:字符串类型请求方式,如果`GET,POST`
  - `headers`:字典类型的,浏览器用户代理
  - `cookies`:设置`cookies`
  - `meta`:字典类型键值对,向回调函数直接传一个指定值
  - `encoding`:设置网页编码
  - `priority`:默认为0,如果设置的越高,越优先调度
  - `dont_filter`:默认为`False`,如果设置为真,会过滤掉当前`url`
  - `errback`: 在发生错误的时候执行的函数

### 二、关于`Response`的认识

定义:`Response`对象一般是由`Scrapy`给你自定构建的.因此开发者不需要关心如何创建`Response`对象,而是直接知道他有哪些属性就可以。主要包括下面这些常用属性:

- `meta`:从上一个请求传递过来的,常用于多个请求之间数据交互
- `encoding`: 返回当前字符串编码和解码的格式
- `text`: 将返回的数据作为`unicode`字符串返回
- `body`:将返回的数据作为`bytes`字符串返回
- `xpath`:使用`xpath`选择器
- `css`: 使用`css`选择器