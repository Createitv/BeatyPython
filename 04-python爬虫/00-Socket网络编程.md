## Socket简介

Socket 基于不同的协议可以创建面向连接和非连接两种套接字，即 TCP 和 UDP 服务。前者提供序列化、非重复的可靠数据传递功能，后者在通信之前无需创建连接，但不能保证数据的顺序性，而且有可能收不到数据或收到重复数据。我们的课程主要介绍基于 TCP 协议的套接字，在后面的章节中会不断创建 TCP 客户端。

网络套接字 Network socket 又称为网络接口、网络插槽，是计算机网络进程间数据流的端点。套接字是操作系统提供的进程间的通信机制，相当于前文所讲的 “通信端点” 的概念。在任何类型的通信开始之前，网络应用程序必须创建套接字。

套接字的起源可以追溯到 20 世纪 70 年代，它是加利福尼亚大学的伯克利版本 UNIX 的一部分。因此，有时你可能会听过将套接字称为伯克利套接字或 BSD 套接字。套接字最初是为同一主机上的应用程序所创建，使得主机上运行的一个程序（也可以说一个进程）与另一个运行的程序进行通信。这就是所谓的进程间通信。有两种类型的套接字：基于文件的和面向网络的。

Socket 对外提供了一套丰富的接口，通过这些接口就可以统一、方便地使用 TCP/IP 协议。下面所列的是最常用的几个，我们在后面的学习中会用到它们。

- socket 创建 socket 实例
- bind 绑定地址和端口
- listen 开始监听网络
- accept 接收客户端连接
- connect 连接服务器
- send 发送数据
- recv 接收数据
- close 关闭 socket

这几个接口在学习 Socket 时，是经常用到的。尤其是在 C/S (客户端/服务端) 模式中，整个流程是比较统一简单的。

