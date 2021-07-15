## scrapy.Spider基本爬虫类

Spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。 换句话说，Spider就是您定义爬取的动作及分析某个网页(或者是有些网页)的地方。

`class scrapy.Spider`是最基本的类，所有编写的爬虫必须继承这个类。

主要用到的函数及调用顺序为：

__init__() : 初始化爬虫名字和start_urls列表

start_requests() 调用make_requests_from url():生成Requests对象交给Scrapy下载并返回response

parse() : 解析response，并返回Item或Requests（需指定回调函数）。Item传给Item pipline持久化 ， 而Requests交由Scrapy下载，并由指定的回调函数处理（默认parse())，一直进行循环，直到处理完所有的数据为止。

```python
#所有爬虫的基类，用户定义的爬虫必须从这个类继承
class Spider(object_ref):
 
    #定义spider名字的字符串(string)。spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的。
    #name是spider最重要的属性，而且是必须的。
    #一般做法是以该网站(domain)(加或不加 后缀 )来命名spider。 例如，如果spider爬取 mywebsite.com ，该spider通常会被命名为 mywebsite
    name = None
 
    #初始化，提取爬虫名字，start_ruls
    def __init__(self, name=None, **kwargs):
        if name is not None:
            self.name = name
        # 如果爬虫没有名字，中断后续操作则报错
        elif not getattr(self, 'name', None):
            raise ValueError("%s must have a name" % type(self).__name__)
 
        # python 对象或类型通过内置成员__dict__来存储成员信息
        self.__dict__.update(kwargs)
 
        #URL列表。当没有指定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。 后续的URL将会从获取到的数据中提取。
        if not hasattr(self, 'start_urls'):
            self.start_urls = []
 
    # 打印Scrapy执行后的log信息
    def log(self, message, level=log.DEBUG, **kw):
        log.msg(message, spider=self, level=level, **kw)
 
    # 判断对象object的属性是否存在，不存在做断言处理
    def set_crawler(self, crawler):
        assert not hasattr(self, '_crawler'), "Spider already bounded to %s" % crawler
        self._crawler = crawler
 
    @property
    def crawler(self):
        assert hasattr(self, '_crawler'), "Spider not bounded to any crawler"
        return self._crawler
 
    @property
    def settings(self):
        return self.crawler.settings
 
    #该方法将读取start_urls内的地址，并为每一个地址生成一个Request对象，交给Scrapy下载并返回Response
    #该方法仅调用一次
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
 
    #start_requests()中调用，实际生成Request的函数。
    #Request对象默认的回调函数为parse()，提交的方式为get
    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True)
 
    #默认的Request对象回调函数，处理返回的response。
    #生成Item或者Request对象。用户必须实现这个类
    def parse(self, response):
        raise NotImplementedError
 
    @classmethod
    def handles_request(cls, request):
        return url_is_from_spider(request.url, cls)
 
    def __str__(self):
        return "<%s %r at 0x%0x>" % (type(self).__name__, self.name, id(self))
 
    __repr__ = __str__
```

## CrawlSpider爬虫

### 创建CrawlSpider爬虫

```shell
scrapy genspider -t crawl + 爬虫名 + 主域名
```

### CrawlSpider中的主要模块介绍

#### LinkExtractors链接提取器（找到满足规则的url进行爬取）

```python
class scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor(allow=(), deny=(), allow_domains=(), deny_domains=(), deny_extensions=None, restrict_xpaths=(), restrict_css=(), tags=('a', 'area'), attrs=('href', ), canonicalize=True, unique=True, process_value=None)
```

主要参数介绍：

allow:允许的url，所有满足这个正则表达式的url都会被提取

deny:禁止的url,所有满足这个正则表达式的url都不会被提取

allow_domains:允许的域名，在域名中的url才会被提取

deny_domains:禁止的域名，在域名中的url不会被提取

restrict_xpaths:使用xpath提取

restrict_css:使用css提取

#### Rule规则类

```python
 class scrapy.contrib.spiders.Rule(link_extractor,callback=None,cb_kwargs=None,follow=None,process_links=None,process_request=None)
```

主要参数介绍：

link_extractor:一个LinkExtractor对象，用来定义爬取规则

callback:回调函数

follow:从response中提取的url如满足条件是否进行跟进

process_links：从link_extractor中获取到的链接首先会传递给该函数，主要用来过滤掉无用的链接

## XMLFEEDSpider

`XMLFeedSpider`被设计用于通过迭代各个节点来分析XML源，迭代器可以从 iternodes， xml， html 选择。 鉴于 xml 以及 html 迭代器需要先读取所有`DOM`再分析而引起的性能问题， 一般还是推荐使用`iternodes` 。在使用错误标记解析XML时，使用html作为迭代器可能很有用。

文章目录

