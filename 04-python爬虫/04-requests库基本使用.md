### 基本请求方法

获取它的网页源代码了。

我们可以用 requests 这个库轻松地完成这个过程，代码的写法是这样的：

```python
import requests

r = requests.get('<https://static1.scrape.center/>')
print(r.text)
```

### 参数传递

```python
import requests

data = {
    'name': 'germey',
    'age': 25
}
r = requests.get('<http://httpbin.org/get>', params=data)
print(r.text)
```

### JSON数据返回处理

```python
import requests

r = requests.get('<http://httpbin.org/get>')
print(type(r.text))
print(r.json())
print(type(r.json()))

------------output---------------
<class'str'>
{'headers': {'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.10.0'}, 'url': '<http://httpbin.org/get>', 'args': {}, 'origin': '182.33.248.131'}
<class 'dict'>
```

### 二进制数据返回处理

```python
import requests

r = requests.get('<https://github.com/favicon.ico>')
print(r.text)
print(r.content)
```

### 网页处理

```python
import requests
import re

r = requests.get('<https://static1.scrape.center/>')
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

------------output---------------
['肖申克的救赎 - The Shawshank Redemption', '霸王别姬 - Farewell My Concubine', '泰坦尼克号 - Titanic', '罗马假日 - Roman Holiday', '这个杀手不太冷 - Léon', '魂断蓝桥 - Waterloo Bridge', '唐伯虎点秋香 - Flirting Scholar', '喜剧之王 - The King of Comedy', '楚门的世界 - The Truman Show', '活着 - To Live']
```

### 添加请求头

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('<https://static1.scrape.center/>', headers=headers)
print(r.text)
```

### 获取响应数据

```python
import requests

r = requests.get('<https://static1.scrape.center/>')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
```

### 文件上传

```python
import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('<http://httpbin.org/post>', files=files)
print(r.text)
```

### Cookies设置

```python
import requests
# 获取cookies
r = requests.get('<http://www.baidu.com>')
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

import requests
# 上传cookies
headers = {
    'Cookie': '_octo=GH1.1.1849343058.1576602081; _ga=GA1.2.90460451.1576602111; __Host-user_session_same_site=nbDv62kHNjp4N5KyQNYZ208waeqsmNgxFnFC88rnV7gTYQw_; _device_id=a7ca73be0e8f1a81d1e2ebb5349f9075; user_session=nbDv62kHNjp4N5KyQNYZ208waeqsmNgxFnFC88rnV7gTYQw_; logged_in=yes; dotcom_user=Germey; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; _gh_sess=your_session_info',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('<https://github.com/>', headers=headers)
print(r.text)
```

### Session维持

```python
import requests

s = requests.Session()
s.get('<http://httpbin.org/cookies/set/number/123456789>')
r = s.get('<http://httpbin.org/cookies>')
print(r.text)
```

### SSL证书验证

```python
import requests

response = requests.get('<https://static2.scrape.center/>', verify=False)
print(response.status_code)
```

### 超时设置

在本机网络状况不好或者服务器网络响应延迟甚至无响应时，我们可能会等待很久才能收到响应，甚至到最后收不到响应而报错。为了防止服务器不能及时响应，应该设置一个超时时间，即超过了这个时间还没有得到响应，那就报错。这需要用到 timeout 参数。这个时间的计算是发出请求到服务器返回响应的时间。

```python
import requests

r = requests.get('<https://httpbin.org/get>', timeout=1)
print(r.status_code)
```

### 身份认证

```python
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('<https://static3.scrape.center/>', auth=HTTPBasicAuth('admin', 'admin'))
print(r.status_code)
```

### 代理设置

```python
import requests

proxies = {
  'http': '<http://10.10.10.10:1080>',
  'https': '<http://10.10.10.10:1080>',
}
requests.get('<https://httpbin.org/get>', proxies=proxies)
```

若代理需要使用上文所述的身份认证，可以使用类似 http://user:password@host:port 这样的语法来设置代理，示例如下：

```python
import requests

proxies = {'https': '<http://user:password@10.10.10.10:1080/>',}
requests.get('<https://httpbin.org/get>', proxies=proxies)
```