![图片描述](https://doc.shiyanlou.com/courses/uid770606-20190924-1569295003865))

这是一个 TCP 连接的基本流程，下面讲解如何实现。

## TCP Socket

TCP 是使用最广泛的网络协议，它会保证网络的可靠性，有序性。大多数网络连接都使用 TCP 连接，例如浏览器的 HTTP 协议和邮件的 SMTP 协议，都是建立在 TCP 协议基础上。创建 TCP 连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。创建连接需要确定四点：IP 类型、协议、IP 地址、端口号。

通常使用 socket.socket 函数来创建套接字。因为服务器需要占用一个端口并等待客户端的请求，所以 TCP 套接字必须绑定到一个本地地址（IP 端口元组）。因为 TCP 是一种面向连接的通信系统，所以在 TCP 服务器开始操作之前，必须安装一些基础设施。需要注意的一点，TCP 服务器必须一直监听传入的连接。一旦这个安装过程完成后，服务器就可以开始它的无限循环。

TCP 服务器调用 accept 方法之后，就开启了一个简单的单线程服务器，它会等待客户端的连接。默认情况下，accept 方法是阻塞的，后续代码的执行将被暂停，直到与一个客户端建立连接。套接字也支持非阻塞运行，后面的课程会讲到。当客户端向服务器发起连接请求，服务器接受连接后，就会利用 accept 方法返回一个临时独立的套接字，用来处理客户端发送过来的消息。此时服务器套接字仍可接收其它客户端的连接，但需要等待前一个客户端完成消息收发并断开连接，然后处理下一个客户，这也是最简单的单线程服务器的限制所在。最后，遇到某些外部条件，可以使用 close 方法关闭套接字。

要创建套接字，需使用 `socket.socket` 方法，语法如下：

```python
import socket
socket.socket(socket_family, socket_type)
```

参数说明：

1、socket_family : 套接字家族

| 套接字家族 | 说明                 |
| ---------- | -------------------- |
| AF_UNIX    | 基于文件的套接字家族 |
| AF_INET    | 面向网络的套接字家族 |

2、socket_type : 套接字传输类型

| 套接字类型  | 说明                                      |
| ----------- | ----------------------------------------- |
| SOCK_STREAM | 创建 TCP 套接字时使用，面向连接，数据流式 |
| SOCK_DGRAM  | 创建 UDP 套接字时使用，无连接，数据报式   |

TCP 为面向连接的网络套接字，可以使用下面的方式创建：

```python
import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

## Socket服务端和客户端

下面的代码是一个 TCP 服务器程序，它接收客户端发送的数据字符串，将其打上 `[ShiYanLou]` 标签并返回给客户端。将代码写入 tcp_server.py 文件：

```python
# File Name: tcp_server.py
from socket import socket, AF_INET, SOCK_STREAM

# 预先定义好 IP PORT 地址元组
# IP 值为空字符串，表示接收任意 IP 地址的客户端，PORT 值为任意未占用端口号
ip_port = ('', 1234)

# 定义 TCP 服务器套接字
tcp_server_sock = socket(AF_INET, SOCK_STREAM)
# 将地址绑定到套接字上
tcp_server_sock.bind(ip_port)
# 开启服务器监听
tcp_server_sock.listen()

# 进入监听状态后，等待客户端连接
while True:
    # 启动服务器后立即打印该语句，与客户端断开连接后也会打印该语句
    print('Waiting for connection...')
    # 下一行为阻塞运行状态，等待客户端的连接
    # 服务器套接字相当于总机接线员，接到客户电话后转给分机客服
    # 当成功接入一个客户端，accept 方法会返回一个临时套接字和对方地址
    tcp_extension_sock, addr = tcp_server_sock.accept()
    # 如果此时另一个客户端向服务器发送连接请求，也是可以的
    # 连接成功后保持等待，前一个已连接的客户端断开连接后，才会处理下一个
    print('Connected from: {}'.format(addr))
    while True:
        # 临时服务端套接字的 recv 方法获得客户端传来的数据
        # 此方法也是阻塞运行，每次接收固定量的数据，直到全部接收完毕
        # recv 的参数为数据缓存区字节数，通常定义为 1024
        data = tcp_extension_sock.recv(1024)
        if not data:
            break
        # data 为二进制对象，将其转换为 UTF-8 格式
        print('收到数据：{}'.format(data.decode()))
        # 临时服务端套接字的 send 方法向客户端发送数据
        # data 为二进制对象，将其转换为 UTF-8 格式，再整体转换为二进制对象
        tcp_extension_sock.send('{} {}'.format(
            '[ShiYanLou]', data.decode()).encode())
    # while 循环结束后，关闭临时服务器套接字
    tcp_extension_sock.close()
# 主动关闭服务器（正常情况下这步不会发生）
tcp_server_sock.close()
```

现在创建对应的客户端，将以下代码写入 tcp_client.py 文件中：

```python
from socket import socket, AF_INET, SOCK_STREAM

# 定义客户端套接字
tcp_client_sock = socket(AF_INET, SOCK_STREAM)
# 向服务器发送连接请求，IP 地址为服务器的 IP 地址
# 注意 connect 方法的参数为元组
tcp_client_sock.connect(('localhost', 1234))

# 连接成功后，进入发送/接收数据循环
while True:
    data = input('输入内容：')
    if not data:
        break
    # 发送二进制数据
    tcp_client_sock.send(data.encode())
    # 接收二进制数据
    data = tcp_client_sock.recv(1024)
    if not data:
        break
    print(data.decode())
# 关闭客户端套接字
tcp_client_sock.close()
```

客户端相对来说比较简单，首先创建 socket 实例，和服务端是相同的。然后使用 connect 方法进行连接服务端，此方法也是阻塞运行的，在连接上服务端之后继续执行，再向服务端发送数据，并且会接收服务端返回的数据。最后关闭客户端套接字。

服务器和客户端代码编写完毕，现在尝试运行它们。

在一个终端打开多个标签，首先启动服务器：

```bash
$ python3 tcp_server.py
Waiting for connection...
```

在另一个标签中启动客户端：

```bash
$ python3 tcp_client.py
输入内容：
```

客户端会阻塞住，等待终端输入。此时服务器的状态：

```bash
$ python3 tcp_server.py
Waiting for connection...
Connected from: ('127.0.0.1', 62446)
```

在客户端输入信息，按回车发送：

```bash
$ python3 tcp_client.py
输入内容：Hello, World
[ShiYanLou] Hello, World
输入内容：shiyanlou
[ShiYanLou] shiyanlou
输入内容：
```

此时服务器的状态：

```bash
$ python3 tcp_server.py
Waiting for connection...
Connected from: ('127.0.0.1', 62520)
收到数据：Hello World
收到数据：shiyanlou
```

我们向服务器发送数据，服务器收到数据后，在数据前面添加 [ShiYanLou] 字样，返回给客户端。这样会看到服务端打印接收到的客户端发送的信息，同时客户端也会收到服务端发送的数据。这样客户端和服务端完成了通信。

在客户端不输入数据直接按回车即可关闭客户端，客户端与服务器的连接自动断开：

```bash
$ python3 tcp_client.py
输入内容：Hello World
[ShiYanLou] Hello World
输入内容：shiyanlou
[ShiYanLou] shiyanlou
输入内容：
$
```

此时服务器会进入下一个 while 循环：

```bash
$ python3 tcp_server.py
Waiting for connection...
Connected from: ('127.0.0.1', 62557)
收到数据：Hello World
收到数据：shiyanlou
Waiting for connection...
```

这就是服务器启动后，客户端与服务器建立连接并收发数据最后断开连接的完整流程。

## 多线程服务端

上文创建的服务器套接字为单线程运行，虽然可以接收多个客户端的连接，但处理下一个连接必须等待上一个连接断开。将上文代码的内层 while 循环收发消息的代码写入一个函数，采用多线程方式运行，可以实现并发处理客户端连接，达到同时处理多个连接的效果。

将以下多线程服务器代码写入 server_threading.py 文件：

```python
# File Name: server_threading.py
import threading
from socket import socket, AF_INET, SOCK_STREAM

ADDR = ('', 1234)
BUFSIZ = 1024
tcp_server_sock = socket(AF_INET, SOCK_STREAM)
tcp_server_sock.bind(ADDR)
tcp_server_sock.listen()

def handle(sock, addr):
    while True:
        # 套接字的 recv 方法阻塞等待，直到客户端发送消息过来
        # 阻塞等待期间释放 CPU ，CPU 可以执行其它线程中的任务
        data = sock.recv(BUFSIZ).decode()
        if not data:
            sock.close()
            break
        print('收到信息：{}'.format(data))
        sock.send(
            '[{}] {}'.format('ShiYanLou', data).encode())
    # 关闭临时服务器套接字
    sock.close()
    print('{} 已关闭'.format(addr))

def main():
    print('等待客户端请求...')
    # 进入无限循环，每出现一个客户端请求，就会循环一次，创建一个子线程
    # 这样可以创建多个线程来并发处理多个客户端请求
    while True:
        # 这个 try 语句是为了捕获终端 Ctrl + C 结束程序时触发的 Keyboard 异常
        # 捕获异常后，while 循环可能并不会立刻结束
        # 它会阻塞等待，直到所有子线程结束后结束
        try:
            tcp_extension_sock, addr = tcp_server_sock.accept()
        except KeyboardInterrupt:
            break
        # 创建子线程，运行前面定义的 handle 任务
        t = threading.Thread(
            target=handle, args=(tcp_extension_sock, addr))
        t.start()
    # while 循环结束，关闭服务器套接字，退出程序
    print('\nExit')
    tcp_server_sock.close()

if __name__ == '__main__':
    main()
```

启动服务器后，每个客户端连接成功后，会创建一个临时套接字，余下的任务交由一个新建子线程来执行，主线程继续等待新的连接。这样就实现了同时处理多个连接的功能。

首先，在一个终端标签中启动服务端：

```bash
$ python3 server_threading.py
等待客户端请求...
```

客户端代码是通用的，保存在 tcp_client.py 文件中。在另一个终端标签中启动客户端，定为 1 号客户端：

```bash
$ python3 tcp_client.py
输入内容：
```

此时服务器状态：

```bash
$ python3 server_threading.py
等待客户端请求...
```

为了验证多线程服务器的并发效果，再打开一个终端标签，启动另一个客户端，定为 2 号客户端：

```bash
$ python3 tcp_client.py
输入内容：
```

此时服务器的状态：

```bash
$ python3 server_threading.py
等待客户端请求...
Connected from ('127.0.0.1', 63325)
Connected from ('127.0.0.1', 63360)
```

在 1 号客户端中输入以下内容，按回车发送：

```bash
python3 tcp_client.py
输入内容：1，晴空一鹤排云上
[ShiYanLou] 1，晴空一鹤排云上
输入内容：
```

在 2 号客户端中输入以下内容，按回车发送：

```bash
python3 tcp_client.py
输入内容：2，杨柳青青江水平
[ShiYanLou] 2，杨柳青青江水平
输入内容：
```

此时服务器的状态：

```bash
$ python3 server_threading.py
等待客户端请求...
Connected from ('127.0.0.1', 63325)
Connected from ('127.0.0.1', 63360)
收到信息：1，晴空一鹤排云上
收到信息：2，杨柳青青江水平
```

如上所示，这样就实现了服务器同时处理多个客户端连接的功能。

在两个客户端分别不输入数据按下回车键关闭它们：

```bash
# 1 号客户端
$ python3 tcp_client.py
输入内容：1, 晴空一鹤排云上
[ShiYanLou] 1晴空一鹤排云上
输入内容：
$

# 2 号客户端
$ python3 tcp_client.py
输入内容：2，杨柳青青江水平
[ShiYanLou] 2，杨柳青青江水平
输入内容：
$
```

此时服务器的状态：

```bash
$ python3 server_threading.py
等待客户端请求...
Connected from ('127.0.0.1', 63325)
Connected from ('127.0.0.1', 63360)
收到信息：1，晴空一鹤排云上
收到信息：2，杨柳青青江水平
('127.0.0.1', 63325) 已关闭
('127.0.0.1', 63360) 已关闭
```

按快捷键 Ctrl + C 可以关闭服务器套接字，终止 server_threading.py 脚本。

在接收到一个客户端请求时会启动一个线程对客户端进行处理，这样就可以同时处理多个客户端请求了。虽然 Python 的线程有全局锁 (GIL) 的限制，一个进程中只有一个 CPU 在执行，但是在线程遇到 I/O 操作时会释放 GIL，让出控制权，CPU 会切换到其它线程中工作。

## IO多路复用

计算机有运算器、控制器、存储器、输入设备、输出设备五部分组成，CPU 作为运算器，执行运算，速度是最快的。存储器，输入输出设备存储数据，供 CPU 读写数据，在距离 CPU 的越远读写速度就会越慢。内存读写数据、磁盘寻址、网络传输相对于 CPU 运算都是很慢的。CPU 在需要数据时是通过 I/O 传输数据，I/O 速度较慢，CPU 大部分时间都是在等待 I/O 完成操作，浪费了大量的时间。I/O 成了最大的性能瓶颈。

Linux 系统进程运行时分为内核态和用户态，运行于用户态的进程可以执行的操作和访问的资源都会受到极大的限制，而运行在内核态的进程则可以执行任何操作并且在资源的使用上没有限制。很多程序开始时运行于用户态，但在执行的过程中，一些操作需要在内核权限下才能执行，这时需要从用户态切换到内核态。

网络通信是两个主机之间的通信，一个主机通过网线将数据发送到另一台主机，网络在进行数据传输时，需要用户态和内核态的转换，整个流程如下：

- 操作系统将数据从网络中接收数据并将其复制到系统内核的缓存中
- 应用程序将数据从内核缓存复制到应用的缓存中
- 应用程序将处理完之后的数据再写回内核的 Socket 缓存中
- 操作系统将数据从 Socket 缓存区复制到网卡缓存，然后将其通过网络发出

整个过程中，相比 CPU 的运行 I/O 操作是非常耗时的，可以看一下 CPU 时间对比：

| 操作                      | 真实时间 | 相对时间      |
| ------------------------- | -------- | ------------- |
| L1 缓存                   | 0.5 纳秒 | 1.3 秒        |
| 分支纠错                  | 5 纳秒   | 13 秒         |
| L2 缓存                   | 7 纳秒   | 18.2 秒       |
| 加/解互斥锁               | 25 纳秒  | 1 分 5 秒     |
| 内存寻址                  | 100 纳秒 | 4 分 20 秒    |
| 上下文切换/系统调用       | 1.5 微秒 | 1 小时 5 分钟 |
| 1Gbps 网络传输 2KB 数据   | 20 微秒  | 14.4 小时     |
| 从内存对 1M 连续数据      | 250 微秒 | 7.5 天        |
| ping 同数据中心的两台主机 | 0.5 毫秒 | 15 天         |
| 磁盘寻址                  | 1 毫秒   | 30 天         |
| 从磁盘读 1M 连续数据      | 20 毫秒  | 20 个月       |
| 通过网络城市直接发送数据  | 150 毫秒 | 12.5 年       |

相对于 CPU ，网络的性能差了几个数量级，网络 I/O 是最大的瓶颈。为了提升 I/O 性能，操作系统提供了高性能的异步 IO 模型，异步 I/O 是一个比较好的解决方案，性能得到了大幅的提升。

Linux 系统中有五种 I/O 模型，需要重点介绍的是 I/O 多路复用模型，广泛使用的 I/O 多路复用有 select 、poll 、epoll 这三种，我们会介绍这几种技术的优缺点，并使用 Python 的 select 模块提供的接口，分别实现服务端。

## Socket同步阻塞爬虫

阻塞是 socket 模块的默认设置，现在我们以阻塞方式实现一个爬虫程序，爬取实验楼网站的某些课程图片并保存。

代码编写思路：

- 首先创建一个 socket 客户端
- 然后与保存图片的服务器创建连接
- 连接成功后向服务器发送下载图片的请求
- 接收服务器返回的数据并保存

课程图片共十张，地址：

```txt
https://dn-simplecloud.shiyanlou.com/ncn1.jpg
https://dn-simplecloud.shiyanlou.com/ncn110.jpg
https://dn-simplecloud.shiyanlou.com/ncn109.jpg
https://dn-simplecloud.shiyanlou.com/1548126810319.png
https://dn-simplecloud.shiyanlou.com/1517282865454.png
https://dn-simplecloud.shiyanlou.com/1543913883545.png
https://dn-simplecloud.shiyanlou.com/1502778396172.png
https://dn-simplecloud.shiyanlou.com/1540965522764.png
https://dn-simplecloud.shiyanlou.com/1546500900109.png
https://dn-simplecloud.shiyanlou.com/1547620906601.png
```

将以下代码写入 spider_sync_blocking.py 文件中：

```python
# File Name: spider_sync_blocking.py

import time
import os
import socket
from urllib.parse import urlparse

# 需要爬取图片的地址列表
urls = ['https://dn-simplecloud.shiyanlou.com/ncn1.jpg',
        'https://dn-simplecloud.shiyanlou.com/ncn110.jpg',
        'https://dn-simplecloud.shiyanlou.com/ncn109.jpg',
        'https://dn-simplecloud.shiyanlou.com/1548126810319.png',
        'https://dn-simplecloud.shiyanlou.com/1517282865454.png',
        'https://dn-simplecloud.shiyanlou.com/1543913883545.png',
        'https://dn-simplecloud.shiyanlou.com/1502778396172.png',
        'https://dn-simplecloud.shiyanlou.com/1540965522764.png',
        'https://dn-simplecloud.shiyanlou.com/1546500900109.png',
        'https://dn-simplecloud.shiyanlou.com/1547620906601.png'
]


# 定义一个爬虫类
class Crawler:
    def __init__(self, url):
        self.url = url              # 定义该属性，方便后续使用
        self.receive_data = b''     # 该属性用来保存从服务器接收的二进制数据

    def fetch(self):
        # urlparse 方法用来处理 URL ，其返回值便于获得域名和路径
        url = urlparse(self.url)
        # 创建 socket 实例
        self.sock = socket.socket()
        # 该方法阻塞运行，直到成功连接服务器，Web 服务器端口通常为 80
        self.sock.connect((url.netloc, 80))
        print('连接成功')
        # 创建保存图片的目录 pic
        os.system('mkdir -p pic')
        # 向服务器发送的数据的固定格式
        # 使用 HTTP/1.1 需要设置 Connection 为 close，默认是Keep-Alive
        # 默认值会保持连接，如果数据发送完毕，连接不会断开，方便下次连接使用
        # 保持连接会占用资源影响爬虫效率，我们的爬虫不需要
        data = 'GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(
                url.path, url.netloc)
        # 向服务器发送数据，阻塞运行
        self.sock.send(data.encode())
        # 接收服务器返回的数据，阻塞运行
        while True:
            # 每次至多接收 1K 数据
            d = self.sock.recv(1024)
            if d:
                self.receive_data += d
            else:
                break
        print('接收数据成功')
        # 第一个参数为文件名，注意 url.path 的值的第一个字符为斜杠，须去掉
        # 从服务器接收到的数据为二进制，其中第一部分为报头，第二部分为图片数据
        # 两部分之间使用 \r\n\r\n 隔开，选择第二部分存入文件
        with open('pic/{}'.format(url.path[1:]), 'wb') as f:
            f.write(self.receive_data.split(b'\r\n\r\n')[1])
        print('保存文件成功')
        self.sock.close()

