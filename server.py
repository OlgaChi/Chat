import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # создаем сервер
server.bind(("localhost", 1111)) # привязываем сервер к локальному порту

server.listen()

client, address = server.accept() # принял клиента

flag= True

while flag:
    msg = client.recv(1024).decode("utf-8")
    if msg == "quit" :
        flag = False
    else:
            print(msg)
            client.send(input("Пользователь2: ").encode("utf-8"))

client.close()
server.close()


