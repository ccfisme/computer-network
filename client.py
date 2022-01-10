import socket
import struct
import json
import os

# 这个是客户端对象
class MYTCPClient:
    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    max_packet_size = 8192

    coding = 'utf-8'

    request_queue_size = 5

    def __init__(self, server_address, connect=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise

    def client_connect(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    # 客户端接收输入的文件路径
    def run(self):
        while True:
            inp = input(">>: ").strip()
            if not inp:
                continue
            # 用cmd存文件路径
            l = inp.split()
            cmd = l[0]
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(l)

    def put(self, args):
        # 查找文件路径
        cmd = args[0]
        filename = args[1]
        # 判断路径下内容是否为文件
        if not os.path.isfile(filename):
            print('file:%s is not exists' % filename)
            return
        else:
            filesize = os.path.getsize(filename)
        # 1.制作固定长度的报头
        head_dic = {'cmd': cmd, 'filename': os.path.basename(filename), 'filesize': filesize}  # 返回文件名
        # 1.1序列化报头,序列化为byte字节流类型
        head_json = json.dumps(head_dic)
        # 1.2编码为utf-8
        head_json_bytes = bytes(head_json, encoding=self.coding)
        # 2.先发送报头的长度
        # 2.1 将byte类型的长度打包成4位int
        head_struct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_struct)
        # 2.2 再发报头
        self.socket.send(head_json_bytes)
        send_size = 0
        # 2.3 再发真实数据
        with open(filename, 'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size += len(line)
                # print(send_size)
            else:
                print('upload successful')

# 客户端绑定端口
client = MYTCPClient(('127.0.0.1', 8080))

# 客户端运行
client.run()
