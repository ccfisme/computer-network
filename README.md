学习视频参考：https://www.bilibili.com/video/BV1ob4y1Y7Ep?p=1&share_medium=android&share_plat=android&share_session_id=50b0e6c5-6796-4e4f-b34d-bdd5113f4b5f&share_source=COPY&share_tag=s_i&timestamp=1641906004&unique_k=DmzCEHB

## cookie目的

浏览器第一次发出请求，用户名密码放在请求信息里，服务器收到，创建cookie，并把cookie的值填充好，然后发给浏览器，浏览器存起来，以后浏览器每一个请求都会添加上这个cookie，以此让服务器判断是否为第一次的那个用户登录，后续就不需要用户名密码就可以登录了

## session目的  

客户端电脑被黑，cookie就很容易泄露，所以更改了cookie存的信息，变成了一个很复杂的字符串，每个字符串对应一组用户名密码，将这个字符串装在cookie返回，以后用这个来判断是否为用户本人登录，而不是用户名密码  

## token目的  

让服务器用数据库存字符串来进行匹配会出现数据库崩溃的情况，这样就没办法进行匹配，所以就出现了token，浏览器第一次发出请求，用户名密码放在请求信息里，服务器收到，创建token字符串，然后并不保存字符串，而是发给浏览器，让浏览器用cookie或者其他形式存这个token字符串，服务器只存解密方法，然后下一次访问时，浏览器发token字符串，服务器解密，这样就会简单很多，让浏览器存密文字符串。
