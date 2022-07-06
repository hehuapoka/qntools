
import socket,sys,json

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务，指定主机和端口
s.connect(("127.0.0.1", 10340))

# 接收小于 1024 字节的数据
xx=json.dumps({"Cmd":1,"Args":r"E:\Work\dev\qntools\scripts\cgteamwork\test1.py"})
s.send(xx.encode("utf-8"))

msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))