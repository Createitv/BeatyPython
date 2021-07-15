

 

## spider中间件

spider中间件用于处理引擎传回的response及spider生成的item和Request

主要作用：

- 处理spider的异常
- 对item在进入管道之前操作
- 根据引擎传入的响应，再进入回调函数前先处理

#### 默认spider中间件

SPIDER_MIDDLEWARES_BASE



```python
{
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
}
```

同理，激活中间件



```python
SPIDER_MIDDLEWARES = {
    'myproject.middlewares.CustomSpiderMiddleware': 543,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': None,
}
```

s 

#### 自定义spider中间件

**1.process_spider_input(self, response, spider)**

对于通过spider中间件并进入spider的每个响应，都会调用此方法进行处理。

process_spider_input()应该返回None或提出异常。

- 如果它返回None，Scrapy将继续处理此响应，执行所有其他中间件，直到最后，响应被交给spider进行处理。
- 如果它引发异常，Scrapy将不会调用任何其他spider中间件的process_spider_input()，将调用请求errback(如果有的话)，否则它将进入process_spider_exception()链

参数：
　　response（Responseobject） - 正在处理的响应
　　spider（Spiderobject） - 此响应所针对的spider

 

**2.process_spider_output(self, response, result, spider)**

在处理完响应之后，使用Spider返回的结果调用此方法。

process_spider_output()必须返回一个可迭代的 Request，dict或Item 对象。

参数：
　　response（Responseobject） - 从spider生成此输出的响应
　　result（可迭代的Request，dict或Item对象） - spider返回的结果
　　spider（Spiderobject） - 正在处理其结果的spider

 

**3.process_spider_exception(self, response, exception, spider)**

当spider或process_spider_output() 方法（来自先前的spider中间件）引发异常时，将调用此方法。

process_spider_exception()应该返回一个None或一个可迭代的Request，dict或 Item对象。

- 如果它返回None，Scrapy将继续处理此异常，执行process_spider_exception()以下中间件组件中的任何其他组件，直到没有剩余中间件组件并且异常到达引擎（它被记录并丢弃）。
- 如果它返回一个iterable，那么process_spider_output()管道将从下一个spider中间件开始启动，并且不会process_spider_exception()调用其他任何一个 。

参数：
　　response（Responseobject） - 引发异常时正在处理的响应
　　exception（异常对象） - 引发异常
　　spider（Spiderobject） - 引发异常的spider

 

**4.process_start_requests(self, start_requests, spider)**

当spider运行到start_requests()的时候，爬虫中间件的process_start_requests()方法被调用

它接收一个iterable（在start_requests参数中）并且必须返回另一个可迭代的Request对象。

参数：
start_requests（可迭代Request） - 开始请求
spider（Spiderobject） - 启动请求所属的spider

 

**5.from_crawler(cls, crawler)**

这个类方法通常是访问settings和signals的入口函数

 

#### spider中间件总结

1.spider开始start_requests()的时候，spider中间件的process_start_requests()方法被调用

2.下载response成功后，返回到spider 回调函数parse前，调用process_spider_input()

3.当spider yield scrapy.Request()或者yield item的时候，spider中间件的process_spider_output()方法被调用。

4.当spider出现了Exception的时候，spider中间件的process_spider_exception()方法被调用。

 

### 中间件与spider的关系流程图

 

[![img](https://img2018.cnblogs.com/blog/1685507/201909/1685507-20190903175131996-230085075.png)](https://img2018.cnblogs.com/blog/1685507/201909/1685507-20190903175131996-230085075.png)

 

