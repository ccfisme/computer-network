1.1</br>
没讲啥，就明白了因特网就是互联网这个概念，对Internet的翻译不同而已</br></br>
1.2</br>
先讲的互连网，也就是多个计算机通过路由器连在一起，最初美国发明的是一根线，这根线叫ARPANET，后来用的地方多了，就用一些类似路由器的设备把多个计算机连成一片，这也就是第一个互连网，再后来1983规定了一个TCP/IP协议，只要遵守就可以互相连接，这就是互联网的诞生。</br>
后来发现要想使连接到互联网的所有用户都可以相互通信，单靠线线连接并不可行，如聊城与北京相隔486公里，如果传输一个大型文件，那么一个一个节点一个节点的传，势必会造成堵塞和效率低下，所以可以建一个更大的市级的节点，然后让市与市之间连接，这其实已经解决绝大部份的问题了，不过考虑到更远的比如云南到哈尔滨，这就需要更大的节点，即联通整个国家的节点，这也就是三级ISP结构，(ISP是指交换的节点，其中市级与市级之间可通过IXP直接交换信息)即
![IMG_20210919_154812](https://user-images.githubusercontent.com/74129445/133919723-9676fb3e-13d5-4c52-af4e-6d9ae5b519e2.jpg)</br>
然后简单介绍了万维网，它代表web网页的出现</br></br>
1.3</br>
以工作方式的不同介绍了互联网两个结构</br>
一个是边缘部分，即连接在互联网的所有主机，小的叫个人电脑，大的叫服务器。这些主机之间的通信方式又分为两类。一类是“客户端-服务器”方式，也就是我之前学的Java web，即主机A运行客户端程序，发出请求，主机B运行服务器程序，接收请求作出响应。另一类是“对等连接”方式，即不区分哪个是服务请求方，哪个是服务提供方，只要有对等连接软件P2P，就可以既做服务器，又做客户端，并且这一类可以支持大量对等用户</br>
另一个是核心部分，也就是如何实现的数据传输。就比如两个电话发生信息交互，则需要两根线，一根输入数据，一根输出数据，如果是10000个电话相连接，那么线实在是太多了，所以发明了交换机，即
![截屏2021-09-19 16 24 46](https://user-images.githubusercontent.com/74129445/133920715-bcd8a42c-0f03-40f1-a047-20cf24ea9ca0.png)</br>
不过要想把这种模式转移到计算机方面，就太浪费了，因为在通话的时间内通话的两个用户始终占线，如果我在线编辑一个云保存的文档，岂不是一直都要占用这条线路，实在是浪费，并且计算机的数据都是突发式的出现在传输线路上的，所以后面出现了存储转发技术，即
![截屏2021-09-19 16 50 10](https://user-images.githubusercontent.com/74129445/133921360-80f52be9-64b1-432d-8acb-99718a062418.png)</br>
这里我出现了一个疑问，服务器与路由器的区别有什么？明明都是传输数据的，后来发现这个问题很愚蠢，服务器是存储数据，按请求发送数据，路由器是转发数据，根本是两个东西</br></br>
1.4</br>