def main():
    start = time.time()
    for url in urls:
        # 创建爬虫实例
        crawler = Crawler(url)
        # 开始爬取数据
        crawler.fetch()
    print('耗时：{:.2f}s'.format(time.time() - start))

if __name__ == '__main__':
    main()
```

终端运行程序：

```bash
$ python3 spider_sync_blocking.py
连接成功
接收数据成功
保存文件成功

... ...

连接成功
接收数据成功
保存文件成功
耗时：1.04s
```

查看保存图片的目录结构：

```bash
$ tree pic
pic
├── 1502778396172.png
├── 1517282865454.png
├── 1540965522764.png
├── 1543913883545.png
├── 1546500900109.png
├── 1547620906601.png
├── 1548126810319.png
├── ncn1.jpg
├── ncn109.jpg
└── ncn110.jpg

0 directories, 10 files
```

![图片描述](https://doc.shiyanlou.com/courses/uid310176-20190808-1565247204228)

执行程序三五次，选择耗时的中位数作为程序运行耗时，我这里测试程序运行耗时也就是 1.1 秒上下。

后面我们会对程序进行修改，现在的程序运行耗时会与修改后的程序运行耗时作比较。

## Socket多线程爬虫

使用多线程实现异步爬虫。多线程爬虫在原理上应该明显减少程序运行耗时，因为爬取网络图片属于 IO 密集型操作，这种场景最适合多线程发挥作用而且丝毫不受 GIL 全局锁的影响。

```python
# File Name: spider_threading.py
import os
import time
import threading
import socket
from urllib.parse import urlparse

