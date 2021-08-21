#### 基本使用

```python
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
browser = webdriver.Chrome() 
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url) # 当前url
    print(browser.get_cookies()) # 获取cookies
    print(browser.page_source) # 获取浏览器解析的源代码
finally:
    browser.close()
```

#### 声明浏览器

```python
from selenium import webdriver
browser = webdriver.Chrome() 
browser = webdriver.Firefox() 
browser = webdriver.Edge() 
browser = webdriver.Safari()
```

#### 节点定位

```python
# 单个节点
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
# 多个
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
#或者
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```

#### 节点交互

```python
from selenium import webdriver 
import time 
browser = webdriver.Chrome() 
browser.get('https://www.taobao.com') 
input = browser.find_element_by_id('q') 
input.send_keys('iPhone')  # send_keys()输入自符
time.sleep(1) 
input.clear()              # 清空
input.send_keys('iPad') 
button = browser.find_element_by_class_name('btn-search') 
button.click()             # 左键点击
```

#### 动作链

鼠标拖拽、键盘按键等，这些动作用另一种方式来执行，那就是动作链。

```python
from selenium import webdriver 
from selenium.webdriver import ActionChains 
browser = webdriver.Chrome() 
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable' 
browser.get(url) 
browser.switch_to.frame('iframeResult') 
source = browser.find_element_by_css_selector('#draggable') 
target = browser.find_element_by_css_selector('#droppable') 
actions = ActionChains(browser) 
actions.drag_and_drop(source, target) 
actions.perform()
```

#### 执行 JavaScript

```python
from selenium import webdriver 
browser = webdriver.Chrome() 
browser.get('https://www.zhihu.com/explore') 
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') 
browser.execute_script('alert("To Bottom")')
```

#### 切换 Frame

我们知道网页中有一种节点叫作 iframe，也就是子 Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致。Selenium 打开页面后，默认是在父级 Frame 里面操作，而此时如果页面中还有子 Frame，Selenium 是不能获取到子 Frame 里面的节点的。这时就需要使用 switch_to.frame 方法来切换 Frame。示例如下：

```python
import time 
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable' 
browser.get(url) 
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo') 
except NoSuchElementException:
    print('NO LOGO') 
browser.switch_to.parent_frame() 
logo = browser.find_element_by_class_name('logo')
print(logo) 
print(logo.text)
```

#### 隐式等待

当使用隐式等待执行测试的时候，如果 Selenium 没有在 DOM 中找到节点，将继续等待，超出设定时间后，则抛出找不到节点的异常。换句话说，隐式等待可以在我们查找节点而节点并没有立即出现的时候，等待一段时间再查找 DOM

```python
from selenium import webdriver 
browser = webdriver.Chrome() 
browser.implicitly_wait(10) 
browser.get('https://dynamic2.scrape.center/') 
input = browser.find_element_by_class_name('logo-image') 
print(input)
```

#### 显式等待

这里还有一种更合适的显式等待方法，它指定要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有加载出该节点，则抛出超时异常。

```python
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
browser = webdriver.Chrome() 
browser.get('https://www.taobao.com/') 
wait = WebDriverWait(browser, 10)   # 最长等待时间
input = wait.until(EC.presence_of_element_located((By.ID, 'q'))) 
button =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search'))) 
print(input, button)
```

在 10 秒内如果 ID 为 q 的节点（即搜索框）成功加载出来，就返回该节点；如果超过 10 秒还没有加载出来，就抛出异常。

![img](https://s0.lgstatic.com/i/image3/M01/04/3A/Ciqah1596FyAIAjtAAECe0Jujuw745.png)

![img](https://s0.lgstatic.com/i/image3/M01/04/3A/Ciqah1596R2Af973AAEiFfxC3E4161.png)

#### Cookies

使用 Selenium，还可以方便地对 Cookies 进行操作，例如获取、添加、删除 Cookies 等。示例如下：

```python
from selenium import webdriver 
browser = webdriver.Chrome() 
browser.get('https://www.zhihu.com/explore') 

#获取Cookies
print(browser.get_cookies()) 

# 添加Cookies
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'}) 
print(browser.get_cookies()) 

# 删除所有cookies
browser.delete_all_cookies() 
print(browser.get_cookies())
```

#### Webdrive反屏蔽

检测基本原理是检测当前浏览器窗口下的 window.navigator 对象是否包含 webdriver 这个属性。因为在正常使用浏览器的情况下，这个属性是 undefined，然而一旦我们使用了 Selenium，Selenium 会给 window.navigator 设置 webdriver 属性。很多网站就通过 JavaScript 判断如果 webdriver 属性存在，那就直接屏蔽。

在 Selenium 中，我们可以使用 CDP（即 Chrome Devtools-Protocol，Chrome 开发工具协议）来解决这个问题，通过 CDP 我们可以实现在每个页面刚加载的时候执行 JavaScript 代码，执行的 CDP 方法叫作 Page.addScriptToEvaluateOnNewDocument

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=option)

browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
   'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})
browser.get('https://antispider1.scrape.center/')
```

#### 无头模式

Chrome 浏览器从 60 版本已经支持了无头模式，即 Headless。无头模式在运行的时候不会再弹出浏览器窗口，减少了干扰，而且它减少了一些资源的加载，如图片等资源，所以也在一定程度上节省了资源加载时间和网络带宽

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)

browser.set_window_size(1366, 768)
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('preview.png')
```

