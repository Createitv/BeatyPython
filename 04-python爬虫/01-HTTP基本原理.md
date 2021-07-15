## 1.URI和URL

URI 全称为 Uniform Resource Identifier，即统一资源标志符，URL 全称为 Universal Resource Locator，即统一资源定位符。

URL是URI的子集，URI 还包括一个子类叫做 URN，它的全称为 Universal Resource Name，即统一资源名称。URI可被视为定位符URL，名称URN或者两者兼备。URN定义某事物的身份，URL提供查找该事物的方法，URN仅用于命名，而不指定地址。

在互联网中，URN使用很少，几乎都是URI和URL，所以一般网页可以成为URL或URI。

## 2.超文本

超文本的英文是Hypertext，浏览器中的网页就是超文本解析而成的，网页源代码是一系列HTML代码，里面包含一系列标签，如img显示图片，p显示段落，浏览器解析这些标签后形成了我们平时看到的网页，而这些网页的源代码HTML就可称为超文本。

## 3.HTTP、HTTPS

HTTP的全称Hyper Text Transfer Protocol，中文名称叫超文本传输协议，HTTP协议是用于从网络传输超文本数据到本地浏览器的传输协议，它能保证传送高效而准确的传送超文本文档。

HTTPS的全称是Hyper Text Transfer Protocol over Secure Socket Layer，是以安全为目标的HTTP通道，就是HTTP安全版，即HTTP下加入SSL层，简称HTTPS。

HTTPS的安全基础是SSL，通过它传输的内容都是SSL加密的，主要作用有两种：

> 建立一个信息安全通道，保证数据传输的安全。
>
> 确认网站的真实性，凡是使用HTTPS的网站都可以通过点击浏览器地址栏的锁头标志来查看网站认证之后的真实信息，也可通过CA机构颁发的安全签章来查询。

