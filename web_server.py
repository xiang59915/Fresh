import socket
import mutiprocessing
import re


class WSGI_SERVER(object):
    def __init__(self):
        self.tcp_server_socket = socket.socket()
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_ip, self.server_port = "", 2333

        self.tcp_server_socket.bind((self.server_ip, int(self.server_port)))
        self.tcp_server_socket.listen(128)

    def service_client(new_socket, request):
        request = new_socket.recv(1024).decode("utf-8")

        request_lines = request.splitlines()
        print(request_lines)

        back_html = ""
        ret = re.match(r"[^/]+([^ ]*)", request_lines[0])
        if ret:
          back_html = ret.group(1)
          if back_html == "/":
            back_html = "/index.html"


        try:
          f = open("")

        
        
if __name__ == "__main__":
    main()