# 需要爬取图片的地址列表
urls = ['https://dn-simplecloud.shiyanlou.com/ncn1.jpg',
        'https://dn-simplecloud.shiyanlou.com/ncn110.jpg',
        'https://dn-simplecloud.shiyanlou.com/ncn109.jpg',
        'https://dn-simplecloud.shiyanlou.com/1548126810319.png',
        'https://dn-simplecloud.shiyanlou.com/1517282865454.png',
        'https://dn-simplecloud.shiyanlou.com/1543913883545.png',
        'https://dn-simplecloud.shiyanlou.com/1502778396172.png',
        'https://dn-simplecloud.shiyanlou.com/1540965522764.png',
        'https://dn-simplecloud.shiyanlou.com/1546500900109.png',
        'https://dn-simplecloud.shiyanlou.com/1547620906601.png'
]


# 定义一个爬虫类
class Crawler(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.response = b''

    def run(self):
        # urlparse 方法用来处理 URL ，其返回值便于获得域名和路径
        url = urlparse(self.url)
        # 创建 socket 实例
        self.sock = socket.socket()
        # 该方法阻塞运行，直到成功连接服务器，Web 服务器端口通常为 80
        self.sock.connect((url.netloc, 80))
        print('连接成功', url.path)
        # 向服务器发送的数据的固定格式
        data = 'GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(
            url.path, url.netloc)
        # 向服务器发送数据，阻塞运行
        self.sock.send(data.encode())
        # 接收服务器返回的数据，阻塞运行
        while True:
            # 每次接收 1K 数据
            d = self.sock.recv(1024)
            if d:
                self.response += d
            else:
                break
        print('接收数据成功', url.path)
        os.system('mkdir -p pic')
        with open('pic/{}'.format(url.path[1:]), 'wb') as f:
            f.write(self.response.split(b'\r\n\r\n')[1])
        print('保存文件成功', url.path)
        self.sock.close()

