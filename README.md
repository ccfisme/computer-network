## 原因
*写这个笔记的原因是因为实训做的博客中又出现了只在前端就能访问服务器的状况，对于这种请求访问很疑惑，有时候在前端，有时候在后端，还有一个吊毛request对象不知道是啥。后来又学了一个[Python的套接字socket](https://cloud.tencent.com/developer/article/1078620)，让我感觉这是我穿起来网络，把整个客户端服务器连成一个电脑的机会，所以就socket展开学习  

> 注：对于socket的函数学习可以参考https://www.hiyu.space/2021/02/28/C-socket%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/

## 什么是分布式？

就是一个系统，有多个不同地区的计算机构成，这些计算机在网络连接的时候可以看成是一台电脑

## 分布式长什么样？

具体可以参考这篇文章：https://blog.csdn.net/weixin_42449639/article/details/103376251，里面有好几个比如c/s，或者p2p，或者远程连接的样式，现在主要用一用远程连接  
![image](https://user-images.githubusercontent.com/74129445/148672218-c1662349-a649-4c15-8e1b-89e8dcfd2217.png)  


