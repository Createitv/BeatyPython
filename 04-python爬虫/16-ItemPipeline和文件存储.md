## Item Pipeline

Item Pipeline调用发生在Spider产生Item之后。当Spider解析完Response之后，Item就会传递到Item Pipeline，被定义的Item Pipeline组件会顺次调用，完成一连串的处理过程，比如数据清洗、存储等。

Item Pipeline的主要用途是:

- 清理HTML数据。
- 验证爬取数据，检查爬取字段。
- 查重并丢弃重复内容。
- 将爬取结果保存到数据库。

## Pipeline类

可以自定义管道类，但每个管道类必须实现以下方法:

**process_item(self, item, spider)**

process_item()是必须要实现的方法，被定义的Item Pipeline会默认调用这个方法对Item进行处理。比如，我们可以进行数据处理或者将数据写入到数据库等操作。它**必须**返回Item类型的值或者抛出一个DropItem异常。

参数:

- **`item`**，是Item对象，即被处理的Item。
- **`spider`**，是Spider对象，即生成该Item的Spider。

 

除了process_item()必须实现，管道类还有其它的方法实现:

1.**open_spider(spider)**

在Spider开启时被调用，主要做一些初始化操作，如连接数据库等。参数是即被开启的Spider对象

2.**close_spider(spider)**

在Spider关闭时被调用，主要做一些如关闭数据库连接等收尾性质的工作。参数spider就是被关闭的Spider对象

3.**from_crawler(cls,crawler)**

类方法，用@classmethod标识，是一种依赖注入的方式。它的参数是crawler，通过crawler对象，我们可以拿到Scrapy的所有核心组件，如全局配置的每个信息，然后创建一个Pipeline实例。参数cls就是Class，最后返回一个Class实例。

 

**激活Item Pipeline组件**

要激活Item Pipeline组件，必须将其类添加到 ITEM_PIPELINES设置中，如下例所示



```python
ITEM_PIPELINES = {
    'myproject.pipelines.Pipelineclass1': 300,
    'myproject.pipelines.Pipelineclass2': 800,
}
```

设置中为类分配的整数值决定了它们运行的顺序：项目从较低值到较高值类别。习惯上在0-1000范围内定义这些数字。

 

## Scrapy文件图片保存

settings.py中ITEM_PIPELINES中数字代表执行顺序（范围是1-1000），参数需要提前配置在settings.py中（也可以直接放在函数中，这里主要是放在settings.py中），同时settings.py需要配置开启

```python
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
 
    # 启用scrapy自带的图片下载ImagesPipeline（None：为关闭）  
  	# 默认
    'scrapy.pipelines.images.ImagesPipeline': None,
  	# 自定义
    'qishutest.pipelines.CustomImagesPipeline':1,
    # 启用scrapy自带的文件下载FilesPipeline
    # 'scrapy.pipelines.files.FilesPipeline': 2
  
  	# 自定义
    'qishutest.pipelines.CustomFilesPipeline':2,
}

# 配置图片的保存目录
IMAGES_STORE = 'pics'
# 在ImagesPipeline进行下载图片，配置图片对应的Item字段
IMAGES_URLS_FIELD = 'pic_src'
 
FILES_STORE = 'novel'
 
FILES_URLS_FIELD = 'download_url'


```

图片保存中间件代码

```python
#图片++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipeline import ImagesPipeline
from scrapy import Request
class CustomImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 从items中获取要下载图片的url, 根据url构造Requeset()对象, 并返回该对象
        # sort_title = item['sort_title']
        try:
            image_url = item['pic_src'][0]
            yield Request(image_url, meta={'item': item})
        except:
            image_url = 'https://www.qisuu.la/modules/article/images/nocover.jpg'
        yield Request(image_url, meta={'item': item})
 
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        return '{}/{}.jpg'.format(item['sort'], item['novel_name'])
 
    def item_completed(self, results, item, info):
 
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item
 
#文本++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class CustomFilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
 
            download_url = item['download_url'][0]
            download_url = download_url.replace("'",'')
            print(download_url)
            yield Request(download_url, meta={'item':item})
 
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
       #创建sort_name文件，在里面保存novel_name文件
        return '%s/%s' % (item['sort'],item['novel_name'])
 
    def item_completed(self, results, item, info):
        print(results)
        return item

```

## 	`JSON`格式保存

- 1、直接在运行命令的时候生成文件

  ```py
  scrapy crawl 爬虫名字 -o 文件名
  ```

- 2、使用`json`直接写入

  ```python
  import json
  
  class JsonPipeline(object):
      def __init__(self):
          self.file = open('blog.json', 'a', encoding='utf8')
  
      def process_item(self, item, spider):
          if spider.name == 'blog':
              self.file.write(json.dumps(dict(item), indent=2, ensure_ascii=False) + ',\n')
          return item
  
      def close_spider(self, spider):
          self.file.close()
  ```