def main():
    start = time.time()
    crawler_list = []
    for url in urls:
        # 创建爬虫实例
        crawler = Crawler(url)
        crawler_list.append(crawler)
        # 开始爬取数据
        crawler.start()
    # 将主线程挂起，直到全部子线程内的爬虫程序运行完毕
    for crawler in crawler_list:
        crawler.join()
    print('耗时：{:.2f}s'.format(time.time() - start))

if __name__ == '__main__':
    main()
```

Crawler 类继承 threading.Thread 类，在线程启动之后会执行 run 方法，run 方法里执行爬取工作。

终端运行程序如下：

```bash
$ python3 spider_threading.py
连接成功 /ncn1.jpg
连接成功 /ncn109.jpg
连接成功 /1540965522764.png
连接成功 /1547620906601.png
连接成功 /ncn110.jpg
连接成功 /1543913883545.png
连接成功 /1548126810319.png
连接成功 /1502778396172.png
连接成功 /1546500900109.png
连接成功 /1517282865454.png
接收数据成功 /1540965522764.png
保存文件成功 /1540965522764.png
接收数据成功 /1548126810319.png
接收数据成功 /ncn1.jpg
保存文件成功 /1548126810319.png
保存文件成功 /ncn1.jpg
接收数据成功 /ncn109.jpg
保存文件成功 /ncn109.jpg
接收数据成功 /1543913883545.png
接收数据成功 /1547620906601.png
保存文件成功 /1543913883545.png
保存文件成功 /1547620906601.png
接收数据成功 /ncn110.jpg
保存文件成功 /ncn110.jpg
接收数据成功 /1502778396172.png
保存文件成功 /1502778396172.png
接收数据成功 /1546500900109.png
保存文件成功 /1546500900109.png
接收数据成功 /1517282865454.png
保存文件成功 /1517282865454.png
耗时：0.19s
$
```

可以看出程序运行的速度快了很多，几乎瞬间完成，运行耗时在理论上应该是同步阻塞程序的十分之一，考虑到创建线程和线程切换的时间开销，也是合理的。在一定范围内，爬取的数据量越大，多线程的高效越明显，必要的时候可以使用线程池。

另外注意一下多线程程序的打印信息不像同步程序那样有规律，这也是多线程的特点。

虽然 Python 有 GIL 的限制，一个进程中有多个线程，但同一时刻只能有一个 CPU 在进程中运行，但是在遇到 I/O 操作时会释放 CPU 进行线程切换，让出控制权。

## Socket I/O异步爬虫

多线程虽然提升了很大的性能，但是当面对成百上千的并发时，要创建大量的线程，线程的资源消耗比较大，线程上下文切换时也会消耗时间，这样性能就会大幅下降。

如何在一个线程里，同时进行多个请求呢？

通过前面的学习，我们知道 I/O 多路复用可以在一个线程里并发处理多个请求，使用 select，poll，epoll 创建服务端，可以并发的处理多个客户端请求。

在 Python 中，selectors 模块可以获取到系统里最好的异步处理方法，一般 Linux 中是 epoll，Mac 上是 Kqueue，并且提供了统一的接口。

在 spider_sync_blocking.py 文件的基础上进行修改，将以下代码写入 spider_selectors.py 文件中：

```python
# File Name: spider_selectors.py

