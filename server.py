import socket

def run_server():
    # Configuración del servidor
    host = 'localhost'
    port = 5000
    
    # Crear socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Configurar socket para reutilizar direcciones
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Vincular socket al puerto
        server_socket.bind((host, port))
        
        # Escuchar conexiones entrantes
        server_socket.listen(1)
        print(f"Servidor TCP iniciado en {host}:{port}. Esperando conexiones...")
        
        while True:
            try:
                # Aceptar nueva conexión
                conn, addr = server_socket.accept()
                print(f"\nConexión establecida con {addr}")
                
                with conn:
                    while True:
                        # Recibir datos del cliente
                        data = conn.recv(1024)
                        if not data:
                            break
                            
                        message = data.decode().strip()
                        print(f"Mensaje recibido: '{message}'")
                        
                        # Verificar si el cliente solicitó desconexión
                        # y enviar respuesta
                        if message.upper() == "DESCONEXION":
                            print("Cliente solicitó desconexión. Cerrando conexión...")
                            break
                        elif message.upper() == "HOLA SERVER":
                            # Enviar la respuesta en mayúsculas
                            response = "HOLA CLIENTE"
                            conn.sendall(response.encode())
                            print(f"Respuesta enviada: '{response}'")
                        else:
                            # Enviar respuesta en mayúsculas
                            response = message.upper()
                            conn.sendall(response.encode())
                            print(f"Respuesta enviada: '{response}'")
                
                print(f"Conexión con {addr} cerrada. Listo para nuevas conexiones.")
                
            except KeyboardInterrupt:
                print("\nServidor detenido por el usuario.")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    run_server()