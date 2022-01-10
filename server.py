import socket
import struct
import json
import os

# 首先创建对象，这个是服务器对象
class MYTCPServer:
    # AF_INET IPv4因特网协议
    address_family = socket.AF_INET
    # SOCK_STREAM 提供顺序的，可靠的双向的基于连接的字节流。可能支持带外数据传输机制。
    socket_type = socket.SOCK_STREAM
    # 一次性允许传输的最大字节数
    max_packet_size = 8192
    # 编码方式
    coding = 'utf-8'
    # 最大连接数
    request_queue_size = 5
    # 服务端文件url,这里填写服务器提供的上传文件夹
    server_dir = '/Users/ccf/Desktop/experiment/upload/client/download'

    def __init__(self, server_address, bind_and_activate=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise  # 中断程序

    def server_bind(self):
        """
        由构造函数调用以绑定套接字
        """
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        """
        由构造函数调用监听
        """
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """
        由构造函数调用关闭服务器套接字
        """
        self.socket.close()

    def get_request(self):
        """
        接收客户端请求
        """
        return self.socket.accept()

    def close_request(self, request):
        """
        关闭单个客户端请求
        """
        request.close()

    def run(self):
        while True:
            self.conn, self.client_addr = self.get_request()
            print('from client ', self.client_addr)
            while True:
                try:
                    # 收客户端的报头长度
                    head_struct = self.conn.recv(4)
                    if not head_struct:
                        break
                    head_len = struct.unpack('i', head_struct)[0]
                    # 收客户端的序列化报头，解析出数据的真实信息（报头字典）
                    head_json = self.conn.recv(head_len).decode(self.coding)
                    head_dic = json.loads(head_json)  # 反序列化报头

                    print(head_dic)
                    # 4.解析命令
                    cmd = head_dic['cmd']
                    if hasattr(self, cmd):
                        func = getattr(self, cmd)
                        func(head_dic)
                except Exception:
                    break

    def put(self, args):
        # 规范path字符串形式,把目录和文件名合成一个路径
        file_path = os.path.normpath(os.path.join(
            self.server_dir,
            args['filename']
        ))

        filesize = args['filesize']
        recv_size = 0
        print('----->', file_path)
        # 接收真实数据
        with open(file_path, 'wb') as f:
            while recv_size < filesize:
                recv_data = self.conn.recv(self.max_packet_size)
                f.write(recv_data)
                recv_size += len(recv_data)

# 服务器绑定端口
tcpserver1 = MYTCPServer(('127.0.0.1', 8080))

# 服务器运行
tcpserver1.run()
