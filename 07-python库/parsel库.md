# Parsel

[![Tests](https://github.com/scrapy/parsel/actions/workflows/tests.yml/badge.svg)](https://github.com/scrapy/parsel/actions/workflows/tests.yml) [![Supported Python versions](https://img.shields.io/pypi/pyversions/parsel.svg)](https://github.com/scrapy/parsel/actions/workflows/tests.yml) [![PyPI Version](https://img.shields.io/pypi/v/parsel.svg)](https://pypi.python.org/pypi/parsel) [![Coverage report](https://img.shields.io/codecov/c/github/scrapy/parsel/master.svg)](https://codecov.io/github/scrapy/parsel?branch=master)

Parsel is a BSD-licensed [Python](https://www.python.org/) library to extract and remove data from [HTML](https://en.wikipedia.org/wiki/HTML) and [XML](https://en.wikipedia.org/wiki/XML) using [XPath](https://en.wikipedia.org/wiki/XPath) and [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) selectors, optionally combined with [regular expressions](https://docs.python.org/library/re.html).

#### demo

```python
>>> from parsel import Selector
>>> selector = Selector(text="""<html>
        <body>
            <h1>Hello, Parsel!</h1>
            <ul>
                <li><a href="http://example.com">Link 1</a></li>
                <li><a href="http://scrapy.org">Link 2</a></li>
            </ul>
        </body>
        </html>""")
>>> selector.css('h1::text').get()
'Hello, Parsel!'
>>> selector.xpath('//h1/text()').re(r'\w+')
['Hello', 'Parsel']
>>> for li in selector.css('ul > li'):
...     print(li.xpath('.//@href').get())
http://example.com
http://scrapy.org
```

#### 基本使用

```python
>>> from parsel import Selector
>>> text = "<html><body><h1>Hello, Parsel!</h1></body></html>"
>>> selector = Selector(text=text)
>>> selector.css('h1::text').get()
'Hello, Parsel!'
>>> selector.xpath('//h1/text()').getall()
['Hello, Parsel!']
```

#### 网页数据解析

```python
>>> import requests
>>> from parsel import Selector
>>> url = 'https://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
>>> text = requests.get(url).text
>>> selector = Selector(text=text)
>>> selector.xpath('//title/text()')
[<Selector xpath='//title/text()' data='Example website'>]
>>> selector.css('title::text')
[<Selector xpath='descendant-or-self::title/text()' data='Example website'>]
>>> selector.xpath('//title/text()').getall()
['Example website']
>>> selector.xpath('//title/text()').get()
'Example website'
>>> selector.css('title::text').get()
'Example website'
>>> selector.css('img').xpath('@src').getall()
['image1_thumb.jpg',
 'image2_thumb.jpg',
 'image3_thumb.jpg',
 'image4_thumb.jpg',
 'image5_thumb.jpg']
```

#### Extensions to CSS Selectors

Per W3C standards, [CSS selectors](https://www.w3.org/TR/css3-selectors/#selectors) do not support selecting text nodes or attribute values. But selecting these is so essential in a web scraping context that Parsel implements a couple of **non-standard pseudo-elements**:

- to select text nodes, use `::text`
- to select attribute values, use `::attr(name)` where *name* is the name of the attribute that you want the value of

```python
>>> selector.css('base').attrib
{'href': 'http://example.com/'}
>>> selector.css('base').attrib['href']
'http://example.com/'
```

#### Using selectors with regular expressions

[`Selector`](https://parsel.readthedocs.io/en/latest/parsel.html#parsel.selector.Selector) also has a `.re()` method for extracting data using regular expressions. However, unlike using `.xpath()` or `.css()` methods, `.re()` returns a list of unicode strings. So you can’t construct nested `.re()` calls.

```python
>>> selector.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
['My image 1 ',
 'My image 2 ',
 'My image 3 ',
 'My image 4 ',
 'My image 5 ']
```

There’s an additional helper reciprocating `.get()` (and its alias `.extract_first()`) for `.re()`, named `.re_first()`. Use it to extract just the first matching string:

```python
>>> selector.xpath('//a[contains(@href, "image")]/text()').re_first(r'Name:\s*(.*)')
'My image 1 '
```