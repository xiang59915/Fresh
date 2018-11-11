import socket as s   # 导入socket模块

PORT = 2333   # 设置端口号为2333
HOST = s.gethostname()   # 获取本地IP地址
s.socket.bind((HOST, PORT))
s.socket.listen()

print("FTP 等待接收...")

while True:
	conn, addr = s.socket.accept()
	print("客户端的IP地址和端口信息",addr)
	data = conn.recv(1024)
	print("客户端发过来的文件",repr(data))

	FileName = input("输入一个文件名用于接收客户端发过来的文件例如test.txt")
	f = open(FileName, 'rb')
	


