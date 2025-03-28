import socket


def run_client():
    # Configuración del cliente
    host = 'localhost'
    port = 5000
    
    # Crear socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Conectar al servidor
            client_socket.connect((host, port))
            print(f"Conectado al servidor {host}:{port}")
            print("Escriba la palabra 'DESCONEXION' para terminar la conexión.\n")
            
            while True:
                # Solicitar mensaje al usuario
                message = input("Ingrese mensaje: ")
                
                # Enviar mensaje al servidor
                client_socket.sendall(message.encode())
                
                # Verificar si el usuario solicitó desconexión
                if message.upper() == "DESCONEXION":
                    print("Solicitando desconexión...")
                    break
                
                # Recibir respuesta del servidor
                response = client_socket.recv(1024).decode()
                print(f"Respuesta del servidor: {response}")
                
        except ConnectionRefusedError:
            print("Error: No se pudo conectar al servidor. Asegúrese que el servidor está ejecutándose.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Conexión cerrada.")

if __name__ == "__main__":
    run_client()