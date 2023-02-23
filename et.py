import os, socket, threading

bind_ip = '127.0.0.1'
bind_port_min = 50100
bind_port_max = 50199

def link():
    pass

def unlink():
    pass

def fly():
    pass

def land():
    pass

def send_msg():
    pass

def send_file():
    pass

def disconnect():
    pass


if __name__=="__main__":
    """
    
    
    """

    bind_port = 
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