## 简介

Scrapy是通过`scrapy`命令行工具进行控制的。详细的命令行工具说明[点击这里](https://docs.scrapy.org/en/latest/topics/commands.html)参考文档。

一般来说，使用 scrapy 工具的第一件事就是创建您的Scrapy项目：

```
scrapy startproject project_name [project_dir]
```

它将在 `project_dir` 目录。如果 `project_dir` 没有指定， `project_dir` 将与 `myproject` .



一个Scrapy项目的目录结构如下：

```
scrapy.cfg
project_name/
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...
```



其中，`scrapy.cfg`存放的目录被认为是项目的根目录。这时候就可以在项目中使用`scrapy`工具来对其进行控制和管理。比如，创建一个新的spider:

```
scrapy genspider mydomain mydomain.com
```



这个命令会在`spiders/`目录下创建一个`mydomain.py`文件，就可以修改编写爬虫了。

Scrapy提供了两种类型的命令。一种必须在**Scrapy项目中**运行(项目命令)，另外一种则不需要(全局命令)。

## 全局命令

全局命令就是不需要在项目中使用的命令。

#### startproject

在`project_name`文件夹下创建一个名为`project_name`的Scrapy项目。用法：

```
scrapy startproject <project_name> [project_dir]
```



如果没有指定`project_dir`，将与`project_name`使用相同名字。

#### settings

这个命令在项目中运行时会输出项目的设定值，否则输出Scrapy默认设定。用法：

```
scrapy settings [options]
```



#### runspider

可以在未创建项目的情况下，运行一个编写在Python文件中的spider。用法：

```
scrapy runspider <spider_file.py>
```



#### shell

是一个交互终端，可以在未启动spider的情况下尝试及调试爬取代码。以给定的URL(如果给出)或者空(没有给出URL)启动Scrapy shell。
这个终端可以用来测试XPath或CSS表达式，也可以作为正常Python终端。如果安装了IPython，Scrapy终端将使用IPython替代标准Python终端。

```
scrapy shell [url]
```



Scrapy终端根据下载的页面会自动创建一些方便使用的对象:

- `crawler` - 当前 Crawler 对象.
- `spider` - 处理URL的spider。 对当前URL没有处理的Spider时则为一个 Spider 对象。
- `request` - 最近获取到的页面的 Request 对象。 可以使用`replace()`修改该request。或者 使用`fetch`快捷方式来获取新的request。
- `response` - 包含最近获取到的页面的 Response 对象。
- `sel` - 根据最近获取到的response构建的 Selector 对象。
- `settings` - 当前的 Scrapy settings

更多关于shell的内容，可以参考[文档](https://docs.scrapy.org/en/latest/topics/shell.html#topics-shell)。

#### fetch

使用Scrapy下载器下载给定的URL，并将获取到的内容输出，用法：

```
scrapy fetch <url>
```



还可以加一些其他参数，`--nolog`不输出日志，`--headers`输出`headers`：

```
scrapy fetch --nolog --headers http://www.example.com/
```



#### view

在浏览器中打开给定的URL，并以Scrapy spider获取到的形式展现。相当于保存获取的源码到本地，有些时候因为页面使用Ajax+js渲染页面，spider获取到的页面和用户浏览器看到的并不相同，可以用来检查spider所获取到的页面。用法：

```
scrapy view <url>
```

#### genspider

该方法可以使用提前定义好的模板来生成spider，使用`scrapy genspider -l`可以查看可用模版，`scrapy genspider -d [template]`可以查看模版具体内容。使用：

```
scrapy genspider [-t template] <name> <domain>
```

举例：

```shell
$ scrapy genspider -l
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed

$ scrapy genspider example example.com
Created spider 'example' using template 'basic'

$ scrapy genspider -t crawl scrapyorg scrapy.org
Created spider 'scrapyorg' using template 'crawl'
```

#### bench

运行benchmark测试，用法：

```
scrapy bench
```



#### version

输出Scrapy版本。配合`-v`运行时，该命令同时输出Python, Twisted以及平台的信息。用法：

```
scrapy version [-v]

Scrapy       : 2.5.0
lxml         : 4.6.3.0
libxml2      : 2.9.10
cssselect    : 1.1.0
parsel       : 1.6.0
w3lib        : 1.22.0
Twisted      : 21.2.0
Python       : 3.9.4 (default, Apr  5 2021, 01:50:46) - [Clang 12.0.0 (clang-1200.0.32.29)]
pyOpenSSL    : 20.0.1 (OpenSSL 1.1.1k  25 Mar 2021)
cryptography : 3.4.7
Platform     : macOS-11.2.3-x86_64-i386-64bit
```



## 项目命令

项目命令就是必须依赖于项目，要在项目里运行的命令。

#### crawl

使用spider进行爬取。用法：

```
scrapy crawl spider_name
```



#### check

运行contract检查代码是否有错误，用法：

```
scrapy check
```



#### list

列出当前项目中所有可用的spider。用法：

```
scrapy list
```



#### edit

使用`EDITOR`中设定的编辑器编辑给定的spider，用法：

```
scrapy edit spider_name
```



用的不多，直接使用IDE比较好。

#### parse

获取给定的URL并使用相应的spider分析处理。如果提供`--callback`选项，则使用spider的该方法处理，否则使用`parse`。用法：

```
scrapy parse <url> [options]
```



支持的选项：

- `--spider=SPIDER`: 跳过自动检测spider并强制使用特定的spider
- `--a NAME=VALUE`: 设置spider的参数(可能被重复)
- `--callback` or `-c`: spider中用于解析返回(response)的回调函数
- `--pipelines`: 在pipeline中处理item
- `--rules` or `-r`: 使用 CrawlSpider 规则来发现用来解析返回(response)的回调函数
- `--noitems`: 不显示爬取到的item
- `--nolinks`: 不显示提取到的链接
- `--nocolour`: 避免使用pygments对输出着色
- `--depth` or `-d`: 指定跟进链接请求的层次数(默认: 1)
- `--verbose` or `-v`: 显示每个请求的详细信息