import os
import time
import socket
from urllib.parse import urlparse
# selectors 是对 select 的封装，它会根据不同的操作系统自动选择适合的系统调用
# DefaultSelector 类的实例是系统调用，类似 select、poll、epoll
# EVENT_READ 和 EVENT_WRITE 是事件常数，值为 1 和 2
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
# 需要爬取图片的地址列表
urls = ['https://dn-simplecloud.shiyanlou.com/ncn1.jpg',
        'https://dn-simplecloud.shiyanlou.com/ncn110.jpg',
        'https://dn-simplecloud.shiyanlou.com/ncn109.jpg',
        'https://dn-simplecloud.shiyanlou.com/1548126810319.png',
        'https://dn-simplecloud.shiyanlou.com/1517282865454.png',
        'https://dn-simplecloud.shiyanlou.com/1543913883545.png',
        'https://dn-simplecloud.shiyanlou.com/1502778396172.png',
        'https://dn-simplecloud.shiyanlou.com/1540965522764.png',
        'https://dn-simplecloud.shiyanlou.com/1546500900109.png',
        'https://dn-simplecloud.shiyanlou.com/1547620906601.png'
]

# 创建保存图片的目录 pic
os.system('mkdir -p pic')


# 该类用来模拟发送「协助事件循环停止运行」的信号
class Signal:
    def __init__(self):
        self.stop = False