一些网站虽然使用HTTPS协议但还是会被浏览器提示不安全，如在chrome中打开12306，链接为：[https://www.12306.cn/](https://link.jianshu.com?t=https%3A%2F%2Fwww.12306.cn%2F)，浏览器会提示“您的连接不是私密连接”，如下图

![img](https:////upload-images.jianshu.io/upload_images/11737062-2834bed616ee94d6.png)

原因是12306的CA证书是中国铁道部自己颁发给自己的，这个证书是不被官方机构认可的，所以证书验证不会通过，但它的数据传输依然是SSL加密的。爬虫如果要爬取这样的站点需要设置忽略证书的选项，否则会提示SSL链接错误。

## 4.HTTP请求过程

在浏览器输入一个url，回车后在浏览器中观察到页面内容，其中的过程是浏览器向网站所在服务器发送一个Request，即请求，网站服务器接收到Request后进行处理和解析，然后返回对应的Response，即响应，然后传回浏览器，Response中包含了页面的源代码等内容，浏览器在对其进行解析便将网页呈现出来。

用chrome浏览器的开发者模式下的Network监听组件做演示，访问百度：[http://www.baidu.com](https://link.jianshu.com?t=http%3A%2F%2Fwww.baidu.com) Network页面下的一个条目代表一次发送Request和接受Response的过程，如图：

![img](https:////upload-images.jianshu.io/upload_images/11737062-e1d1faf113996ca5.png)

网络请求记录

这一个条目的各列分别代表：

第一列 Name，即 Request 的名称。一般会用URL的最后一部分内容当做名称。

第二列 Status，即 Response 的状态码。这里显示为 200，代表 Response 是正常的，通过状态码我们可以判断发送了 Request 之后是否得到了正常的 Response。

第三列 Type，即 Request 请求的文档类型。这里为 document，代表我们这次请求的是一个 HTML 文档，内容就是一些 HTML 代码。

第四列 Initiator，即请求源。用来标记 Request 是由哪个对象或进程发起的。

第五列 Size，即从服务器下载的文件和请求的资源大小。如果是从缓存中取得的资源则该列会显示 from cache。

第六列 Time，即发起 Request 到获取到 Response 所用的总时间。

第七列 Waterfall，即网络请求的可视化瀑布流。

点击条目可以看到更详细的信息，如图：

![img](https:////upload-images.jianshu.io/upload_images/11737062-b61659b6be3b282e.png)

详细信息

 General 部分，Request URL 为 Request 的 URL，Request Method 为请求的方法，Status Code 为响应状态码，Remote Address 为远程服务器的地址和端口，Referrer Policy 为 Referrer 判别策略。

Response Headers 和一个 Request Headers，这分别代表响应头和请求头，请求头里面带有许多请求信息，例如浏览器标识、Cookies、Host 等信息，这是 Request 的一部分，服务器会根据请求头内的信息判断请求是否合法，进而作出对应的响应，返回 Response，那么在图中看到的 Response Headers 就是 Response 的一部分，例如其中包含了服务器的类型、文档类型、日期等信息，浏览器接受到 Response 后，会解析响应内容，进而呈现网页内容。

## 5.Request

Request，请求，由客户端向服务端发出。可以将Request划为四部分内容：Request Method、Request URL、Request Headers、Request Body，即请求方式、请求链接、请求头、请求体。

### Request Method

请求方式，常见两种GET和POST。

在浏览器中直接输入一个URL并回车，这便发起一个GET请求，请求参数会直接包含到URL里，如百度搜索Python，这就是一个GET请求，链接为：[https://www.baidu.com/s?wd=Python](https://link.jianshu.com?t=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3DPython)，URL中包含了请求的参数信息，这里的参数wd就是要搜寻的关键词。POST请求大多为表单提交发起，如登录表单，输入用户名和密码，点击登录，通常会发起一个POST请求，其数据通常以Form Data即表单形式传输，不会体现在URL中。

GET和POST请求方法的区别：

1.GET 方式请求中参数是包含在 URL 里面的，数据可以在 URL 中看到，而 POST 请求的 URL 不会包含这些数据，数据都是通过表单的形式传输，会包含在 Request Body 中。

2.GET 方式请求提交的数据最多只有 1024 字节，而 POST 方式没有限制。

![img](https:////upload-images.jianshu.io/upload_images/11737062-95c0236617ceb0b2.png)

请求方式总结

### Request URL

请求网址，用URL可以唯一确定我们想请求的资源。

### Request Headers

请求头，用来说明服务器要使用的附加信息，一些常用头：

Accept，请求报头域，用于指定客户端可接受那些类型的信息。

Accept-Language，指定客户端可接受语言类型。

Accept-Encoding，指定客户端可接受的内容编码。

Host，用于指定请求资源的主机IP和端口号，其内容为请求URL的原始服务器或网关的位置。

Cookie/Cookies，是网站为了辨别用户进行Session跟踪而存储在本地的数据。Cookies 的主要功能就是维持当前访问会话，例如我们输入用户名密码登录了某个网站，登录成功之后服务器会用 Session 保存我们的登录状态信息，后面我们每次刷新或请求该站点的其他页面时会发现都是保持着登录状态的，在这里就是 Cookies 的功劳，Cookies 里有信息标识了我们所对应的服务器的 Session 会话，每次浏览器在请求该站点的页面时都会在请求头中加上 Cookies 并将其发送给服务器，服务器通过 Cookies 识别出是我们自己，并且查出当前状态是登录的状态，所以返回的结果就是登录之后才能看到的网页内容。

Referer，此内容用来标识这个请求是从哪个页面发过来的，服务器可以拿到这一信息并做相应的处理，如做来源统计、做防盗链处理等。

User-Agent，简称 UA，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、浏览器及版本等信息。在做爬虫时加上此信息可以伪装为浏览器，如果不加很可能会被识别出为爬虫。

Content-Type，即 Internet Media Type，互联网媒体类型，也叫做 MIME 类型，在 HTTP 协议消息头中，使用它来表示具体请求中的媒体类型信息。例如 text/html 代表 HTML 格式，image/gif 代表 GIF 图片，application/json 代表 Json 类型，更多对应关系可以查看此对照表：[http://tool.oschina.net/commons](https://link.jianshu.com?t=http%3A%2F%2Ftool.oschina.net%2Fcommons)。

Request Headers 是 Request 等重要组成部分，在写爬虫的时候大部分情况都需要设定 Request Headers。

### Request Body

请求体，一般承载的内容是POST请求中的Form Data，即表单数据，而对于GET请求Request Body则为空。

在Request Headers中指定Content-Type

![img](https:////upload-images.jianshu.io/upload_images/11737062-3e6de9a77c6d8140.png)

Content-Type和POST提交数据方式的关系

在爬虫中如果要构造POST请求需注意这几种Content-Type，了解请求库的各个参数设置时使用的是哪种Content-Type，不然可能会导致POST提交后得不到正常的Response。

## 6.Response

Response，即响应，由服务端返回给客户端。Response 可以划分为三部分，Response Status Code、Response Headers、Response Body。

### Response Status Code

响应状态码，状态码表示了服务器响应状态，如200表示服务器正常响应，404代表页面未找到，500代表服务器内部发生错误。在爬虫中可以根据状态码来判断服务器响应状态，如判断为200，则证明成功返回数据，再进行进一步处理，否则直接忽略。

![img](https://s0.lgstatic.com/i/image3/M01/6B/36/Cgq2xl5XTQSAfWsUAAa-jFIsTTw064.png)

常见的错误代码及错误原因

```python
# request库源码
_codes = {

    # Informational.
    100: ('continue',),
    101: ('switching_protocols',),
    102: ('processing',),
    103: ('checkpoint',),
    122: ('uri_too_long', 'request_uri_too_long'),
    200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
    201: ('created',),
    202: ('accepted',),
    203: ('non_authoritative_info', 'non_authoritative_information'),
    204: ('no_content',),
    205: ('reset_content', 'reset'),
    206: ('partial_content', 'partial'),
    207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
    208: ('already_reported',),
    226: ('im_used',),

    # Redirection.
    300: ('multiple_choices',),
    301: ('moved_permanently', 'moved', '\\o-'),
    302: ('found',),
    303: ('see_other', 'other'),
    304: ('not_modified',),
    305: ('use_proxy',),
    306: ('switch_proxy',),
    307: ('temporary_redirect', 'temporary_moved', 'temporary'),
    308: ('permanent_redirect',
          'resume_incomplete', 'resume',),  # These 2 to be removed in 3.0

    # Client Error.
    400: ('bad_request', 'bad'),
    401: ('unauthorized',),
    402: ('payment_required', 'payment'),
    403: ('forbidden',),
    404: ('not_found', '-o-'),
    405: ('method_not_allowed', 'not_allowed'),
    406: ('not_acceptable',),
    407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
    408: ('request_timeout', 'timeout'),
    409: ('conflict',),
    410: ('gone',),
    411: ('length_required',),
    412: ('precondition_failed', 'precondition'),
    413: ('request_entity_too_large',),
    414: ('request_uri_too_large',),
    415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
    416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
    417: ('expectation_failed',),
    418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
    421: ('misdirected_request',),
    422: ('unprocessable_entity', 'unprocessable'),
    423: ('locked',),
    424: ('failed_dependency', 'dependency'),
    425: ('unordered_collection', 'unordered'),
    426: ('upgrade_required', 'upgrade'),
    428: ('precondition_required', 'precondition'),
    429: ('too_many_requests', 'too_many'),
    431: ('header_fields_too_large', 'fields_too_large'),
    444: ('no_response', 'none'),
    449: ('retry_with', 'retry'),
    450: ('blocked_by_windows_parental_controls', 'parental_controls'),
    451: ('unavailable_for_legal_reasons', 'legal_reasons'),
    499: ('client_closed_request',),

    # Server Error.
    500: ('internal_server_error', 'server_error', '/o\\', '✗'),
    501: ('not_implemented',),
    502: ('bad_gateway',),
    503: ('service_unavailable', 'unavailable'),
    504: ('gateway_timeout',),
    505: ('http_version_not_supported', 'http_version'),
    506: ('variant_also_negotiates',),
    507: ('insufficient_storage',),
    509: ('bandwidth_limit_exceeded', 'bandwidth'),
    510: ('not_extended',),
    511: ('network_authentication_required', 'network_auth', 'network_authentication'),
}
```



### Response Headers

响应头，包含服务器对请求的应答信息，如Context-Type、Server、Set-Cookie等，一些常见的头信息：

Date，标识Response产生的时间

Last-Modified，指定资源的最后修改时间

Content-Encoding，指定Response内容的编码

Serve，包含了服务器的信息，名称，版本号等

Context-Type，文档类型，指定了返回的数据类型是什么。

Set-Cookie，设置Cookie，告诉浏览器要将此内容放在Cookies中，下次请求携带Cookies请求

Expires，指定Response的过期时间，使用它可以控制代理服务器或浏览器将内容更新到缓存中，如果再次访问时，直接从缓存中加载，降低服务器负载，缩短加载时间

### Response Body

响应体，最重要的当属响应体内容，响应的正文数据都是在响应体中，如请求一个网页，它的响应体是网页的HTML代码，请求一张图片，响应体就是图片的二进制数据。在做爬虫时主要解析的内容就是 Resposne Body，通过 Resposne Body 我们可以得到网页的源代码、Json 数据等等，然后从中做相应内容的提取。



