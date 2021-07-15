## 	pipelines.py

```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

MONGO_URI = 'localhost'
MONGO_DB = 'dbname'

MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'dbname'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import pymysql
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get("MONGO_URI"),
                   mongo_db=crawler.settings.get("MONGO_DB"))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


import pymysql


class MysqlPipleline(object):

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.port = port
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get('MYSQL_HOST'),
                   database=crawler.settings.get("MYSQL_DATABASE"),
                   user=crawler.settings.get("MYSQL_USER"),
                   password=crawler.settings.get("MYSQL_PASSWORD"),
                   port=crawler.settings.get("MYSQL_PORT"),)

    def open_spider(self, spider):
        self.db = pymysql.connect(
            host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(["%s"] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item


class ImagePipleline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
    
    def item_complete(self, results, item, info):
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem("Image Download Failed")
        return item
    
    def get_media_requests(self, item, info):
        yield Request(item['url'])

```