signal = Signal()


# 定义一个爬虫类
class Crawler:
    def __init__(self, url):
        # urlparse 方法用来处理 URL ，其返回值便于获得域名和路径
        self.url = urlparse(url)
        self._url = url
        self.response = b''

    def fetch(self):
        # 创建 socket 实例
        self.sock = socket.socket()
        # 将客户端套接字设置为非阻塞模式
        self.sock.setblocking(False)
        try:
            # 连接需要时间，非阻塞模式下这里会报出 BlockingIOError 异常
            self.sock.connect((self.url.netloc, 80))
        except BlockingIOError:
            pass
        # 向 selector 这个系统调用中注册套接字的可写事件
        # 参数为套接字的文件描述符、事件常数、回调函数
        # 当连接服务器成功后，可写事件会立即就绪，然后自动执行对应的回调函数
        # 注意回调函数的执行不是由操作系统决定的，而是由 selector 内部控制
        selector.register(self.sock.fileno(), EVENT_WRITE, self.writable)

    # 套接字可写事件就绪后，自动运行此回调函数
    # 所有回调函数的参数都是固定的：SelectorKey 实例，事件常数（选填）
    def writable(self, key):
        # 可写事件就绪后，这个事件就不需要再监听了，注销此事件
        # 不注销的话，selector 就一直提醒事件已就绪
        # SelectorKey 实例的 fd 属性值为对应的套接字的文件描述符
        selector.unregister(key.fd)
        print('连接成功', key.fd)
        # 向服务器发送数据，这是网页请求的固定格式
        data = 'GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(
            self.url.path, self.url.netloc)
        self.sock.send(data.encode())
        print('发送数据成功', key.fd)
        # 接收数据后，监视套接字的可读事件并设置回调函数
        # 在套接字的可读事件就绪后，自动运行回调函数
        selector.register(self.sock.fileno(), EVENT_READ, self.readable)

    # 套接字可读事件就绪后，自动运行此回调函数
    # 可读事件就绪，并不代表内核空间已经接收完全部数据
    def readable(self, key):
        print('接收数据', key.fd)
        # 接收服务器返回的数据，注意这步是从内核空间复制数据到用户空间
        # 每次最多接收 100K 数据，如果数据量比较大，该回调函数会运行多次
        # 只要内存空间里有数据，相关套接字的可读事件就会就绪
        # 所以每次 recv 方法收到的数据很可能不足 100k
        d = self.sock.recv(102400)
        if d:
            self.response += d
        else:
            # 可读事件一直被监听，直到接收数据为空，接收完毕
            # 就不需要再监听此事件了，注销它
            selector.unregister(key.fd)
            print('接收数据成功', key.fd)
            # 注意第一个参数 self.url.path 的第一个字符为斜杠，须去掉
            # 接收到的数据为二进制，其中第一部分为报头，第二部分为图片数据
            # 两部分之间使用 \r\n\r\n 隔开，选择第二部分存入文件
            with open(self.url.path[1:], 'wb') as f:
                f.write(self.response.split(b'\r\n\r\n')[1])
            print('保存文件成功')
            self.sock.close()
            # 接收数据完毕，从需要爬取的地址列表中删除此地址
            urls.remove(self._url)
            # 如果地址列表为空
            # 修改 signal 的属性值，停止 loop 函数中的 while 循环
            if not urls:
                signal.stop = True


