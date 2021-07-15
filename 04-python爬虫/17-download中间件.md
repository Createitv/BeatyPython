### 概述

查看scrapy官网的框架图，可以看出中间件处于几大主要组件之间，类似于生产流水线上的加工过程，将原料按照不同需求与功能加工成成品

[![img](https://img2018.cnblogs.com/blog/1685507/201909/1685507-20190903145223263-460541142.png)](https://img2018.cnblogs.com/blog/1685507/201909/1685507-20190903145223263-460541142.png)

 

其中4，5处于下载器与引擎之间的就是下载中间件，而spider与引擎之间的就是spider中间件。目前scrapy主要的中间件就这两个

### 下载中间件

下载器中间件是介于Scrapy的request/response处理的钩子框架，是用于全局修改Scrapy request和response的一个轻量、底层的系统。

主要过程：

 当Downloader生成Response之后，Response会被发送给Spider，在发送给Spider之前，Response会首先经过Spider Middleware处理，当Spider处理生成Item和Request之后，Item Request还会经过Spider Middleware的处理。

主要作用:

- 在Scrapy将请求发送到网站之前修改,处理请求,如：更换代理ip，header等
- 在将响应传递给引擎之前处理收到的响应，如：响应失败重新请求，或将失败的做一定处理再返回给引擎
- 忽略一些响应或者请求

#### 默认下载中间件

scrapy内置了一些默认配置，这些是不允许被修改的，通常是_BASE结尾的设置，比如DOWNLOADER_MIDDLEWARES_BASE下载中间件的默认设置，如下



```python
{
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
}
```

scrapy就是按照上面数字从小到大依次执行的，比如执行完RobotsTxtMiddleware的process_request()方法后会继续执行下面HttpAuthMiddleware等process_request()，可以看作串联的形式依次过流水线

如果我们要添加自定义的下载中间件，需要在settings.py中激活DOWNLOADER_MIDDLEWARES。同时想取消默认的一些中间件，也可以设置为None。注意的是激活DOWNLOADER_MIDDLEWARES并不会覆盖DOWNLOADER_MIDDLEWARES_BASE，而是继续串联起来



```python
DOWNLOADER_MIDDLEWARES = {
    'myproject.middlewares.CustomDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}
```

各默认中间件的可以参考https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#built-in-downloader-middleware-reference

 

#### 自定义下载中间件

在创建项目后，再项目文件夹中有一middlewares.py文件，里面自动生成了两个中间件示例或者说模板。我们如果要自定义中间件的话，可以在给的示例上修改，或者新建类实现方法，或者继承已有的中间件重写方法

以下是下载中间件可以实现的方法，在自定义中间件时，可以根据需求实现

**1.process_request(self, request, spider)**

当每个request通过下载中间件时，该方法被调用。process_request() 必须返回其中之一: 返回 None 、返回一个 Response 对象、返回一个 Request 对象或raise IgnoreRequest 。**最常使用的是返回None**

- 如果其返回 None ，会将处理过后的request丢给中间件链中的下一个中间件的process_request()方法处理，直到丢到下载器，由下载器下载
- 如果其返回 Response 对象，Scrapy将不会调用任何其他的 process_request() 或 process_exception() 方法，也不会丢到下载器下载；直接将其返回的response丢到中间件链的process_response()处理。可以通过**scrapy.http.Response**构建Response 
- 如果其返回 Request 对象，Scrapy则停止调用process_request方法并重新调度返回的request。当新返回的request被执行后， 相应地中间件链将会根据下载的response被调用。
- 如果其raise一个 IgnoreRequest 异常，则安装的下载中间件的 process_exception() 方法会被调用。如果没有任何一个方法处理该异常， 则request的errback(Request.errback)方法会被调用。如果没有代码处理抛出的异常， 则该异常被忽略且不记录(不同于其他异常那样)。

参数:
　　request(Request 对象)–处理的request
　　spider(Spider 对象)–该request对应的spider

 

**2.process_response(self, request, response, spider)**

 

当下载的response返回时，process_response()被调用，且 必须返回以下之一: 返回一个 Response 对象、 返回一个 Request 对象或raise一个 IgnoreRequest 异常。

- 如果其返回一个 Response (可以与传入的response相同，也可以是全新的对象)， 该response会被在链中的其他中间件的 process_response() 方法处理。
- 如果其返回一个 Request 对象，则中间件链停止， 返回的request会被重新调度下载。处理类似于 process_request() 返回request所做的那样。
- 如果其抛出一个 IgnoreRequest 异常，则调用request的errback(Request.errback)。 如果没有代码处理抛出的异常，则该异常被忽略且不记录(不同于其他异常那样)。

参数:
　　request (Request 对象) – response所对应的request
　　response (Response 对象) – 被处理的response
　　spider (Spider 对象) – response所对应的spider

**3.process_exception(self, request, exception, spider)**

 

当下载处理器(download handler)或 process_request() (下载中间件)抛出异常(包括IgnoreRequest异常)时，Scrapy调用 process_exception() 。process_exception() 应该返回以下之一: 返回 None 、 一个 Response 对象、或者一个 Request 对象。

- 如果其返回 None ，Scrapy将会继续处理该异常，接着调用已安装的其他中间件的 process_exception() 方法，直到所有中间件都被调用完毕，则调用默认的异常处理。
- 如果其返回一个 Response 对象，则已安装的中间件链的 process_response() 方法被调用。Scrapy将不会调用任何其他中间件的 process_exception() 方法。
- 如果其返回一个 Request 对象， 则返回的request将会被重新调用下载。这将停止中间件的 process_exception() 方法执行，就如返回一个response的那样。

参数:
　　request (是 Request 对象) – 产生异常的request
　　exception (Exception 对象) – 抛出的异常
　　spider (Spider 对象) – request对应的spider

**4.from_crawler(cls, crawler)**

如果存在，则调用此类方法创建中间件实例Crawler。它必须返回一个新的中间件实例。Crawler对象提供对所有Scrapy核心组件的访问，如设置和信号; 它是中间件访问它们并将其功能挂钩到Scrapy的一种方式。

参数:

　　crawler（Crawlerobject）- 使用此中间件的爬网程序

#### 设置随机UA中间件

UA中间件源码

```python
"""Set User-Agent header per spider or use a default value from settings"""

from scrapy import signals


class UserAgentMiddleware:
    """This middleware allows spiders to override the user_agent"""

    def __init__(self, user_agent='Scrapy'):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings['USER_AGENT'])
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        self.user_agent = getattr(spider, 'user_agent', self.user_agent)

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers.setdefault(b'User-Agent', self.user_agent)

```

自定义UA中间件



```python
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
]

class UserAgent_Middleware():

    def process_request(self, request, spider):
        ua = random.choice(user_agent_list)
        request.headers['User-Agent'] = ua
```

或者使用faker大魔王



```python
from faker import Faker

class UserAgent_Middleware():

    def process_request(self, request, spider):
        f = Faker()
        ua = f.firefox()
        request.headers['User-Agent'] = ua
```

 

#### 设置代理中间件



```python
proxy_list=[
    "http://180.76.154.5:8888",
    "http://14.109.107.1:8998",
    "http://106.46.136.159:808",
    "http://175.155.24.107:808",
    "http://124.88.67.10:80",
    "http://124.88.67.14:80",
    "http://58.23.122.79:8118",
    "http://123.157.146.116:8123",
    "http://124.88.67.21:843",
    "http://106.46.136.226:808",
    "http://101.81.120.58:8118",
    "http://180.175.145.148:808"]
class proxy_Middleware(object):

    def process_request(self,request,spider):
        proxy = random.choice(proxy_list)
        request.meta['proxy'] = 'http://'+proxy
        
```

至于代理池，可以自己爬取，或者github上查找，或者编写一套可替换可检查可用性的代理池脚本存在文件或者数据库中

 

#### 集成selenium



```python
from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class SeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(2)
        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url,
                           body=body,
                           encoding='utf-8',
                           request=request)
```

当然不是每一个spider都要用selenium，那样会很慢，可以在spider里的custom_settings单独激活这个中间件，selenium的用法会在其他文章讲述

 

#### 重试中间件



```python
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message


class CustomRetryMiddleware(RetryMiddleware):
    

    def process_response(self, request, response, spider):
    
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            #如果返回了[500, 502, 503, 504, 522, 524, 408]这些code，换个proxy试试
            proxy = random.choice(proxy_list)
            request.meta['proxy'] = proxy
            return self._retry(request, reason, spider) or response
            
        return response
    
    #RetryMiddleware类里有个常量，记录了连接超时那些异常
    #EXCEPTIONS_TO_RETRY = (defer.TimeoutError, TimeoutError, DNSLookupError,
    #                       ConnectionRefusedError, ConnectionDone, ConnectError,
    #                       ConnectionLost, TCPTimedOutError, ResponseFailed,
    #                       IOError, TunnelError)
    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get('dont_retry', False):
            #这里可以写出现异常那些你的处理            
            proxy = random.choice(proxy_list)
            request.meta['proxy'] = proxy
            time.sleep(random.randint(3, 5))
            return self._retry(request, exception, spider)
    #_retry是RetryMiddleware中的一个私有方法，主要作用是
    #1.对request.meta中的retry_time进行+1 
    #2.将retry_times和max_retry_time进行比较，如果前者小于等于后者，利用copy方法在原来的request上复制一个新request，并更新其retry_times，并将dont_filter设为True来防止因url重复而被过滤。
    #3.记录重试reason
```

 