- [1 XMLFeedSpider 类](https://geek-docs.com/scrapy/scrapy-tutorials/scrapy-xmlfeedspider.html#XMLFeedSpider)
- [2 XMLFeedSpider 示例](https://geek-docs.com/scrapy/scrapy-tutorials/scrapy-xmlfeedspider.html#XMLFeedSpider-2)

## XMLFeedSpider 类

**class scrapy.contrib.spiders.XMLFeedSpider**

要设置迭代器和标签名，必须定义以下类属性:

**iterator**
定义要使用的迭代器的字符串, 默认值为 iternodes，可选项如下：

- `iternodes` – 基于正则表达式的快速迭代器
- `html` – 使用 Selector 的迭代器。特别提醒，它使用DOM解析，并且必须在内存中加载所有DOM，当数据量大的时候可能会产生问题。
- `xml` – 使用 Selector 的迭代器。特别提醒，它使用DOM解析，并且必须在内存中加载所有DOM，当数据量大的时候可能会产生问题。

------

**itertag**
具有要迭代的节点（或元素）名称的字符串，例如:

```python
itertag = 'product'
```

**namespaces**
一个由 (prefix, url) 元组(tuple)所组成的list。 其定义了在该文档中会被spider处理的可用的命名空间。 prefix 及 uri 会被自动调用 register_namespace()函数注册命名空间。

您可以通过在 `itertag` 属性中指定节点的 namespace。
例如:

```python
class YourSpider(XMLFeedSpider):

    namespaces = [('n', 'http://www.sitemaps.org/schemas/sitemap/0.9')]
    itertag = 'n:url'
    # ...
```



除了这些新的属性之外，该`spider`也有以下可以覆盖(overrideable)的方法:

**adapt_response(response)**
该方法在spider分析response前被调用。您可以在response被分析之前使用该函数来修改内容(body)。 该方法接受一个response并返回一个response(可以相同也可以不同)。

**parse_node(response, selector)**
当节点符合提供的标签名时(itertag)该方法被调用。 接收到的response以及相应的 Selector 作为参数传递给该方法。 该方法返回一个 Item 对象或者 Request 对象 或者一个包含二者的可迭代对象(iterable)。

**process_results(response, results)**
当spider返回结果(item或request)时该方法被调用。 设定该方法的目的是在结果返回给框架核心(framework core)之前做最后的处理， 例如设定item的ID。其接受一个结果的列表(list of results)及对应的response。 其结果必须返回一个结果的列表(list of results)(包含Item或者Request对象)。

该`spider`十分易用，下边是其中一个例子:

```python
from scrapy.spiders import XMLFeedSpider
from tutorial.items import TutorialItem

class MySpider(XMLFeedSpider):
    name = 'geek-docs'
    allowed_domains = ['sina.com.cn']
    # 设置要分析的 XML 文件地址
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    # 此时将开始迭代的节点设置为第一个节点 rss
    itertag = 'rss'  # change it accordingly

    def parse_node(self, response, selector):
        i = TutorialItem()
        i['title'] = selector.xpath("/rss/channel/item/title/text()").extract()
        i['link'] = selector.xpath("/rss/channel/item/link/text()").extract()
        i['author'] = selector.xpath("/rss/channel/item/author/text()").extract()
        # 通过 for 循环以遍历出提取出来的存在在 item 中的信息并输出
        for j in range(len(i['title'])):
            print("第 %s 篇文章" % str(j + 1))
            print("标题是：%s" % i['title'][j])
            print("对应链接是：%s" % i['link'][j])
            print("对应作者是：%s" % i['author'][j])
            print("-" * 20)
        return i
```

**输出结果：**
![Scrapy XMLFeedSpider](https://img.geek-docs.com/scrapy/201908042323.png)

## CSVFeedSpider

CSVFeedSpider与XMLFeedspider非常相似，区别是XMLFeedspider是根据节点来迭代数据的，而CSVFeedSpider是每行迭代。类似的，每行迭代调用的是parse_row()方法。常用的属性方法如下：
•  　delimiter：字段分隔符，默认是英文逗号','。
•  　quotechar：CSV字段中如果包含回车、引号、逗号，那么此字段必须用双引号引起来。此属性默认值为半角双引号。
•  　headers：CSV文件的标题头，该属性值是一个列表。
•  　parse_row(response,row)：对每一行数据进行处理，接收由一个Response、一个文件标题头组成的字典。
同XMLFeedSpider一样，在CSVFeedSpider中也可以复写adapt_response与process_result方法。

## SitemapSpider

SitemapSpider允许通过Sitemap发现URL链接来爬取一个网站。简单来讲，Sitemap包含网站所有网址以及每个网址的其他元数据，包括上次更新的时间、更改的频率以及相对于网站上其他网址的重要程度为何等

[参考](https://www.w3cschool.cn/scrapy2_3/scrapy2_3-18nc3fml.html)

