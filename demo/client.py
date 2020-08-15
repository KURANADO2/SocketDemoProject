import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8001))
while True:
    msg = input('Please input msg:')
    # 退出
    if msg == 'exit':
        break
    # 空内容
    if not msg:
        continue
    client_socket.send(msg.encode('utf-8'))
    print(msg)
