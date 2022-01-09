## 原因
*写这个笔记的原因是因为实训做的博客中又出现了只在前端就能访问服务器的状况，对于这种请求访问很疑惑，有时候在前端，有时候在后端，还有一个吊毛request对象不知道是啥。后来又学了一个[Python的套接字socket](https://cloud.tencent.com/developer/article/1078620)，让我感觉这是我穿起来网络，把整个客户端服务器连成一个电脑的机会，所以就socket展开学习*  

> 注：对于socket的函数学习可以参考https://www.hiyu.space/2021/02/28/C-socket%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/

## 什么是分布式？

就是一个系统，有多个不同地区的计算机构成，这些计算机在网络连接的时候可以看成是一台电脑

## 分布式长什么样？

具体可以参考这篇文章：https://blog.csdn.net/weixin_42449639/article/details/103376251 ，里面有好几个比如c/s，或者p2p，或者远程连接的样式，现在主要用一用远程连接  
![image](https://user-images.githubusercontent.com/74129445/148672218-c1662349-a649-4c15-8e1b-89e8dcfd2217.png)  

注：一般情况下，函数只能返回一个返回值

## 什么是socket?
为了与远程计算机进行数据传输，需要连接到因特网，而socket就是用来连接到因特网的工具。  


网络编程就是编写程序使两台联网的计算机相互交换数据。这就是全部内容了吗？是的！网络编程要比想象中的简单许多。那么，这两台计算机之间用什么传输数据呢？首先需要物理连接。如今大部分计算机都已经连接到互联网，因此不用担心这一点。在此基础上，只需要考虑如何编写数据传输程序。但实际上这点也不用愁，因为操作系统已经提供了 socket。即使对网络数据传输的原理不太熟悉，我们也能通过 socket 来编程。  


socket 的典型应用就是 Web 服务器和浏览器：浏览器获取用户输入的 URL，向服务器发起请求，服务器分析接收到的 URL，将对应的网页内容返回给浏览器，浏览器再经过解析和渲染，就将文字、图片、视频等元素呈现给用户。学习 socket，也就是学习计算机之间如何通信，并编写出实用的程序。这和计算机网络中6.2的文件传输协议FTP有些类似  

FTP概述

![image](https://user-images.githubusercontent.com/74129445/148685033-33f3bbbc-5446-49e2-b019-d5df84852cb8.png)  
![image](https://user-images.githubusercontent.com/74129445/148685049-46eac3c4-e5fd-4abf-9810-cfe9f2f668a6.png)  

FTP基本工作原理简直就是一个socket  

![image](https://user-images.githubusercontent.com/74129445/148685116-5db456cc-cafd-4372-86ba-b82d7be015a2.png)  




## socket与远程连接的关系？

