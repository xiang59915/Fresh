import socket, re, gevent
from gevent import monkey

monkey.patch_all()  # 猴子补丁 解阻塞


def service(new_socket):
    '''服务新客户端'''
    request = new_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()

    print(request_lines)

    file_name = ""
    ret = re.match(r"[^/]+([^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    '''返还给浏览器数据'''
    try:
        f = open("../html" + file_name, "rb")
    except:
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        response += "<h1>404 NOT FOUND</h1>"
        return response
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"

        html_content = f.read()
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)

    new_socket.close()  # 关闭套接字


def main():
    tcp_server_socket = socket.socket()
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 避免端口占用
    tcp_server_socket.bind(("", 7890))

    tcp_server_socket.listen(128)

    while True:
        new_client, client_addr = tcp_server_socket.accept()
        gevent.spawn(service, new_client)

    tcp_server_socket.close()  # 关闭套接字


if __name__ == '__main__':
    main()
