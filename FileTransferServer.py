# xiang59915练习
import socket as s   # 导入socket模块
import os

server = s.socket()   # 创建套接字
PORT = 2333   # 设置端口号为2333
server.bind(("localhost", PORT))
server.listen(8)

print("等待客户端连接...")

while True:
	conn, addr = server.accept()
	print("客户端的IP地址和端口信息",addr)
	data = conn.recv(1024)
	print("客户端回应",repr(data))

	FileName = os.path.basename(os.path.realpath(__file__))
	f = open(FileName, 'rb')
	InData = f.read(1024)
	while InData:
		conn.send(InData)
		print('sent', repr(InData))
		InData = f.read(1024)
	f.close()

	print('传输完成')
	conn.send("感谢使用本次FTP服务")
	conn.close()




