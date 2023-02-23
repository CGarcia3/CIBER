import socket, threading

bind_ip = '127.0.0.1'
bind_port = 50001


def fly():
    pass

def land():
    pass

def send_msg():
    pass

def send_file():
    pass

def get_status():
    pass

def shutdown():
    pass

def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    if request["msg_type"] == "FLY":
        fly()
    client_socket.send('ACK!')
    client_socket.close()


if __name__=="__main__":
    """
    Al ejecutar esta file se crea una base de operaciones (si no existe ya una)
    y se queda escuchando mensajes y creando un fork para cada uno que llegue,
    ocupandose ese fork de la funcionalidad
    """

    # Creamos el socket...
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server.connect_ex((bind_ip, bind_port)) == 0:
        print("Base de operaciones ya existe.\n")
    # Lo asociamos a la IP y puerto correctos...
    server.bind((bind_ip, bind_port))
    # Y decimos al SO que atienda por nosotros hasta 5 conexiones
    server.listen(5)

    print('Escuchando en {}:{}'.format(bind_ip, bind_port))

    while True:
        client_sock, address = server.accept()
        print('Aceptada conexion de {}:{}'.format(address[0], address[1]))

        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,)  
        )
        client_handler.start()
