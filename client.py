import socket
import password
enter = True
query = "Введите логин: "
while enter:
    login = input(query)
    if login in password.users:
        enter = False
        passwords = input("Введите пароль: ")
        if passwords == password.users[login]:
            print("welcome")

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            client.connect(('localhost', 1111))

            flag=True
            while flag:
                client.send(input("Пользователь1: ").encode("utf-8"))
                msg= client.recv(1024).decode("utf-8")
            if msg == "quit" :
                flag =False
            else:
                print(msg)
        else:
            print("не верный пароль")
    else:
        query = "wrong"
        client.close()

