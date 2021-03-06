import socket as s              # Import socket module

client = s.socket()             # Create a socket object
PORT = 2333                    # Reserve a port for your service.

client.connect(("localhost", PORT))
client.send("Hello server!").encode("utf-8")

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

