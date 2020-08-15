import socket
import threading

# 接收缓冲区大小
buff_size = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 8001))
# 最多可以连接多少个客户端
server_socket.listen(1)
print('Waiting for connections')


def receive_msg(sock):
    while True:
        recv_msg = sock.recv(buff_size)
        print(recv_msg.decode('utf-8'))


while True:
    sock, addr = server_socket.accept()
    print(sock, addr)
    thread = threading.Thread(target=receive_msg, args=(sock,))
    thread.start()