def loop():
    # 事件循环，不停地查询被监听的事件是否就绪
    while not signal.stop:
        print('-------------------')
        # selector.select 方法为阻塞运行
        # 轮询被监听事件，如有事件就绪，立即返回就绪事件列表
        # 该方法的功能类似于 select().select 方法，具体用法不同
        events = selector.select()
        # 事件列表中每个事件是一个元组，元组里有俩元素
        # 分别是 SelectorKey 对象和事件常数
        print(events)
        # 事件常数暂时无用，用一个下划线接收它
        for event_key, _ in events:
            # SelectorKey 对象的 data 属性值就是回调函数
            callback = event_key.data
            # 运行回调函数
            callback(event_key)


def main():
    start = time.time()
    for url in urls:
        # 创建爬虫实例
        crawler = Crawler(url)
        # 执行此方法后，将创建一个套接字，套接字向服务器发送连接请求后
        # 将套接字的可写事件注册到 selector 中
        crawler.fetch()
    loop()  # 运行事件循环 + 回调函数
    print('耗时：{:.2f}s'.format(time.time() - start))


if __name__ == '__main__':
    main()
```

在一个终端里执行程序：

```bash
$ python3 spider_selectors.py
-------------------
[(SelectorKey(fileobj=4, fd=4, events=2, data=<bound method Crawler.writable of <__main__.Crawler object at 0x102972b00>>), 2), (SelectorKey(fileobj=7, fd=7, events=2, data=<bound method Crawler.writable of <__main__.Crawler object at 0x102972dd8>>), 2)]
连接成功 4
发送数据成功 4
连接成功 7
发送数据成功 7
-------------------
[(SelectorKey(fileobj=8, fd=8, events=2, data=<bound method Crawler.writable of <__main__.Crawler object at 0x102972e48>>), 2)]
连接成功 8
发送数据成功 8
-------------------
[(SelectorKey(fileobj=9, fd=9, events=2, data=<bound method Crawler.writable of <__main__.Crawler object at 0x102972eb8>>), 2)]
连接成功 9
发送数据成功 9
-------------------
[(SelectorKey(fileobj=11, fd=11, events=2, data=<bound method Crawler.writable of <__main__.Crawler object at 0x102972f98>>), 2)]
连接成功 11
发送数据成功 11
-------------------
[(SelectorKey(fileobj=10, fd=10, events=2, data=<bound method Crawler.writable of <__main__.Crawler object at 0x102972f28>>), 2)]
连接成功 10
发送数据成功 10

... ...

-------------------
[(SelectorKey(fileobj=10, fd=10, events=1, data=<bound method Crawler.readable of <__main__.Crawler object at 0x102972f28>>), 1)]
接收数据 10
-------------------
[(SelectorKey(fileobj=10, fd=10, events=1, data=<bound method Crawler.readable of <__main__.Crawler object at 0x102972f28>>), 1)]
接收数据 10
接收数据成功 10
保存文件成功
耗时：0.15s
```

程序运行时间极短，打印信息较多，只截取首尾的部分。如果去掉代码中的打印信息部分，程序运行耗时会更短。这就是 IO 多路复用在单线程上的巨大优势。

程序运行流程简单描述：

- 1、创建 10 个客户端套接字，分别连接 10 张图片的服务器
- 2、连接成功后将套接字的写事件注册到 selector 上被监视
- 3、开始 loop 事件循环，打印信息就是从这里开始
- 4、当有套接字调用 writable 回调函数发送数据成功后，selector 将监视其读事件
- 5、当有套接字调用 readable 回调函数接收完全部数据，将 URL 从 URL 列表中删除
- 6、当全部套接字接收完毕数据，信号对象 signal 的 stop 属性变成 True，loop 函数的 while 循环结束

## 总结

我们写了三个简单的图片爬取程序，使用不同的方法实现：阻塞式，线程式，I/O 异步。

阻塞式的实现方式最简单，对于开发来说效率最高，但是性能最差，请求时间最长。使用线程请求时，性能提升明显，实现方式稍微复杂，但是线程消耗资源比较大，在并发量大时，性能也会直线下降。I/O 异步请求在一个线程里可以并发请求，在我们的程序中图片数量较少，单张图片的体积小，性能提升和线程模式相比几无差别，由于避免了线程创建和上下文切换，在并发量大的场景下性能也不会有显著下降，这是它的优势，不过在实现方式上复杂度稍高，开发效率最低，代码量增加了很多。