- 3、 使用自带的`<u>JsonItemExporter</u>`方法写入到本地文件中

  ```python
  from scrapy.exporters import JsonItemExporter
  
  class JsonPipeline(object):
      def __init__(self):
          self.file = open('blog.json', 'wb')
          self.exporter = JsonItemExporter(self.file, ensure_ascii=False, encoding='utf8')
          self.exporter.start_exporting()
  
      def process_item(self, item, spider):
          if spider.name == 'blog':
              self.exporter.export_item(item)
          return item
  
      def close_spider(self, spider):
          self.exporter.finish_exporting()
          self.file.close()
  ```

- 4、 使用自带的`<u>JsonLinesItemExporter</u>`方法写入到本地文件中

  ```python
  from scrapy.exporters import JsonItemExporter
  class JsonPipeline1(object):
      def __init__(self):
          self.fp = open('blog1.json', 'wb')
          self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf8')
  
      def process_item(self, item, spider):
          self.exporter.export_item(item)
          return item
  
      def close_spider(self, spider):
          self.fp.close()
  ```

## 写入mysql数据库

- 1、需要根据`item`的字段来创建表

- 2、在`settings.py`中设置`mysql`数据库连接信息

  ```py
  MYSQL_HOST = 'localhost'
  MYSQL_DBNAME = 'py_test'  # 数据库名字，请修改
  MYSQL_USER = 'root'  # 数据库账号，请修改
  MYSQL_PASSWD = 'root'  # 数据库密码，请修改
  MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用（
  ```

- 3、在`pipelines`中写一个类

  ```python
  import pymysql
  
  class XiciPipeline(object):
      def __init__(self, dbparams):
          self.connect = pymysql.connect(
              host=dbparams['host'],
              port=dbparams['port'],
              db=dbparams['db'],
              user=dbparams['user'],
              passwd=dbparams['passwd'],
              charset=dbparams['charset'],
              use_unicode=dbparams['use_unicode']
          )
          # 创建一个句柄
          self.cursor = self.connect.cursor()
  
      @classmethod
      def from_crawler(cls, crawler):
          # 读取settings中的配置
          dbparams = dict(
              host=crawler.settings.get('MYSQL_HOST'),
              db=crawler.settings.get('MYSQL_DBNAME'),
              user=crawler.settings.get('MYSQL_USER'),
              passwd=crawler.settings.get('MYSQL_PASSWD'),
              port=crawler.settings.get('MYSQL_PORT'),
              charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
              use_unicode=False,
          )
          return cls(dbparams)
  
      def process_item(self, item, spider):
          if spider.name == 'xici':
              # sql语句:插入数据
              sql = 'insert into xici(ip, port, speed, proxy_type, localhost) values (%s, %s, %s, %s,%s)'
              self.cursor.execute(sql, (item['ip'], item['port'], item['speed'], item['proxy_type'], item['localhost']))
              self.connect.commit()
          return item
  
      def close_spider(self, spider):
          self.connect.close()
  ```

## 写入mongodb数据库

- 1、在`settings.py`中设置`mongodb`数据库连接

  ```python
  # 配置mongodb数据库
  MONGO_URI = 'localhost'
  MONGO_DATABASE = 'py_test'
  ```

- 2、书写`pipelines`

  ```python
  import pymongo
  
  class MongoPipeline(object):
      # 定义表名
      collection_name = '随意取'
  
      def __init__(self, mongo_url, mongo_db):
          self.mongo_url = mongo_url
          self.mongo_db = mongo_db
          self.client = None
          self.db = None
  
      @classmethod
      def from_crawler(cls, crawler):
          return cls(
              mongo_url=crawler.settings.get('MONGO_URI'),
              mongo_db=crawler.settings.get('MONGO_DATABASE', 'item')
          )
  
      def open_spider(self, spider):
          """
          打开爬虫的时候
          :param spider:
          :return:
          """
          self.client = pymongo.MongoClient(self.mongo_url)
          self.db = self.client[self.mongo_db]
  
      def close_spider(self, spider):
          """
          爬虫关闭的时候
          :param spider:
          :return:
          """
          self.client.close()
  
      def process_item(self, item, spider):
          """
          主要处理数据
          :param item:
          :param spider:
          :return:
          """
          if spider.name == 'blog':
              self.db[self.collection_name].insert(dict(item))
              return item
  ```

- 3、在`settings.py`中注册自己写的`pipelines`类

  ```python
  ITEM_PIPELINES = {
      'jobbloe.pipelines.MongoPipeline': 300,
  }
  ```

